from bs4 import BeautifulSoup
import urllib
import urllib.request
from urllib.parse import urlparse
from urllib.parse import urljoin
from urllib.request import urlretrieve
from urllib.request import urlopen
from os import makedirs
import os.path, time, re
import subprocess
import socks, socket

import tor_checker

socks.set_default_proxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', 9050)
socket.socket = socks.socksocket

tor_checker.tor()

#type the target url
base_url = "your_target_url"

test_files = {}

def enum_links(html, base):
   soup = BeautifulSoup(html, "html.parser")
   links = soup.select("link[rel='stylesheet']")
   links += soup.select("a[href]")
   scripts= []
   imgs = []
   result = []
   scripts = soup.find_all("script")
   imgs = soup.find_all("img")
   
   
   for link in links:
      href = link.attrs['href']
      url = urljoin(base, href)
      result.append(url)
   
   for link in imgs:
      if not ( type(link) is str ):
         if link.get("src").endswith('.jpg'):
            imgs.append(link.get('src'))
            
         elif link.get('src').endswith('.svg'):
            imgs.append(link.get('src'))
            
         elif link.get('src').endswith('.png'):
            imgs.append(link.get('src'))
            
         elif link.get('src').endswith('.jpeg'):
            imgs.append(link.get('src'))
   
   for script in scripts:
      if not (type( link ) is str):
         if link.get('src').endswith('.js'):
            scripts.append(link.get('src'))

   #print(result)
   return (result, imgs, scripts)


def download_file(url):
   o = urlparse(url)
   savepath = "/var/www/html/site-data/" + o.netloc + o.path
   if re.search(r"/$", savepath):
      savepath += "index.html"
   savedir = os.path.dirname(savepath)

   if os.path.exists(savepath): return savepath

   if not os.path.exists(savedir):
      print("mkdir=", savedir)
      makedirs(savedir)
      
   try:
      print("download=", url)
      #urlretrieve(url, savepath)
      data = urlopen(url).read()
      
      with open( savepath, mode="mb" ) as f:
         f.write(data)
      
      time.sleep(1)
      return savepath
   except Exception as e:
      print("ダウンロード失敗:", url)
      print ("==========エラー内容==========")
      print ('type:' + str(type(e)) if e else "UNKNOWN" )
      print ('args:' + str(e.args) if e.args else "UNKNOWN" )
      print ('message:' + str(e.message) if e.message else "UNKNOWN" )
      print ('e_self:' + str(e) if e else "UNKNOWN")
      return None

def analize_html(url, root_url):
   savepath = download_file(url)
   if savepath is None: return
   if savepath in test_files: return
   test_files[savepath] = True
   print("analize_html=", url)

   html = open(savepath, "r", encoding="utf-8").read()
   links = enum_links(html, url)

   for link_url in links:
      if link_url.find(root_url) != 0:
         if not re.search(r".(css)$", link_url): continue

      if re.search(r".(html|htm)$", link_url):
         analize_html(link_url, root_url)
         continue
      download_file(link_url)
   
   

if __name__ == "__main__":
   url = f"{base_url}"
   analize_html(url, url)
   chmod_R777 = ['sudo', 'chmod', '-R', '777', './site-data']
   subprocess.call(chmod_R777)
   
   #img_url = f"{url}img/"
   #analize_html( url, url)
   #js_url = f"{url}js/"
   #analize_html(url, url)
