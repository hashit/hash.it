import os
from urlparse import urlparse

class HashValue(object):
    def __init__(self, path):
        import hashlib
        self.path = path
        self.md5 = hashlib.md5()
        self.sha256 = hashlib.sha256() 
        self.sha512 = hashlib.sha512()
        self.compute_hashes()

    def compute_hashes(self):
        blk = 2**20
        with open(self.path) as f:
            while True:
                data = f.read(blk)
                if not data:
                    break
                self.md5.update(data)
                self.sha256.update(data)
                self.sha512.update(data)

class HashFile(object):
    def __init__(self, url):
        import hashlib
        self.url = url
        self.parsed_url = urlparse(url)
        self.filename = os.path.basename(self.parsed_url.path)
        self.filename_digest = hashlib.sha256(self.filename).hexdigest()

class Hasher(object):
    def __init__(self, hash_db=None):
        self.file_value = None
    
    def verify(self, path):
        self.file_value = ''
    
    def add_to_db(self):
        pass
