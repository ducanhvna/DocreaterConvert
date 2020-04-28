# character level 
# Nhiem vu cua module laf chuyen tu dinh dang output cua doc creator sang character level ma tool khac cos the doc duoc Lableimg
# Output foler: OuputCharacterLevel

# Read all folder
# Each subfoder
#   
#   Read groud truth
#   Read OD
#   Write to xml data
#   Write to file to Output foder
#   Copy image to output folder


# Read all foder
import os
import glob
import xml.etree.ElementTree as ET
from xml.dom import minidom
def ReadGroudTruth(filepath):
    
    

    # parse an xml file by name
    mydoc = minidom.parse(filepath)

    items = mydoc.getElementsByTagName('textBlock')

    # one specific item attribute
    print('Item #1 attribute:')
    print(items[0].attributes['height'].value)

    # all item attributes
    print('\nAll attributes:')
    for elem in items:
        print(elem.attributes['height'].value)

    # one specific item's data
    print('\nItem #1 data:')
    print(items[0].firstChild.data)
    print(items[0].childNodes[0].data)

    # all items data
    print('\nAll item data:')
    for elem in items:
        print(elem.firstChild.data)



def ExtractData(folderpath, outLoction):
    # List all file
    mylist = [ReadGroudTruth(f) for f in glob.glob(folderpath+ "/*.od")]
    
    # Read ground truth


    print(mylist)
    return 1
Extract = lambda i,o : ExtractData(i,o)

directory = 'SampleData'
outputfoder = 'OuputCharacterLevel'
# Create Output foder if not exsts

if not os.path.exists(outputfoder):
    os.makedirs(outputfoder)

listfolder = [Extract(x[0], outputfoder) for x in os.walk(directory)]
print (listfolder)