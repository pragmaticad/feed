# %%
import xmltodict
import pandas as pd
from sqlalchemy import create_engine
import sqlalchemy
import datetime
import urllib3
import os
import sys 
import requests
import re
import base64
UTM = 'ff.prospecting.productfeed.subnetwork.adtraction'
# %%
df = pd.read_csv('https://transport.productsup.io/ef17cd31fd40bf3deb77/channel/444455/PragmaticAd_affiliate.csv',sep='|', header=0)
df['ads_redirect'].replace(r'wt_mc=[^&]*&', 'wt_mc=' + UTM + '&', inplace=True, regex=True)
# df['price'] = df['price'].apply(lambda x: str(round(float(x),2)) + ' PLN')
# df['sale_price'] = df['sale_price'].apply(lambda x: str(round(float(x),2)) + ' PLN')
c = df.to_xml(root_name='rss', row_name='item', namespaces = {"g": "http://base.google.com/ns/1.0"}, prefix='g', index=False)
c = c.replace('g:rss', 'rss')
c = c.replace('g:item', 'item')
c = c[:83] + ' version="2.0"' + c[83:85] + '  <channel>\n    <title>Pragmatic RSS Product Feed</title>\n<link>https://www.pragmaticad.com/</link>\n<description>Dedicated</description>\n' + c[85:-6] +  '  </channel>\n' + c[-6:]
c = c.replace('&amp;', '&')
with open("obi_parsed.xml", "w", encoding="utf8") as xml_file:
    xml_file.write(c)
# %%
# f = 'obi_parsed.xml'

# user='user'
# password='XJrBeiwBfDq9'
# # password='2Kj6bM8SqIr3'
# # password = 'T4cq AlTW zypu Yt0u 4HIi 61ie'
# url1='http://3.66.189.224/wp-login.php'
# redirecturl='http://3.66.189.224/wp-admin/media-new.php'
# url2='http://3.66.189.224/wp-admin/async-upload.php'

# headerauth= {
#         'Cookie':'wordpress_test_cookie=WP Cookie check; ROUTEID=.1',
#         'Host':'3.66.189.224',
#         'Content-Type': 'application/x-www-form-urlencoded'
#         }
# dataauth = {
#         'log':user,
#         'pwd':password,
#         'wp-submit':'Log In',
#         'redirect_to': redirecturl,
#         'testcookie': 1
#         }
# image = {'async-upload':(f, open(f, "rb"))}
# testimage = open(f, "rb")

# session1=requests.Session()
# # session1.max_redirects = 1000
# session1.get(url1)
# r1 = session1.post(url1, headers=headerauth, data=dataauth, allow_redirects=True)

# test = re.search('"multipart_params":.*_wpnonce":"[0-9a-z]+"', r1.text)
# nonce = re.search('(?<=_wpnonce":")[0-9a-z]{10}', test.group(0))
# nonce = nonce.group(0)

# uploadheaders = {
#         'Connection': 'keep-alive',
#         'Referer': 'http://3.66.189.224/wp-admin/upload.php',
#         'Sec-Fetch-Dest': 'empty',
#         'Sec-Fetch-Mode': 'cors',
#         'Sec-Fetch-Site': 'same-origin'
#         }
# dataupload = {
#         'name': f,
#         'action': 'upload-attachement',
#         '_wpnonce': nonce,
#         'wpmf_folder': '0',
#         }

# r2 = session1.post(url2, data=dataupload, headers=uploadheaders, files=image)
# # %%
# resp = requests.get('http://3.66.189.224/wp-json/wp/v2/media?search=obi_parsed').json()
# for el in resp:
#     print(el['id'])
# # %%
# credentials = user + ':' + password
# token = base64.b64encode(credentials.encode())
# header = {'Authorization': 'Basic ' + token.decode('utf-8')}
# resp = requests.delete('http://3.66.189.224/wp-json/wp/v2/media/10658?force=true', headers=header)
# # %%
# resp.history
# %%
