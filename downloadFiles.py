import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

import urllib, http.cookiejar

opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
# then for all requests
postData = ""
if postData:
    pData =  urllib.parse.urlencode(postData)
else:
    pData = None

httpReq = urllib.request.Request("https://userscloud.com/2rdteo81ocgs", pData)
page =  opener.open(httpReq)
strPage = page.read()
strPage = strPage.decode()
print(strPage)
with open("out.html", 'a') as out:
    out.write(strPage + '\n')

posRan = strPage.find("\"rand\"")
print(posRan)

#import requests
#url_0 = "http://dailyuploads.net/030p4rn9ll6a"
#url = "https://webapp.pucrs.br/consulta/servlet/consulta.aluno.ValidaAluno"
#data = {"pr1": "123456789", "pr2": "1234"}

#s = requests.session()
#r = s.get(url_0)

#print(r)