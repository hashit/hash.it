# In here we shall test the hash related functions.

filename = 'tor-browser-gnu-linux-x86_64-2.3.25-13-dev-ar.tar.gz'
test_url = 'https://www.torproject.org/dist/torbrowser/linux/' + filename
def test_hash_file():
    from hashit.hashes import Hasher, HashFile, HashValue
    hf = HashFile(test_url)
    assert hf.filename == filename
    assert hf.filename_digest == 'bf3ee626c6761c0760386211f10c4a102f9c2f705ff9f57d4bd7ca4da048e350'
