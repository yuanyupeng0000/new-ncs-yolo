import os
XML_DIR = './Annotations/'
JPG_DIR = './JPEGImages/'
xmls = os.listdir(XML_DIR)
jpgs = os.listdir(JPG_DIR)
xml_num_list = [xml[:-4] for xml in xmls]
jpg_num_list = [jpg[:-4] for jpg in jpgs]
for xml_num in xml_num_list:
    if xml_num not in jpg_num_list:
        os.remove(XML_DIR + xml_num + '.xml')
        print('delete {0}'.format(xml_num))
