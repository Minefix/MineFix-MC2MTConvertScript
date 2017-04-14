#!/bin/python3

import os, sys, math
import shutil
import argparse
import tempfile
import zipfile

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

def unpack_assets(jar_path, out_path):
    if not zipfile.is_zipfile(jar_path):
        print("Invalid jar file specified. Exiting.")
        sys.exit(1)
    
    minecraft_jar = zipfile.ZipFile(jar_path, "r")
    file_infolist = minecraft_jar.infolist()
    file_count = len(file_infolist)
    for entry in file_infolist:
        data = minecraft_jar.read(entry.filename)
        full_path = os.path.join(out_path, entry.filename)
        s_path, s_name = os.path.split(full_path)
        if s_name.endswith(".png"):
            if not os.path.exists(s_path):
                os.makedirs(s_path)
            file_out = open(full_path, 'wb')
            file_out.write(data)
            file_out.close()
        #percent = math.floor(((file_infolist.index(entry)+1)/file_count)*100)
        #print("[%3i%%] %s" % (percent, full_path))
            print(full_path)

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

    print("Extracting jar...")
    unpack_assets(os.path.join(minecraft_dir, minecraft_version, minecraft_version + ".jar"), mctomt_tempdir.name)
    print("Extraction complete.")

    print("NOTE: This is as far as it goes atm. If you press any key, the temp folder will be deleted before the script exits.")
    print("The folder can be found at", mctomt_tempdir.name)
    input()
