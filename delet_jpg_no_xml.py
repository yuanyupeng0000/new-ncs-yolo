import os
XML_DIR = './Annotations/'
JPG_DIR = './JPEGImages/'
xmls = os.listdir(XML_DIR)
jpgs = os.listdir(JPG_DIR)
xml_num_list = [xml[:-4] for xml in xmls]
jpg_num_list = [jpg[:-4] for jpg in jpgs]
for jpg_num in jpg_num_list:
    if jpg_num not in xml_num_list:
        os.remove(JPG_DIR + jpg_num + '.jpg')
        print('delete {0}'.format(jpg_num))
