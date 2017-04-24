from bs4 import BeautifulSoup
import requests
import sys
import re

# http://www.scimagojr.com/journalrank.php

url = "http://www.scimagojr.com/journalrank.php"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

def Scrape(year: int, subject: str, metric: str):
    # Function to scrape the data and input it to the dictionary



# Build method of pulling a random one (memoized dictionary?) from parameters assigned

# First build dictionary of all ??

### User Input
year = input('Please input a year (currently only 2015 is supported')
subjectarea = input('Please input a subject area. Leaving this blank will pull from all subjects randomly')
metrix = input('Please input a metric: SJR (s), total citations (t)')

# Have an area to randomize
# Can input Subject area (dropdown fill?)
# Include year (2015 down)

# Pull random (how to do this?)

# Round to the nearest 100th place

# Math calculations
# see whether it's close? Within 0.5 pt?
