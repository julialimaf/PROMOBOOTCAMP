from django.core.cache import cache 
import json 


def set_cache(key, value, timeout=300):
    cache.set(key, json.dumps(value), timeout) 

def get_cache(key):
    value = cache.get(key)
    if value:
        return json.loads(value)
    return None

def delete_cache(key):
    cache.delete(key)
