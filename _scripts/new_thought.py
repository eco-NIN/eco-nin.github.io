#!/usr/bin/env python3
"""生成一篇正文留空的感悟，使用北京时间且不覆盖已有文章。"""

from datetime import datetime, timedelta, timezone
from pathlib import Path


def main():
    now = datetime.now(timezone(timedelta(hours=8)))
    posts_dir = Path(__file__).resolve().parent.parent / "_posts"
    posts_dir.mkdir(exist_ok=True)
    stem = now.strftime("%Y-%m-%d-感悟-%H%M%S")
    template = (
        '---\n'
        'title: "一条感悟"\n'
        f'date: {now:%Y-%m-%d %H:%M:%S %z}\n'
        '---\n\n'
    )

    number = 1
    while True:
        suffix = "" if number == 1 else f"-{number}"
        post = posts_dir / f"{stem}{suffix}.md"
        try:
            with post.open("x", encoding="utf-8", newline="\n") as file:
                file.write(template)
            break
        except FileExistsError:
            number += 1

    print(f"已创建：{post}")
    print("打开文件，在第二个 --- 下方填写正文即可。")


if __name__ == "__main__":
    main()
