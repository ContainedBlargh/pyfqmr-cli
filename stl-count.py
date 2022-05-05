from argparse import ArgumentParser
from os.path import exists
import trimesh as tr
from yaspin import yaspin

def path_arg(s: str):
    if not exists(s):
        raise ValueError(f"invalid path '{s}'")
    return s

def main():
    parser = ArgumentParser("stl-count", description="Counts the amount of faces (polys) in a .stl file.")
    parser.add_argument("path", type=path_arg, help="Path to the stl file you need counted.")
    args = parser.parse_args()
    mesh = None
    with yaspin(text="Loading mesh...", color="green") as spinner:
        try:
            mesh: tr.Trimesh = tr.load_mesh(args.path, "stl")
            spinner.ok('✔')
        except Exception as e:
            spinner.fail('❌')
            print(f"Could not load mesh from path '{args.input}', is this an .stl file?")
            print(e)
            return
    count = f"{len(mesh.faces):,}".replace(',', ' ')
    print(f"{args.path}:\t{count}")
    pass

if __name__ == "__main__":
    main()
