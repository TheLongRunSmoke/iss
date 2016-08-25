from app import app
import TleCrawler

def run():
    crawler = TleCrawler()
    if crawler.status == 0:
        data = crawler.getData()
    else:
        print("send mail")# TODO: send email - provider not response
