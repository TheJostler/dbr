#!/usr/bin/env python
 
# Please contact me by emailing: josj@tegosec.com
#
# LICENSE
# Copyright (c) 2024 Josjuar Lister

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import urllib3
import requests
import sys
import argparse
import webbrowser
import logz
import yaml
import random
import gzip
import pickle
from bs4 import BeautifulSoup
from datetime import datetime
from dateutil.parser import parse

# Including generic User-Agent http header to make us look like a browser
HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}



def process(html):
  ## Here we use Beautiful Soup to extract the parts we care about
  

  return text

# Fetch todays days text
def fetch(url, verbose):
    if verbose: print(f"Attempting to fetch [{url}]")
    # Here is where we package our parameters that we will send to our target, they are put into an array that will be passed to 'requests.get' as params
    payload = {}

    # We will wait 15 seconds for a response and try again, if we fail to get a response 3 times we skip that name and move on.
    try:
        r = requests.get(url, params=payload, headers=HEADERS, timeout=15)
    except:
        logz.info("Timed out, retrying")
        try:
            r = requests.get(url, params=payload, headers=HEADERS, timeout=15)
        except:
            logz.info("Timed out, twice, retrying")
            try:
                r = requests.get(url, params=payload, headers=HEADERS, timeout=15)
            except:
                logz.warn("Timed out, tree times, skipping")
                pass

    # Decode response from binary into UTF-8 charcters
    ret = r.content.decode('utf-8')

    # Use Beautiful Soup Module to parse html then find and extract all paragraph elements
    soup = BeautifulSoup(ret, "html.parser")
    
    return(process(soup))

# Initialize -- Start Here! Here is where we parse command line argyments.
if __name__ == "__main__":
  parser=argparse.ArgumentParser(
    description='''A new way of Reading the Bible Daily. This program randomly selects a verse from the Bible and downloads it. Some questions help with procesing the information in the verse and a goal is set.''',
    epilog="""Josjuar Lister 2024""")
  parser.add_argument('-v', '--verbose', help='Increase the verbosity', action='store_true')

  # To use arguments parsed here call 'args.<argument>'
  args=parser.parse_args()

  datadir = "/var/dbr"

  if os.path.exists(datadir):
    ##Do Stuff
    total_verses = 0
    with open("bibleStructure.yml") as f:
      bibleStruct = yaml.safe_load(f)
    for b, book in enumerate(bibleStruct):
       book_name = next(iter(book.keys()))
       print(f"Book No {b+1}, {book_name} has {len(book[book_name])} chapters and {sum(book[book_name])} verses")
       total_verses += sum(book[book_name])
    # First, randomly select a book
    books = len(bibleStruct)
    random_book_number = random.randint(1, len(bibleStruct))
    random_book = bibleStruct[random_book_number-1]
    book_name = next(iter(random_book.keys()))

    # Then randomly select a chapter from that book
    chapter_num = random.randint(1, len(random_book[book_name]))

    # Finally, randomly select a verse from that chapter
    verse_num = random.randint(1, random_book[book_name][chapter_num-1])

    print(f"Total verses catalogued: {total_verses}\n")
    print(f"Random verse: https://jw.org/finder?bible={random_book_number:02d}{chapter_num:03d}{verse_num:03d}")

    # First load your YAML
    with open("bibleStructure.yml") as f:
        bibleStruct = yaml.safe_load(f)

    # Save as pickle
    with open("bible.pkl", "wb") as f:
        pickle.dump(bibleStruct, f)

    # Save as compressed pickle
    with gzip.open("bible.pkl.gz", "wb") as f:
        pickle.dump(bibleStruct, f)

    # Compare sizes
    yaml_size = os.path.getsize("bibleStructure.yml")
    pickle_size = os.path.getsize("bible.pkl")
    gzip_size = os.path.getsize("bible.pkl.gz")

    print(f"YAML size: {yaml_size:,} bytes")
    print(f"Pickle size: {pickle_size:,} bytes")
    print(f"Gzipped pickle size: {gzip_size:,} bytes")
    print(f"\nPickle saves {((yaml_size - pickle_size) / yaml_size * 100):.1f}% space")
    print(f"Gzip saves {((yaml_size - gzip_size) / yaml_size * 100):.1f}% space")
  else:
      # Make the Cache directory
      if args.verbose: print(f"Creating Data directory at: {datadir}")
      try:
        os.mkdir(datadir)
      except PermissionError:
         logz.warn("Couldn't create the data directory at: {datadir} Permission Denied")
         logz.info("Try with sudo)")
      except:
        print(f"Couldn't create the data directory at: {datadir} Nothing was done")
        print("Try ")
