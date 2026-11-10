"""Wrap portfolio.artifact.html (page content) into a standalone index.html for self-hosting."""
from pathlib import Path

here = Path(__file__).parent
src = (here / "portfolio.artifact.html").read_text(encoding="utf-8")

head_end = src.index("</style>") + len("</style>")
head, body = src[:head_end], src[head_end:]
head = head.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', "")

page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="Marvyn Whittaker: diesel technician moving into fleet, equipment and maintenance data analytics. Evidence by skill area.">
{head}
</head>
<body>
{body.strip()}
</body>
</html>
"""
(here / "index.html").write_text(page, encoding="utf-8")
print(f"index.html written, {len(page):,} bytes")
