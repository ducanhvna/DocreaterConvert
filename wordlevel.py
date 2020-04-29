# Nhiem vu cuar module nay convert tat ca cacs thong tin ben trong thu muc sang dinh dang wordleve
# word level 

# Output foler: OuputWordLevel

# Read all folder
# Each subfoder
#   
#   Read groud truth
#   Read OD
#   Write to xml data
#   Write to file to Output foder
#   Copy image to output folder

# Khac voi character level, word level se dung lai o string


# Read all foder
import os
import glob
import xml.etree.ElementTree as ET
from xml.dom import minidom
import shutil
import datetime

def convert(s): 
    '''
    Convert a list of characters into a string
    '''

    # initialization of string to "" 
    new = "" 

    # traverse in the string  
    for x in s: 
        new += x  

    # return string  
    return new 

def ReadGroudTruth(filepath, foldername, outLoction):
     # create the file structure
    data = ET.Element('annotation')
    folder = ET.SubElement(data, 'folder')
    folder.text = 'windows_v1.8.0'
    
    filename = ET.SubElement(data, 'filename')
    path = ET.SubElement(data, 'path')
    source = ET.SubElement(data, 'source')

    database = ET.SubElement(source, 'database')
    database.text = 'Unknown'

   

    # parse an xml file by name
    mydoc = minidom.parse(filepath)

    # document common info
     # size
    size = ET.SubElement(data, 'size')
    width = ET.SubElement(size, 'width')
    root = items = mydoc.getElementsByTagName('document')[0]
    # print(root.attributes['width'].value)
    width.text = root.attributes['width'].value
    

    height = ET.SubElement(size, 'height')
    height.text = root.attributes['height'].value
    
    # fixed deep to 3
    depth = ET.SubElement(size, 'depth')
    depth.text = '3'

    # fixed segmented to 0
    segmented = ET.SubElement(data, 'segmented')
    segmented.text = '0'

    items = mydoc.getElementsByTagName('textBlock')

    # one specific item attribute
    print('Item #1 attribute:')
    print(items[0].attributes['height'].value)

    

    # all item attributes
    print('\nAll attributes:')
    for elem in items:
        print(elem.attributes['height'].value)
        pragraphs = elem.getElementsByTagName('paragraph')
        blockwidth = elem.attributes['width'].value
        blockheight = elem.attributes['height'].value
        blockx = int(elem.attributes['x'].value)
        blocky = int(elem.attributes['y'].value)

        for pragraph in pragraphs:
            strings = pragraph.getElementsByTagName('string')

            for s in strings:
                chars = s.getElementsByTagName('char')
                displayvalues = [celem.attributes['display'].value for celem in chars]
                xvalues = [blockx + int(celem.attributes['x'].value) for celem in chars]
                yvalues = [blocky + int(celem.attributes['y'].value) for celem in chars]
                xmaxvalues = [ blockx + int(celem.attributes['x'].value) + int(celem.attributes['width'].value) for celem in chars]
                ymaxvalues = [ blocky + int(celem.attributes['y'].value) + int(celem.attributes['height'].value) for celem in chars]

                # each char add 1 element
                objectele = ET.SubElement(data, 'object')
                name = ET.SubElement(objectele, 'name')
                name.text = "chardisplay"

                pose = ET.SubElement(objectele, 'pose')
                pose.text = 'Unspecified'

                truncated = ET.SubElement(objectele, 'truncated')
                truncated.text = '0'

                difficult = ET.SubElement(objectele, 'difficult')
                difficult.text = '0'

                bndbox = ET.SubElement(objectele, 'bndbox')
                xmin = ET.SubElement(bndbox, 'xmin')
                xmin.text = str(min(xvalues))

                ymin = ET.SubElement(bndbox, 'ymin')
                ymin.text = str(min(yvalues))

                xmax = ET.SubElement(bndbox, 'xmax')
                xmax.text = str(max(xmaxvalues))

                ymax = ET.SubElement(bndbox, 'ymax')
                ymax.text = str(max(ymaxvalues))

                # item1.set('name','item1')
                # create a new XML file with the results


                # for celem in chars:
                #     # character
                #     print(celem.attributes['display'].value)
                #     chardisplay = celem.attributes['display'].value
                #     charx = celem.attributes['x'].value
                #     chary = celem.attributes['y'].value
                #     charwidth = celem.attributes['width'].value
                #     charheight = celem.attributes['height'].value

                #     # each char add 1 element
                #     objectele = ET.SubElement(data, 'object')
                #     name = ET.SubElement(objectele, 'name')
                #     name.text = chardisplay

                #     pose = ET.SubElement(objectele, 'pose')
                #     pose.text = 'Unspecified'

                #     truncated = ET.SubElement(objectele, 'truncated')
                #     truncated.text = '0'

                #     difficult = ET.SubElement(objectele, 'difficult')
                #     difficult.text = '0'

                #     bndbox = ET.SubElement(objectele, 'bndbox')
                #     xmin = ET.SubElement(bndbox, 'xmin')
                #     xmin.text = str(int(blockx) + int(charx))

                #     ymin = ET.SubElement(bndbox, 'ymin')
                #     ymin.text = str(int(blocky) + int(chary))

                #     xmax = ET.SubElement(bndbox, 'xmax')
                #     xmax.text = str(int(xmin.text) + int(charwidth))

                #     ymax = ET.SubElement(bndbox, 'ymax')
                #     ymax.text = str(int(ymin.text) + int(charheight))

                    

                    
                #     # item1.set('name','item1')
                #     # create a new XML file with the results
        mydata = ET.tostring(data)
        myfile = open(outLoction + "/" + foldername + ".xml", "wb")
        myfile.write(mydata)

        
    # one specific item's data
    print('\nItem #1 data:')
    print(items[0].firstChild.data)
    print(items[0].childNodes[0].data)

    # all items data`
    print('\nAll item data:')
    for elem in items:
        print(elem.firstChild.data)

def WriteXml(filepath, outlocation):
    # create the file structure
    data = ET.Element('annotation')
    folder = ET.SubElement(data, 'folder')
    folder.text = 'windows_v1.8.0'

    filename = ET.SubElement(data, 'filename')
    path = ET.SubElement(data, 'path')
    source = ET.SubElement(data, 'source')

    database = ET.SubElement(source, 'database')

    # size
    size = ET.SubElement(data, 'size')
    width = ET.SubElement(size, 'width')
    height = ET.SubElement(size, 'height')
    depth = ET.SubElement(size, 'depth')

    segmented = ET.SubElement(data, 'segmented')
    objectele = ET.SubElement(data, 'object')
    name = ET.SubElement(objectele, 'name')
    pose = ET.SubElement(objectele, 'pose')
    truncated = ET.SubElement(objectele, 'truncated')
    difficult = ET.SubElement(objectele, 'difficult')
    # item1.set('name','item1')
    # create a new XML file with the results
    mydata = ET.tostring(data)
    myfile = open("items2.xml", "wb")
    myfile.write(mydata)

def ExtractData(folderpath, outLoction):
    # List all file
    foldername = os.path.basename(folderpath)
    mylist = [ReadGroudTruth(f, foldername, outLoction) for f in glob.glob(folderpath+ "/*.od")]
    
    # Copy and rename all image file
    for f in glob.glob(folderpath+ "/*.png"):
        src_dir=f
        dst_dir=outLoction + '/' + os.path.basename(folderpath) + ".png"
        shutil.copy(src_dir,dst_dir)
    # Read ground truth


    print(mylist)
    return 1
Extract = lambda i,o : ExtractData(i,o)

directory = 'SampleData'
outputfoder = 'OuputWordLevel'
# Create Output foder if not exsts

if not os.path.exists(outputfoder):
    os.makedirs(outputfoder)

listfolder = [Extract(x[0], outputfoder) for x in os.walk(directory)]
print (listfolder)
# WriteXml('sample',outputfoder)