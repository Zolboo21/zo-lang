#!/usr/bin/env python3

import argparse
import sys
import os
from src.zo_parser import parse_zo_code
from src.zo_compiler import compile_to_python

def main():
    parser = argparse.ArgumentParser(description="Zo Language Compiler")
    parser.add_argument("source", help="Zo source file (.zo)")
    parser.add_argument("--run", action="store_true", help="Run the compiled Python file")
    args = parser.parse_args()

    with open(args.source) as f:
        zo_code = f.read()

    ast = parse_zo_code(zo_code)
    py_code = compile_to_python(ast)

    out_file = os.path.splitext(args.source)[0] + ".py"
    with open(out_file, "w") as f:
        f.write(py_code)

    print(f"Compiled to {out_file}")

    # ALWAYS run the compiled code
    os.system(f"python3 {out_file}")

if __name__ == "__main__":
    main()

