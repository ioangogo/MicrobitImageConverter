from PIL import ImageOps

def convertoGrayScaleMBITIMG(img, w, h, varname):
        grayimg = ImageOps.grayscale(img)
        px = grayimg.load()
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

def convertoBlackWhiteMBITIMG(img, w, h, varname):
        grayimg = ImageOps.grayscale(img)
        px = grayimg.load()
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