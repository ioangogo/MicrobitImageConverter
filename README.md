Microbit Image converter
===

A small command line utility for converting images of 5x5 or less into a MicroBitImage.

# installing

```
# python3 setup.py install
```

## Example output

```
MicroBitImage north("0,0,255,0,0\n0,255,255,255,0\n255,0,255,0,255\n0,0,255,0,0\n0,0,255,0,0\n");
```

The variable name is based off of the file name

## Installing

```
# python3 setup.py install
```

## Usage


```
usage: mBitImageConverter [-h] [--BW] FILES [FILES ...]

Coverts Images to MicroBitImage.

positional arguments:
  FILES       a list of images to be convered

optional arguments:
  -h, --help  show this help message and exit
  --BW        converts the images to black and white
```