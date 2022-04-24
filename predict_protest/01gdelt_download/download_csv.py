# -*- coding: utf-8 -*-
"""
Created on 2021

@author: Nisha
"""
import urllib.request
from zipfile import ZipFile
import os

hyperlinkpath = "../gdelt_download/hyperlinks_2018.txt"

print("Reading hyperlink file at " + hyperlinkpath)

linkFile = open(hyperlinkpath, 'r')
lines = linkFile.readlines()

print("***********************")
print("PARSING LINKS FROM FILE")
print("***********************")

links = list()
for line in lines:
    splitLine = line.split("\"")
    link = splitLine[1]
    print("Parsed link " + link + "from line " + line) 
    links.append(link)
    
print("************************")
print("DOWNLOAD DATA FROM LINKS")
print("************************")

for link in links:
    writeto = "../gdelt_download/" + link.split('/')[-1]
    urllib.request.urlretrieve(link, writeto)
    filename = link.split('/')[-1]
    with ZipFile(filename, 'r') as zip:
        zip.printdir()
        print('Extracting Files')
        zip.extractall('temp_2018')

print("DONE")
