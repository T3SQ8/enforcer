import os

from .finder import find_violating_paths


def main(path: str):
    structure_violators, whitespace_violators = find_violating_paths(path)
    for v in structure_violators:
        print("Path violating structure:", v)
    print("Total structure violating files:", len(structure_violators))
    for v in whitespace_violators:
        print("Path violating whitespace:", v)
    print("Total whitespace violating files:", len(whitespace_violators))


if __name__ == "__main__":
    import argparse

    def dir_path(path):
        if os.path.isdir(path):
            return path
        raise argparse.ArgumentTypeError(f"'{path}' is not a valid directory")

    parser = argparse.ArgumentParser(
        description="manage and structure large directories"
    )
    parser.add_argument(
        "target_dirs", metavar="PATH", nargs="+", type=dir_path, help="target paths"
    )

    args = parser.parse_args()

    for path in args.target_dirs:
        main(path)
