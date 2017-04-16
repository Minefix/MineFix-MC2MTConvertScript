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

asset_list = "filelist.txt"

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def setup_argparse():
    pass

def unpack_assets(jar_path, out_path):
    if not zipfile.is_zipfile(jar_path):
        eprint("Invalid jar file specified:", jar_path)
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

def extract_assets(asset_list_path, in_path, out_path):
    asset_list_fp = open(asset_list_path, "r")
    asset_list = asset_list_fp.readlines()
    for line in asset_list:
        line_s = line.strip()
        if line_s.startswith("#"):
            continue
        elif line_s.startswith("copy "):
            copycmd = line_s.split()
            try:
                shutil.copy(os.path.join(in_path, copycmd[1]), os.path.join(out_path, copycmd[2]))
                print("Copied file '%s' to '%s'" % (copycmd[1], os.path.join(out_path, copycmd[2])))
            except OSError as e:
                eprint("Error while copying file '%s'\n%s" % (copycmd[1], e))
                #sys.exit(1)
        elif line_s.startswith("convert "):
            pass
        else:
            eprint("Invalid command '%s' in line %i of \"%s\"\n  --> '%s'" % (line_s.split()[0], asset_list.index(line), asset_list_path, line_s))
            sys.exit(1)

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

    extract_assets(asset_list, os.path.join(mctomt_tempdir.name, "assets/minecraft/textures"), "/tmp/testdir")

    print("NOTE: This is as far as it goes atm. If you press any key, the temp folder will be deleted before the script exits.")
    print("The folder can be found at", mctomt_tempdir.name)
    input()
