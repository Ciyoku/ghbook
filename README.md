# ghbook

Python library and CLI for converting GhBook-style HTML book files to clean `.txt` output while preserving book/chapter structure, page separators, and footnotes.

## Install

```bash
pip install ghbook
```

## Use as CLI

```bash
ghbook path/to/book.htm
ghbook path/to/book.htm path/to/output.txt
```

## Use as Library

```python
from ghbook import convert_file

convert_file("path/to/book.htm", "path/to/output.txt")
```

## Supported HTML patterns

Example HTML files are included in `htmlbooks/` to demonstrate these structures.

* Book and chapter headings such as `content_h2` / `content_h3` are emitted with `##` prefix.
* Paragraph text is extracted from `content_paragraph` and `content_text`.
* Page markers like `ص: 531` are converted to `PAGE_SEPARATOR:`.
* `<hr class="content_hr">` with following `content_note` blocks are emitted as:

```
____________
<footnote text>
```

Main text is preserved as-is; footnotes are appended below the separator.

## Notes

* The repository is prepared for publishing to PyPI using a Trusted Publisher workflow, but publishing is optional.
* GitHub Actions workflow is at `.github/workflows/publish.yml` for automatic builds if desired.
