"""
A python script transfer images to specific images format.
It supports any OpenCV file format.

Author: Thomas
License: Apache
Version: 0.0.1
Email: thomas@graphopti.com
Data: 2022-12-08
"""

import argparse
import math
import os
import sys

import cv2

# --help / -H argument
# --input / -i
# --output or -o
parser = argparse.ArgumentParser(
    description="",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
)
parser.add_argument(
    "-o", "--output_type", type=str, default="jpeg", help="output file type"
)
parser.add_argument(
    "src",
    help="Source location, should be a specific image file or a folder contain images",
)
parser.add_argument(
    "dest", help="Destination folder destination for format transferred images"
)
args = parser.parse_args()
config = vars(args)
print("Startring video_to_images.py with configuration:", config)
file_source = str(args.src)
file_destination = args.dest
# src check
if not (os.path.isdir(args.src) or os.path.exists(args.src)):
    sys.exit("The source" + args.dest + "is not a folder or file, exits")

# dest check
if not os.path.exists(args.dest):
    os.makedirs(args.dest)
if not os.path.isdir(args.dest):
    sys.exit("The destination " + args.dest + " is not a folder, exits")

# store images for single file
if not os.path.isdir(file_source):
    img = cv2.imread(file_source)
    if img is None:
        sys.exit("Could not load file " + file_source)
    dir_and_file = os.path.split(file_source)
    name_and_extention = os.path.splitext(dir_and_file[1])
    dest_file = file_destination + name_and_extention[0] + "." + args.output_type
    cv2.imwrite(dest_file, img)
    sys.exit("Success save the image at " + dest_file)
else:
    # store images for directory
    file_list = os.listdir(file_source)
    if file_list is None:
        sys.exit("No estimated image file at " + file_source)
    for file_ite in file_list:
        name_and_extention = os.path.splitext(file_ite)
        img = cv2.imread(file_source + file_ite)
        if img is None:
            continue
        dest_file = file_destination + name_and_extention[0] + "." + args.output_type
        cv2.imwrite(dest_file, img)
        print("Success save the image at " + dest_file)
