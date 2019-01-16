import xml.etree.ElementTree as ET
import sys
import os

os.chdir('xml/')
with open("../stat.tsv","w") as f:
    for t in os.listdir(os.getcwd()):
        tree = ET.parse(t)
        root = tree.getroot()
        for elem in root.findall("./{http://www.tei-c.org/ns/1.0}teiHeader/{http://www.tei-c.org/ns/1.0}fileDesc/{http://www.tei-c.org/ns/1.0}sourceDesc/{http://www.tei-c.org/ns/1.0}biblFull/{http://www.tei-c.org/ns/1.0}publicationStmt/{http://www.tei-c.org/ns/1.0}date/[@type='publication']"):
            f.write(elem.text)
            f.write('\t')
        for elem in root.findall("./{http://www.tei-c.org/ns/1.0}teiHeader/{http://www.tei-c.org/ns/1.0}fileDesc/{http://www.tei-c.org/ns/1.0}sourceDesc/{http://www.tei-c.org/ns/1.0}biblFull/{http://www.tei-c.org/ns/1.0}publicationStmt/{http://www.tei-c.org/ns/1.0}volume"):
            f.write(elem.text)
            f.write('\t')
        for elem in root.findall("./{http://www.tei-c.org/ns/1.0}teiHeader/{http://www.tei-c.org/ns/1.0}fileDesc/{http://www.tei-c.org/ns/1.0}sourceDesc/{http://www.tei-c.org/ns/1.0}msDesc/{http://www.tei-c.org/ns/1.0}msIdentifier/{http://www.tei-c.org/ns/1.0}repository"):
            f.write(elem.text)
            f.write('\t')
        for elem in root.findall("./{http://www.tei-c.org/ns/1.0}teiHeader/{http://www.tei-c.org/ns/1.0}fileDesc/{http://www.tei-c.org/ns/1.0}sourceDesc/{http://www.tei-c.org/ns/1.0}msDesc/{http://www.tei-c.org/ns/1.0}msIdentifier/{http://www.tei-c.org/ns/1.0}idno/{http://www.tei-c.org/ns/1.0}idno/[@type='URLCatalogue']"):
            f.write(elem.text)
            f.write('\t')
        for elem in root.findall("./{http://www.tei-c.org/ns/1.0}teiHeader/{http://www.tei-c.org/ns/1.0}fileDesc/{http://www.tei-c.org/ns/1.0}publicationStmt/{http://www.tei-c.org/ns/1.0}idno/{http://www.tei-c.org/ns/1.0}idno/[@type='DirName']"):
            f.write(elem.text)
            f.write('\t')
        for elem in root.findall("./{http://www.tei-c.org/ns/1.0}teiHeader/{http://www.tei-c.org/ns/1.0}fileDesc/{http://www.tei-c.org/ns/1.0}publicationStmt/{http://www.tei-c.org/ns/1.0}idno/{http://www.tei-c.org/ns/1.0}idno/[@type='URLWeb']"):
            f.write(elem.text)
            f.write('\t')
        for elem in root.findall("./{http://www.tei-c.org/ns/1.0}teiHeader/{http://www.tei-c.org/ns/1.0}fileDesc/{http://www.tei-c.org/ns/1.0}extent/{http://www.tei-c.org/ns/1.0}measure/[@type='images']"):
            f.write(elem.text)
            f.write('\t')
        for elem in root.findall("./{http://www.tei-c.org/ns/1.0}teiHeader/{http://www.tei-c.org/ns/1.0}fileDesc/{http://www.tei-c.org/ns/1.0}extent/{http://www.tei-c.org/ns/1.0}measure/[@type='tokens']"):
            f.write(elem.text)
            f.write('\n')