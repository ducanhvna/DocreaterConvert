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
# Khac voiw paragraph level, trong de dinh dang word level can split thanh tung block 
# Xu ly them ca truong hop xuong dong nua vi o day cha co block nao
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

    filelines = []

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
                lines = []  # Luu thong tin tat ca cac dong moi dong la tap hop cac diem
                # tach tat ca cac line
                line = [] #Thong tin 1 dong
                prveviosx = -1
                for celem in chars:
                    if int(celem.attributes['x'].value) < prveviosx:
                        prveviosx = -1
                        lines.append(line)
                        line = [celem]
                    else:
                        line.append(celem)
                        prveviosx = int(celem.attributes['x'].value)

                lines.append(line)



                for line in lines:
                    words = [] # luu thong tin tat ca cac words
                    word = [] # luu thong tin 1 word
                    for celem in line:
                        if celem.attributes['display'].value is ' ':
                            words.append(word)
                            word = []
                        else:
                            word.append(celem)
                    words.append(word)

                    for word in words:
                        if len(word)>0:
                            displayvalues = [celem.attributes['display'].value for celem in word]
                            xvalues = [blockx + int(celem.attributes['x'].value) for celem in word]
                            yvalues = [blocky + int(celem.attributes['y'].value) for celem in word]
                            xmaxvalues = [ blockx + int(celem.attributes['x'].value) + int(celem.attributes['width'].value) for celem in word]
                            ymaxvalues = [ blocky + int(celem.attributes['y'].value) + int(celem.attributes['height'].value) for celem in word]

                            # each char add 1 element
                            objectele = ET.SubElement(data, 'object')
                            name = ET.SubElement(objectele, 'name')
                            name.text = convert(displayvalues)

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
                            
                            content = xmin.text + ',' + ymin.text + ',' + xmax.text + "," + ymin.text + "," + xmax.text + "," + ymax.text + "," + xmin.text + "," + ymax.text + "," + name.text
                            filelines.append(content)
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

        with open(outLoction + "/" + foldername + '.txt', 'w') as f:
            for item in filelines:
                f.write("%s\n" % item)
        
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