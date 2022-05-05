from argparse import ArgumentParser
from sys import stderr
from turtle import color
from pyfqmr import Simplify
import trimesh as tr
from os.path import exists
from yaspin import yaspin

def target_mesh_count(s: str) -> int:
    out = int(s)
    if out < 1:
        raise ValueError("mesh count must be positive!")
    if out < 1000:
        stderr.write("target mesh count less than 1000! The results will not be very detailed...")
        stderr.flush()
    return out

def iterations(s: str) -> int:
    i = int(s)
    if i < 1:
        raise ValueError("iterations count must be positive!")
    return i

def path_arg(s: str):
    if not exists(s):
        raise ValueError(f"invalid path '{s}'")
    return s

def main():
    parser = ArgumentParser("pyfqmr-cli", description="Reduce the size of a triangle mesh using the pyfqmr library.")
    parser.add_argument("input", type=path_arg, help="The path to your input .stl file.")
    parser.add_argument("target", type=target_mesh_count, help="The amount of triangles you would like to have at most.")
    parser.add_argument("output", type=str, help="The path to where you want to save the simplified .stl file.")
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument("-a", "--aggressivity", type=int, help="Controls how aggressively the triangles are culled. Default is 3", default=3)
    parser.add_argument("-n", "--no-preserve-border", action="store_true", help="Disables border-preserving behavior.")
    parser.add_argument("-i", "--iterations", type=iterations, help="Determines how many iterations the algorithm should run. Default is 1024.", default=1024)
    args = parser.parse_args()

    model = None
    with yaspin(text="Loading mesh...", color="green") as spinner:
        try:
            model = tr.load_mesh(args.input, "stl")
            spinner.ok('✔')
        except Exception as e:
            spinner.fail('❌')
            print(f"Could not load mesh from path '{args.input}', is this an .stl file?")
            print(e)
            return
    simplifier = Simplify()
    with yaspin(text="Simplifying mesh...", color="yellow") as spinner:
        try:
            simplifier.setMesh(model.vertices, model.faces)
            verb = 10 if args.verbose else 0
            simplifier.simplify_mesh(target_count = args.target, aggressiveness=args.aggressivity, preserve_border=not args.no_preserve_border, verbose=verb, max_iterations=args.iterations)
            spinner.ok('✔')
        except Exception as e:
            spinner.fail('❌')
            print("Could not simplify mesh, something went wrong!")
            print(e)
            return
    with yaspin(text="Outputting simplified mesh...", color="blue") as spinner:
        try:
            verts, faces, norms = simplifier.getMesh()
            out_mesh = tr.Trimesh(verts, faces, norms)
            with open(args.output, "wb") as o_fp:
                out_mesh.export(o_fp, 'stl')
                spinner.ok('✔')
        except Exception as e:
            spinner.fail('❌')
            print("Could not export the mesh for some reason :(")
            print(e)
            return
    print("Thank you for using fqmr, pyfqmr and pyfqmr-cli, have a nice day!")
    pass

if __name__ == "__main__":
    main()
