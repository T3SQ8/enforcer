import os
import re

from whitelist import whitelist


def find_violating_paths(target: str) -> tuple[list, list]:
    structure_violators = []
    whitespace_violators = []
    for root, dirs, files in os.walk(target):
        whitespace_violators.extend(
            [
                os.path.join(root, path)
                for path in dirs + files
                if path.endswith(" ") or path.startswith(" ")
            ]
        )
        for path in [os.path.join(root, file) for file in files]:
            if not any(re.fullmatch(pattern, path) for pattern in whitelist):
                structure_violators.append(path)
    return structure_violators, whitespace_violators
