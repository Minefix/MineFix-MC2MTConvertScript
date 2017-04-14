#!/bin/python3

import os, sys
import shutil
import argparse
import tempfile

from PIL import Image

minecraft_version = "1.8.9"
minecraft_texpack = "Minecraft"

if (sys.platform == "win32"):
    pass # to do: see how to get Windows user folder
elif (sys.platform == "darwin"):
    pass # to do: ditto for mac
elif (sys.platform == "linux"):
    minecraft_dir = os.path.join(os.path.expanduser('~'), ".minecraft/versions")
    minetest_dir = os.path.join(os.path.expanduser('~'), ".minetest")

minetest_texdir = os.path.join(minetest_dir, "textures", minecraft_texpack)

def setup_argparse():
    pass

def unpack_assets(assets_path):
    pass

def extract_image(pos_x, pos_y, size_w = 16, size_h = 16):
    pass

if __name__ == "__main__":
    args = setup_argparse()

    print("Creating texture directory:", minetest_texdir)
    try:
        os.mkdir(minetest_texdir)
    except FileExistsError:
        print("Texture directory already exists. Skipping...")

    mctomt_tempdir = tempfile.TemporaryDirectory(prefix="mc2mt-")
    print("Created temporary directory:", mctomt_tempdir.name)
