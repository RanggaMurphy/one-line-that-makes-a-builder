import os
import shutil
import sys


def find_pitch_file():
    folder = os.path.dirname(os.path.abspath(__file__))
    env_folder = os.environ.get("MAKEFUN_BOT_DIR")
    if env_folder:
        env_pitch = os.path.join(env_folder, "pitch.txt")
        if os.path.isfile(env_pitch):
            return env_pitch
    return os.path.join(folder, "pitch.txt")


def run():
    pitch_file = find_pitch_file()
    if not os.path.isfile(pitch_file):
        sys.stderr.write("missing pitch file: %s\n" % pitch_file)
        return 1
    target_folder = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not target_folder:
        target_folder = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(target_folder, exist_ok=True)
    entry_file = os.path.join(target_folder, "entry.txt")
    shutil.copyfile(pitch_file, entry_file)
    if os.path.getsize(entry_file) != os.path.getsize(pitch_file):
        sys.stderr.write("copied entry does not match pitch size\n")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(run())
