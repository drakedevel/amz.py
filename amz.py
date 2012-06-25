#!/usr/bin/env python3
import xml.etree.ElementTree as ET
import sys

def gettracks(elem):
    tracklist = elem.find('trackList')
    for t in tracklist.iterfind('track'):
        artist = t.find('creator').text
        album = t.find('album').text
        loc = t.find('location').text.replace('+', ' ')
        print("mkdir -p '{0}/{1}'".format(artist, album))
        print("wget -P '{0}/{1}' '{2}'".format(artist, album, loc))

def process(filename):
    tree = ET.parse(filename)
    for ext in tree.iterfind('extension'):
        deluxe = ext.find('deluxe')
        if deluxe is not None:
            gettracks(deluxe)
    gettracks(tree)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        process(sys.argv[1])
    else:
        print("Usage: amz.py foo.amz")
