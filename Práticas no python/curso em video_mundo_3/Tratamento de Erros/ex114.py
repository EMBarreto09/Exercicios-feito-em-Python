#Verificador de acesso ao site

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.youtube.com/')
except (urllib.error.URLError):
    print('Não temos acesso ao site')
else:
    print('Temos acesso ao site')