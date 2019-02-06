#!/usr/bin/env python3
import argparse
from PIL import Image, ImageOps

parser = argparse.ArgumentParser(description='Coverts Images to MicroBitImage.')
parser.add_argument('files', metavar='FILES', type=Image.open, nargs='+', help='a list of images to be convered')
parser.add_argument('--BW', help='converts the images to black and white', action='store_true')
args=parser.parse_args()

def convertoGrayScaleMBITIMG(img, w, h):
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
        var += '");'
        return var

def convertoBlackWhiteMBITIMG(img, w, h):
        grayimg = ImageOps.grayscale(img)
        px = grayimg.load()
        varname = input("What will the varible be called: ")
        var = 'MicroBitImage {}("'.format(varname)
        for y in range(h-1, -1, -1):
            for x in range(0, w):
                pixelVal = px[x, y]
                if pixelVal > 0:
                    pixelVal = 1
                else:
                    pixelVal = 0
                var+="{}".format(pixelVal)
                if x == w-1:
                    var+="\\n"
                else:
                    var+=(",")
        var += '");'
        return var


def main():
    print(args)
    files = args.files

    for photo in files:
        img = photo
        h = img.height
        w = img.width
        if args.BW:
            var = convertoBlackWhiteMBITIMG(img,w,h)
        else:
            var = convertoGrayScaleMBITIMG(img,w,h)
        print(var)


if __name__ == "__main__":
    main()