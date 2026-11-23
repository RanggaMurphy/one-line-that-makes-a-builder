import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    bot_dir = os.environ.get("MAKEFUN_BOT_DIR")
    if bot_dir and os.path.isfile(os.path.join(bot_dir, "pitch.txt")):
        src = os.path.join(bot_dir, "pitch.txt")
    else:
        src = os.path.join(here, "pitch.txt")
    if not os.path.isfile(src):
        print("error: pitch.txt is missing next to main.py", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or here
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(out_dir, "entry.txt"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
