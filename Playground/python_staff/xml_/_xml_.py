from xml.dom.minidom import parse, Node
import xml.sax.handler


class BookHandler(xml.sax.handler.ContentHandler):

    def __init__(self):
        super().__init__()
        self.inTitle = False

    def startElement(self, name: str, attributes: str):
        if name == "title":
            self.inTitle = True

    def characters(self, content: str):
        if self.inTitle:
            print(content)

    def endElement(self, name: str):
        if name == "title":
            self.inTitle = False


if __name__ == "__main__":
    xml_tree = parse("books.xml")
    for node1 in xml_tree.getElementsByTagName("title"):
        for node2 in node1.childNodes:
            if node2.nodeType == Node.TEXT_NODE:
                print(node2.data)
    print("-" * 20)
    parser = xml.sax.make_parser()
    handler = BookHandler()
    parser.setContentHandler(handler)
    parser.parse("books.xml")

    print("-" * 20)

    from xml.etree.ElementTree import parse

    tree = parse("books.xml")
    for E in tree.findall("title"):
        print(E.text)
