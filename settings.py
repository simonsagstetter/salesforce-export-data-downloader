# COPYRIGHT @ 2021 Simon, Sagstetter
import xml.etree.ElementTree as ET

class Configuration():
    def __init__(self, USERNAME, PASSWORD,
                SECURITY_TOKEN, AUTH_URL, ORG_URL,
                SENDER, RECEIVER):
        self.USERNAME=USERNAME
        self.PASSWORD=PASSWORD
        self.SECURITY_TOKEN=SECURITY_TOKEN
        self.AUTH_URL=AUTH_URL
        self.ORG_URL=ORG_URL
        self.SENDER=SENDER
        self.RECEIVER=RECEIVER

class Result():
    def __init__(self, XML_DOC):
        self.XML_DOC=XML_DOC

    def server_url(self):
        val = ''
        root = ET.fromstring(self.XML_DOC)
        for e in root.iter():
            if e.tag == '{urn:partner.soap.sforce.com}serverUrl':
                val = e.text

        return val

    def session_id(self):
        val = ''
        root = ET.fromstring(self.XML_DOC)
        for e in root.iter():
            if e.tag == '{urn:partner.soap.sforce.com}sessionId':
                val = e.text

        return val

    def org_id(self):
        val = ''
        root = ET.fromstring(self.XML_DOC)
        for e in root.iter():
            if e.tag == '{urn:partner.soap.sforce.com}organizationId':
                val = e.text

        return val

class SfError(Exception):
    def __init__(self, expression, message):
        self.expression=expression
        self.message=message
