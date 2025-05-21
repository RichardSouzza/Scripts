"""
A Python script to unpack multiple zips from a directory.
"""

import os
from glob import glob
from shutil import unpack_archive


directory = "directory"

destination_dir = "destination_dir"

files = glob(os.path.join(directory, "*.zip"))

for file in files:
    print(f"Unzipping {file}...")
    unpack_archive(file, destination_dir)
