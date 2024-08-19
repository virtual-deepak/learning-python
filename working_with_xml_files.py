import xml.etree.ElementTree as ElementTree

def parse_xml(file_name):
    tree = ElementTree.parse(file_name)
    root = tree.getroot()
    print(f"Domains for author: {root.attrib['name']}")
    for child in root:
        print(f"\t{child.attrib['name']}, {child.tag}")

def add_xml_element(file_name, tag_name, attribute, value):
    tree = ElementTree.parse(file_name)
    root = tree.getroot()
    child = ElementTree.Element(tag_name)
    child.attrib[attribute] = value
    root.append(child)
    tree.write(file_name)

parse_xml('./samples/files_to_read/ef_author.xml')
add_xml_element('./samples/files_to_read/ef_author.xml',
                'domain',
                'name',
                'Java')
parse_xml('./samples/files_to_read/ef_author.xml')