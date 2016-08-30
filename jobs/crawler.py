import requests, re, datetime
from bs4 import BeautifulSoup


class TleCrawler:
    """
    Obtain TLE data from NASA.
    """

    PROVIDER = "http://spaceflight.nasa.gov/realdata/sightings/SSapplications/Post/JavaSSOP/orbit/ISS/SVPOST.html"

    status = 0
    html = ""
    data = []

    def __init__(self):
        """
        Try to download page. If success - initialize field data.
        """
        try:
            r = requests.get(self.PROVIDER, stream=True)
            if r.status_code == 200:
                self.html = r.text
            else:
                self.status = 1
        except requests.exceptions.RequestException:
            self.status = 1

    def get_data(self):
        """
        "Public" method. Return ready data list.
        :return: list with TLE.
        """
        if len(self.html) > 0:
            return self.parse(self.html)

    def parse(self, html):
        """
        Remove all HTML tags from downloaded data.
        :param html: downloaded data.
        :return: list of TLE.
        """
        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text()
        if len(text) > 0:
            result = self.retrieve_tle_main(text)
            return result

    def retrieve_tle_main(self, text):
        """
        Find all useful data.
        :param text: sanitized downloaded data.
        :return: list of TLE
        """
        regexp = "TWO LINE MEAN ELEMENT SET\s*ISS\s*(.*?)\s*Satellite: ISS"
        alldata = re.findall(regexp, text, re.DOTALL)
        result = []
        for i in range(0,len(alldata)-1):
            alldata[i] = re.sub("\n\s*", "\n", alldata[i])
            alldata[i] = re.sub(" +", ' ', alldata[i])
            result.append([self.get_timestamp(alldata[i]), alldata[i]])
        return result

    def get_timestamp(self, tle):
        """
        Obtain UTC+0 timestamp for epoch mean in TLE.
        :param tle: formatted TLE string.
        :return: unix timestamp.
        """
        fields = tle.rsplit(' ')
        if len(fields) > 0:
            if fields[0] == '1':
                return self.epoch_to_timestamp(fields[3])

    @staticmethod
    def epoch_to_timestamp(epoch):
        """
        Convert TLE epoch in unix timestamp with zero timezone.

        TLE epoch format:

        16237.246584
        ||||| ||||||
        first two, it's last two digit of year.
          ||| ||||||
          next three, is day in year.
              ||||||
              after decimeter, time of day as fraction.

        :param epoch: TLE epoch
        :return: unix timestamp
        """
        year = "20" + epoch[:2]
        day = epoch[2:]
        date = datetime.datetime(int(year), 1, 1, tzinfo=datetime.timezone.utc) + datetime.timedelta(float(day))
        return int(date.timestamp())
