from utils.config import cache
from transformers import pipeline
import json


def from_pipeline(pipeline_type):
    cached_pipeline = cache.get(pipeline_type)
    if cached_pipeline is None:
        print("Pipeline not found in cache: " + pipeline_type)
        config = pipeline_config(pipeline_type)
        cached_pipeline = pipeline(config.get("pipeline_name"), model=config.get("pipeline_model"))
        cache.set(pipeline_type, cached_pipeline)
    else:
        print("Pipeline found in cache: " + pipeline_type)
    return cached_pipeline


@cache.memoize()
def pipeline_config(pipeline_type):
    config = json.loads(open("pipelines_configuration.json").read())
    return config.get(pipeline_type)
