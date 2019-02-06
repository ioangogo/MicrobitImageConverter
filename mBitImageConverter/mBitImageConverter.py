#!/usr/bin/env python3
import argparse, os
from PIL import Image, ImageOps

parser = argparse.ArgumentParser(description='Coverts Images to MicroBitImage.')
parser.add_argument('files', metavar='FILES', type=Image.open, nargs='+', help='a list of images to be convered')
parser.add_argument('--BW', help='converts the images to black and white', action='store_true')
args=parser.parse_args()

def convertoGrayScaleMBITIMG(img, w, h,path):
        grayimg = ImageOps.grayscale(img)
        px = grayimg.load()
        varname = os.path.basename(path).split(".")[0]
        var = 'MicroBitImage {}("'.format(varname)
        for y in range(0, h):
            for x in range(0, w):
                pixelVal = px[x, y]
                var+="{}".format(pixelVal)
                if x == w-1:
                    var+="\\n"
                else:
                    var+=(",")
        var += '");'
        return var

def convertoBlackWhiteMBITIMG(img, w, h, path):
        grayimg = ImageOps.grayscale(img)
        px = grayimg.load()
        varname = os.path.basename(path).split(".")[0]
        var = 'MicroBitImage {}("'.format(varname)
        for y in range(0, h):
            for x in range(0, w):
                pixelVal = px[x, y]
                var+="{}".format(int(pixelVal>0))
                if x == w-1:
                    var+="\\n"
                else:
                    var+=(",")
        var += '");'
        return var


def main():
    files = args.files

    for photo in files:
        img = photo
        h = img.height
        w = img.width
        path = img.filename
        if args.BW:
            var = convertoBlackWhiteMBITIMG(img,w,h,path)
        else:
            var = convertoGrayScaleMBITIMG(img,w,h,path)
        print(var)


if __name__ == "__main__":
    main()