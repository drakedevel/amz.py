#!/usr/bin/env python3
import xml.etree.ElementTree as ET
import sys

def gettracks(elem):
    tracklist = elem.find('trackList')
    for t in tracklist.iterfind('track'):
        artist = t.find('creator').text
        album = t.find('album').text
        track = int(t.find('trackNum').text)
        title = t.find('title').text
        fileType = 'mp3'
        for m in t.iterfind('meta'):
            if m.attrib['rel'] == 'http://www.amazon.com/dmusic/trackType':
                fileType = m.text
                break
        loc = t.find('location').text
        print("mkdir -p '{0}/{1}'".format(artist, album))
        print("wget -U'Amazon MP3 Downloader (Win32 1.0.17 en_US)' -O '{0}/{1}/{2:02d} - {3}.{4}' '{5}'".format(artist, album, track, title, fileType, loc))

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
