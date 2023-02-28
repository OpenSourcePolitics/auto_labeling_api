import json
from utils.config import cache


@cache.memoize()
def get_labels(type):
    return categories_config().get(type, [])


@cache.memoize()
def categories_config():
    return json.loads(open("classify_labels_configuration.json").read())
