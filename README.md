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

## Use as library

```python
from ghbook import convert_file

convert_file("path/to/book.htm", "path/to/output.txt")
```

## Supported HTML patterns

Example HTML files are included in `htmlbooks/` to demonstrate these structures.

- Book and chapter headings such as `content_h2` / `content_h3` are emitted with `##` prefix.
- Paragraph text is extracted from `content_paragraph` and `content_text`.
- Page markers like `ص: 531` are converted to `PAGE_SEPARATOR:`.
- `<hr class="content_hr">` with following `content_note` blocks are emitted as:

```text
____________
<footnote text>
```

Main text is preserved as-is; footnotes are appended below the separator.

## PyPI trusted publisher (GitHub Actions OIDC)

This repository is prepared for publishing to PyPI using a trusted publisher workflow at:

- `.github/workflows/publish.yml`

### Configure on PyPI

1. Go to PyPI project settings for `ghbook` and open the publishing/trusted publisher section.
2. Add a GitHub trusted publisher with:
   - Owner: `Ciyoku`
   - Repository: `ghbook`
   - Workflow filename: `publish.yml`
3. Save.

### Release

Tag and push a version tag to publish:

```bash
git tag v0.1.0
git push origin v0.1.0
```

The workflow builds the package and publishes it to PyPI using OIDC, without API tokens.
