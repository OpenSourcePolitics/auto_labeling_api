from utils.config import cache
from transformers import pipeline


def from_pipeline(pipeline_name, model):
    cached_pipeline = cache.get(pipeline_name)
    if cached_pipeline is None:
        print("Pipeline not found in cache: " + pipeline_name)
        cached_pipeline = pipeline(pipeline_name, model=model)
        cache.set(pipeline_name, cached_pipeline)
    else:
        print("Pipeline found in cache: " + pipeline_name)
    return cached_pipeline
