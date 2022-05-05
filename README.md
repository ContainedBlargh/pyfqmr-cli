# pyfqmr-cli

A commandline interface for the [pyfqmr](https://github.com/Kramer84/pyfqmr-Fast-Quadric-Mesh-Reduction) port by [Kramer84](https://github.com/Kramer84), which is a Cython-implementation of [Fast-Quadric-Mesh-Simplification](https://github.com/sp4cerat/Fast-Quadric-Mesh-Simplification) by [sp4cerat](https://github.com/sp4cerat).

## Motivation

A simple CLI-tool for handling the details that arise 

## Usage

```
usage: pyfqmr-cli [-h] [-v] [-a AGGRESSIVITY] [-n] [-i ITERATIONS] input target output

Reduce the size of a triangle mesh using the pyfqmr library.

positional arguments:
  input                 The path to your input .stl file.
  target                The amount of triangles you would like to have at most.
  output                The path to where you want to save the simplified .stl file.

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose
  -a AGGRESSIVITY, --aggressivity AGGRESSIVITY
                        Controls how aggressively the triangles are culled. Default is 3
  -n, --no-preserve-border
                        Disables border-preserving behavior.
  -i ITERATIONS, --iterations ITERATIONS
                        Determines how many iterations the algorithm should run. Default is 1024.  
```

