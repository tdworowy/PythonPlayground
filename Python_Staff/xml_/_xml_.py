from  xml.dom.minidom import parse,Node

xmltree = parse('books.xml')
for node1 in xmltree.getElementsByTagName('title'):
    for node2 in node1.childNodes:
        if node2.nodeType == Node.TEXT_NODE:
            print(node2.data)



import xml.sax.handler

class BookHandler(xml.sax.handler.ContentHandler):

    def __init__(self):
        self.inTitle = False

    def startElement(self,name,attributes):
        if name == 'title':
            self.inTitle = True
    def characters(self, content):
        if self.inTitle:
            print(content)

    def endElement(self, name):
        if name == 'title':
            self.inTitle = False

print('-'*20)
parser = xml.sax.make_parser()
handler = BookHandler()
parser.setContentHandler(handler)
parser.parse('books.xml')

print('-'*20)

from xml.etree.ElementTree import parse
tree = parse('books.xml')
for E in tree.findall('title'):
    print(E.text)