import urllib.request, urllib.error
from bs4 import BeautifulSoup

import socks, socket

socks.set_default_proxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', 9050)
socket.socket = socks.socksocket

def tor():
  # Returns HTML
  def fetch_html(url):
    res = urllib.request.urlopen(url)
    return BeautifulSoup(res, 'html.parser')

  # Returns Global IP address
  def get_ip_addr():
    html = fetch_html('http://checkip.dyndns.com/')
    return html.body.text.split(': ')[1]

  # Tor check
  def check_use_tor():
    html = fetch_html('https://check.torproject.org/')
    return html.find('h1')['class'][0] != 'off'

  print('You are using tor.' if check_use_tor() else 'You are not using tor.')
  print('Current IP address is ' + get_ip_addr())


if __name__ == "__main__":
  tor()