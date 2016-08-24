from app import app

import requests, re, datetime
from bs4 import BeautifulSoup

PROVIDER = "http://spaceflight.nasa.gov/realdata/sightings/SSapplications/Post/JavaSSOP/orbit/ISS/SVPOST.html"

def run():
    result = tryProvider();
    print(result);

def tryProvider():
    try:
        r = requests.get(PROVIDER, stream = True)
        if r.status_code == 200:
            html = r.text
            result = parse(html)
            return result
        else:
            return 0
    except requests.exceptions.RequestException as e:
        return 0

def parse(html):
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text()
    if len(text) > 0:
        result = retriveTleMain(text)
        return result

def retriveTleMain(text):
    regexp = "TWO LINE MEAN ELEMENT SET\s*ISS\s*(.*?)\s*Satellite: ISS"
    alldata = re.findall(regexp, text, re.DOTALL)
    result = []
    for i in range(0,len(alldata)-1):
        alldata[i] = re.sub("\n\s*", "\n", alldata[i])
        alldata[i] = re.sub(" +", ' ', alldata[i])
        result.append([getTimestamp(alldata[i]), alldata[i]])
    return result

def getTimestamp(tle):
    fields = tle.rsplit(' ')
    if (len(fields) > 0):
        if (fields[0] == '1'):
            return epochToTimestamp(fields[3])

def epochToTimestamp(epoch):
    year = "20" + epoch[:2]
    day = epoch[2:]
    date = datetime.datetime(int(year),1,1) + datetime.timedelta(float(day))
    return int(date.timestamp())
