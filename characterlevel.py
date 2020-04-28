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

def ExtractData(folderpath, outLoction):
    
    return 1
Extract = lambda i,o : ExtractData(i,o)

directory = 'SampleData'
outputfoder = 'OuputCharacterLevel'
# Create Output foder if not exsts

if not os.path.exists(outputfoder):
    os.makedirs(outputfoder)

listfolder = [Extract(x[0], outputfoder) for x in os.walk(directory)]
print (listfolder)