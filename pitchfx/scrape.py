#!/usr/bin/env python
import urllib2
from xml.dom import minidom

def getGameXmlDoc(game_url):
  return minidom.parse(urllib2.urlopen(game_url))

def printXmlAttrs(xmldoc, tagname, attrs):
  itemlist = xmldoc.getElementsByTagName(tagname)
  for item in itemlist:
    printstr=[]
    for attr in attrs:
      printstr += item.attributes[attr].value,
    print printstr

'''
game_xml = urllib2.urlopen('http://gd2.mlb.com/components/game/mlb/year_2014/month_06/day_10/gid_2014_06_10_wasmlb_sfnmlb_1/inning/inning_1.xml')
xmldoc = minidom.parse(game_xml)
'''

game_url = 'http://gd2.mlb.com/components/game/mlb/year_2014/month_06/day_10/gid_2014_06_10_wasmlb_sfnmlb_1/inning/inning_1.xml'
xmldoc = getGameXmlDoc(game_url)
printXmlAttrs(xmldoc, 'pitch', ['des', 'start_speed'])

'''
itemlist = xmldoc.getElementsByTagName('pitch')
for iteml in itemlist:
  print iteml.attributes['start_speed'].value
'''
