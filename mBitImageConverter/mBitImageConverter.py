#!/usr/bin/env python3
import argparse, os
from PIL import Image
from mBitImageConverter.functions import convertoBlackWhiteMBITIMG, convertoGrayScaleMBITIMG

parser = argparse.ArgumentParser(description='Coverts Images to MicroBitImage.')
parser.add_argument('files', metavar='FILES', type=Image.open, nargs='+', help='a list of images to be convered', )
parser.add_argument('--BW', help='converts the images to black and white', action='store_true')
args=parser.parse_args()

def main():
    files = args.files

    for photo in files:
        img = photo
        h = img.height
        w = img.width
        varname = os.path.basename(img.filename).split(".")[0]
        if args.BW:
            var = convertoBlackWhiteMBITIMG(img,w,h,varname)
        else:
            var = convertoGrayScaleMBITIMG(img,w,h,varname)
        print(var)


if __name__ == "__main__":
    main()