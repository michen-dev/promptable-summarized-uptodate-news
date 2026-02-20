import hashlib


def hash_url(url):
    return hashlib.sha256(url.encode("utf-8")).hexdigest()