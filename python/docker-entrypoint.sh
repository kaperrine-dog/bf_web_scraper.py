#!/bin/sh
sudo service tor start
python3 scraper.py
tail -f /dev/null