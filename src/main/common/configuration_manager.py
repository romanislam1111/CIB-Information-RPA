from xml.dom import minidom

class   ConfigurationManager():

    def __init__(self, xml_file_dir='App.xml'):
        self.xmldoc = minidom.parse(xml_file_dir)

    def get_data(self, tag_name):
       
        return self.xmldoc.getElementsByTagName(tag_name)[0].childNodes[0].data
     
