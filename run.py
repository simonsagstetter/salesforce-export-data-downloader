# COPYRIGHT @ 2022 Simon, Sagstetter
from main import (
loadConfig,
login,
headers,
getFileLink,
downloadFile
)

from settings import (
Result
)

from sendmail import (
send_mail
)

print('#### Starting Salesforce Export Data Downloader ####')
CONFIG = loadConfig()
print('Configuration loaded...')
RESP = login(CONFIG)
print('Login successfull...')
RESULT = Result(RESP.text)
LINK = getFileLink(RESULT, CONFIG)
print('Init download...')
print('Please wait...')
FILE = downloadFile(LINK, RESULT, CONFIG)
print('Download Completed!')
print('Your file is located: ' + FILE)
send_mail(CONFIG)
