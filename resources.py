import json
from transformers import pipeline

configs = json.loads(open("pipelines_configuration.json").read())

for config in configs:
    pipeline(configs.get(config).get("pipeline_name"), model=configs.get(config).get("pipeline_model"))
