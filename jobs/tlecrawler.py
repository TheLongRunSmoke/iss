import requests, re, datetime
from bs4 import BeautifulSoup

class TleCrawler():
    """Obtaine TLE data from NASA."""

    PROVIDER = "http://spaceflight.nasa.gov/realdata/sightings/SSapplications/Post/JavaSSOP/orbit/ISS/SVPOST.html"

    status = 0
    html = ""
    data = []

    def __init__(self):
        try:
            r = requests.get(self.PROVIDER, stream = True)
            if r.status_code == 200:
                self.html = r.text
            else:
                self.status = 1
        except requests.exceptions.RequestException as e:
            self.status = 1

    def getData(self):
        if (len(self.html) > 0):
            return self.parse(self.html)

    def parse(self,html):
        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text()
        if len(text) > 0:
            result = self.retriveTleMain(text)
            return result

    def retriveTleMain(self,text):
        regexp = "TWO LINE MEAN ELEMENT SET\s*ISS\s*(.*?)\s*Satellite: ISS"
        alldata = re.findall(regexp, text, re.DOTALL)
        result = []
        for i in range(0,len(alldata)-1):
            alldata[i] = re.sub("\n\s*", "\n", alldata[i])
            alldata[i] = re.sub(" +", ' ', alldata[i])
            result.append([self.getTimestamp(alldata[i]), alldata[i]])
        return result

    def getTimestamp(self,tle):
        fields = tle.rsplit(' ')
        if (len(fields) > 0):
            if (fields[0] == '1'):
                return self.epochToTimestamp(fields[3])

    def epochToTimestamp(self,epoch):
        year = "20" + epoch[:2]
        day = epoch[2:]
        date = datetime.datetime(int(year),1,1,tzinfo=datetime.timezone.utc) + datetime.timedelta(float(day))
        return int(date.timestamp())
