import sys
import xml.etree.ElementTree as ET


def get_product_parts(jdfPath):
    it = ET.iterparse(jdfPath)
    tree = ET.parse(jdfPath)
    for _, el in it:
        if '}' in el.tag:
            el.tag = el.tag.split('}', 1)[1]
    root = it.root
    # root = tree.getroot()
    jdfs = root.findall('JDF')
    for child in jdfs:
        print(child.tag)


get_product_parts('M3Job10242.jdf')
