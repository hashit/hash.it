import os
from os.path import join as pj
from urlparse import urlparse

class Downloader(object):
    def __init__(self, url, dst=None):
        self.url = url
        self.parsed_url = urlparse(url)
        if not dst:
            dst = pj(os.getcwd(), os.path.basename(self.parsed_url.path))
        self.dst = dst
        self.hasher = Hasher()

    def download(self):
        pass

    def download_and_verify(self):
        self.download()
        self.hasher.verify_hash(self.dst)
