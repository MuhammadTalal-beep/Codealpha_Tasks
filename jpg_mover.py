"""Move .jpg files from one directory to another

Usage:
    python jpg_mover.py <source_dir> <target_dir>

The script scans the source directory for files ending in .jpg or .jpeg
(case-insensitive) and moves them into the target directory, creating it
if necessary.
"""
import os
import shutil
import sys


def main() -> None:
    if len(sys.argv) == 3:
        src, dst = sys.argv[1], sys.argv[2]
    else:
        print("No directories provided on command line.")
        src = input("Source directory: ").strip()
        dst = input("Target directory: ").strip()
        if not src or not dst:
            print("Source and target directories are required.")
            sys.exit(1)

    if not os.path.isdir(src):
        print(f"Source directory does not exist: {src}")
        sys.exit(1)

    os.makedirs(dst, exist_ok=True)

    moved = 0
    found_any = False
    for name in os.listdir(src):
        print(f"Checking: {name}")
        if name.lower().endswith(('.jpg', '.jpeg')):
            found_any = True
            src_path = os.path.join(src, name)
            dst_path = os.path.join(dst, name)
            try:
                shutil.move(src_path, dst_path)
                print(f"  moved {name}")
                moved += 1
            except Exception as e:
                print(f"  Failed to move {name}: {e}")
    if not found_any:
        print("No .jpg or .jpeg files were found in the source directory.")
    print(f"Moved {moved} file(s) from {src} to {dst}")


if __name__ == '__main__':
    main()
