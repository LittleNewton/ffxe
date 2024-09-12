from .engine import *

import sys
from os.path import realpath, dirname
from pathlib import Path
from glob import glob

import yaml

MMAP_DIR = Path(dirname(realpath(__file__))) / "mmaps"

mmaps = {}

for pd_file in glob(f"{str(MMAP_DIR)}/*.yml"):
    pdpath = Path(pd_file)
    pdname = pdpath.stem
    mmaps[pdname] = yaml.load(pd_file, yaml.Loader)