# COPYRIGHT @ 2021 Simon, Sagstetter
import requests, os, json, sys
from tqdm import tqdm
from settings import Configuration, SfError

ROOT=os.path.dirname(os.path.abspath(__file__))

def loadConfig():
    try:
        with open(ROOT + "\config.json") as config:
            c = json.load(config)
            config.close()
    except:
            print("Unexpected error:", sys.exc_info()[0])
            raise

    return Configuration(c["username"],c["password"],
                           c["security_token"], c["auth_url"]
                           ,c["org_url"])

def login(CONFIG):
    headers = {
        "Content-Type" : "text/xml",
        "SOAPAction" : "login"
    }

    data = """<?xml version="1.0" encoding="utf-8" ?>
    <env:Envelope xmlns:xsd="http://www.w3.org/2001/XMLSchema"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xmlns:env="http://schemas.xmlsoap.org/soap/envelope/">
      <env:Body>
        <n1:login xmlns:n1="urn:partner.soap.sforce.com">
          <n1:username>""" + CONFIG.USERNAME +"""</n1:username>
          <n1:password>""" + CONFIG.PASSWORD + CONFIG.SECURITY_TOKEN + """</n1:password>
        </n1:login>
      </env:Body>
    </env:Envelope>"""
    r = requests.post(CONFIG.AUTH_URL, data=data, headers=headers)
    if r.status_code == 200:
        return r
    else:
        raise SfError(r.reason, r.text)

def headers(RESULT):
    return {
        'Cookie': "oid=" + RESULT.org_id() + "; sid=" + RESULT.session_id(),
        'X-SFDC-Session': RESULT.session_id()
    }

def getFileLink(RESULT, CONFIG):
    REQ_URL=CONFIG.ORG_URL + "/servlet/servlet.OrgExport"
    h = headers(RESULT)
    r = requests.get(REQ_URL, headers=h)
    if r.status_code == 200:
        if r.text is None:
            raise SfError('No File Found', 'Export Data Not Available')
        else:
            return r.text
    else:
        raise SfError(r.reason, r.status_code)

def downloadFile(LINK, RESULT, CONFIG):
    REQ_URL = CONFIG.ORG_URL + LINK
    fileName = LINK[(LINK.find('fileName') +9):(LINK.find('&'))]
    Location = ROOT + "\\downloads\\" + fileName
    h = headers(RESULT)
    try:
        with requests.get(REQ_URL.strip(), headers=h, stream=True) as r:
            totalSize = int(r.headers.get('Content-Length', 0))
            progress = tqdm(total=totalSize, unit='iB', unit_scale=True)
            r.raise_for_status()
            with open(Location, 'wb') as archive:
                for chunk in r.iter_content(chunk_size=1024):
                    progress.update(len(chunk))
                    archive.write(chunk)
            progress.close()
        archive.close()
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
    return Location
