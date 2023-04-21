import os
import sys
import re

def batch_rename(directory, pattern, replace_with):
    if not os.path.isdir(directory):
        print(f"{directory} not found.")
        return

    print(f"Renaming files in {directory}...")

    files = os.listdir(directory)
    renamed_files = 0

    for file in files:
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            new_file_name = re.sub(pattern, replace_with, file)
            new_file_path = os.path.join(directory, new_file_name)
            os.rename(file_path, new_file_path)
            renamed_files += 1

    print(f"{renamed_files} files have been renamed.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python batch_rename.py <directory> <pattern> <replace_with>")
        sys.exit(1)

    directory = sys.argv[1]
    pattern = sys.argv[2]
    replace_with = sys.argv[3]
    batch_rename(directory, pattern, replace_with)

