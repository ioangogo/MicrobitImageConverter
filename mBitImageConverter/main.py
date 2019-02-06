#!/usr/bin/env python3
import argparse
from PIL import Image, ImageOps

parser = argparse.ArgumentParser(description='Coverts Images to MicroBitImage.')
parser.add_argument('files', metavar='FILES', type=Image.open, nargs='+', help='a list of images to be convered')
args=parser.parse_args()

def main():
    print(args.files)
    files = args.files

    for photo in files:
        img = photo
        h = img.height
        w = img.width
        grayimg = ImageOps.grayscale(img)
        px = grayimg.load()
        varname = input("What will the varible be called: ")
        var = 'MicroBitImage {}("'.format(varname)
        for y in range(h-1, -1, -1):
            for x in range(0, w):
                pixelVal = px[x, y]
                var+="{}".format(pixelVal)
                if x == w-1:
                    var+="\\n"
                else:
                    var+=(",")
        var += '")'
        print(var)


if __name__ == "__main__":
    main()