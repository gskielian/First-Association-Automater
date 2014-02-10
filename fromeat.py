#!/usr/local/bin/python

from xml.dom import minidom
import time
import sys

xmldoc = minidom.parse('eat-response-stimulus.xml')
itemlist = xmldoc.getElementsByTagName('stimulus')
print len(itemlist)
print itemlist[0].attributes['word'].value

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv[1])

time.sleep(1)
# for s in itemlist :
#     print s.attributes['word'].value
