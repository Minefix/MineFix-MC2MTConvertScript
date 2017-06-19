# MineFix - Minecraft2Minetest Asset Converter
A script for MineFix to convert Minecraft assets for use in Minetest.

To view the help run:

    ./mc2mt.py -h

**Requires Python 3!**

This script requires `PIL`/`pillow` to work. This can be downloaded via pip: `pip3 install pillow`.

Furthermore if `tqdm` (`pip3 install tqdm`) is installed, a progress bar can be shown with the `-p` argument.

*Sounds will be handled later.*

## Adding new assets

Textures are stored in the `textures` section of the file list. Below is a listing of keys and what they do.

* `in_file` `file || [file_1, file_2, file_n]` - Input file(s) which may be an array. Files in an array will be stiched together unless `door` is present.

* `out_file` `file` - Output file.

* `door` `[w, h, x, y]` - Take two door halves, stack them and then mirror them into double doors. Takes an array to specify where the door halves are.

* `crop` `[w, h, x, y]` - Crop a texture. As above the coords are reversed from the way you'd expect with width and height preceding x and y.

* `flip_x` `true/false` - Flip texture horizontally

* `flip_y` `true/false` - Flip texture vertically

* `rotate` `0/90/180/270` - Rotate texture

* `transparent` `[r,g,b]` - Make colour value in texture transparent

Two important notes:

1. `door` may not be used with any other operation (crop, flip_x/y, rotate, transparent)

2. Input arrays only presently support cropping. This will be fixed later.
