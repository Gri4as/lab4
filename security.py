from pyCr
import hashlib as hash
import random

salt =

def road_to_hash(password):
    s256 = hash.sha256()
    s256.update(bytes(password, encoding='utf-8'))
    return s256.hexdigest()
