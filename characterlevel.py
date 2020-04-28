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
directory = 'SampleData'
os.walk(directory)
listfolder = [x[0] for x in os.walk(directory)]
print (listfolder)