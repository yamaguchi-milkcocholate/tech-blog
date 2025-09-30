# scripts/nb2post.py
import base64
import json
import sys
from pathlib import Path

NB = Path(sys.argv[1])
OUT = Path(sys.argv[2])  # content/drafts or content/posts
ASSETS = Path("assets") / NB.stem
ASSETS.mkdir(parents=True, exist_ok=True)

nb = json.loads(Path(NB).read_text())
md_lines = []

for cell in nb["cells"]:
    if cell.get("cell_type") == "markdown":
        src = "".join(cell.get("source", []))
        if "[post]" in src or "[POST]" in src:
            md_lines.append(src)
    elif cell.get("cell_type") == "code":
        src = "".join(cell.get("source", []))
        if "# [post]" in src or "# [POST]" in src:
            md_lines.append(f"```python\n{src}\n```\n")
    # 画像抽出（display_data）
    for out in cell.get("outputs", []):
        data = out.get("data", {})
        if "image/png" in data:
            b64 = data["image/png"]
            img_bytes = base64.b64decode(b64)
            idx = len(list(ASSETS.glob("*.png"))) + 1
            img_path = ASSETS / f"{NB.stem}_{idx}.png"
            img_path.write_bytes(img_bytes)
            md_lines.append(f"![](/assets/{NB.stem}/{img_path.name})\n")

post = "\n\n".join(md_lines).strip() + "\n"

# 先頭にテンプレフロントマターを付与（ドラフト扱い）
frontmatter = "\n".join(
    [
        "---",
        f'title: "{NB.stem}"',
        'date: ""',
        'updated: ""',
        "category: [analysis]",
        "tags: []",
        'author: "Teppei Yamaguchi"',
        f'slug: "{NB.stem}"',
        "status: draft",
        "---",
        "",
    ]
)

OUT.mkdir(parents=True, exist_ok=True)
(Path(OUT) / f"{NB.stem}.md").write_text(frontmatter + post)
print(f"Wrote: {(Path(OUT) / f'{NB.stem}.md').as_posix()}")
