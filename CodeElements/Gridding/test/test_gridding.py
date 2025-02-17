import os
import argparse
import time
import shutil
import sys
sys.path.append('../src')
from gridding import GriddingLefDefInterface


if __name__ == '__main__':
    design = "ariane"
    src_dir = "../src"
    setup_file = "setup.tcl"
    tolerance = 0.05
    halo_width = 0.05
    openroad_exe = "./openroad"  # You need to specify the openroad exe

    GriddingLefDefInterface(src_dir, design, setup_file, tolerance, halo_width, openroad_exe)

