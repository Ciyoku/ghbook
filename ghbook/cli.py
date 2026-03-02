from __future__ import annotations

import sys
from pathlib import Path

from .converter import convert_html_to_text, resolve_output_path


def main() -> int:
    args = sys.argv[1:]
    if len(args) < 1 or len(args) > 2:
        return 1
    input_path = Path(args[0])
    output_path = resolve_output_path(input_path, Path(args[1]) if len(args) == 2 else None)
    if not input_path.exists() or not input_path.is_file():
        return 1
    convert_html_to_text(input_path, output_path)
    return 0
