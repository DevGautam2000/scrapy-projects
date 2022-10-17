"""
        AUTHOR: GAUTAM CHANDRA SAHA
        DATE & TIME: 16/10/22 AT 4:02 PM ON Sun
"""

from scrapy import cmdline


def main(user,passw):
    cmdline.execute(f"scrapy crawl login -a username={user} -a password={passw}".split())


if __name__ == '__main__':
    main("201900099","000992019")
