import os
import json
import requests


def translate(sequence, lang):
    if lang == "EN":
        return sequence
    else:
        return perform_translate(sequence, source_lang=lang, target_lang="EN")


def perform_translate(sequence, source_lang, target_lang):
    api_key = os.environ.get("DEEPL_API_KEY")
    if api_key == '' or api_key is None:
        raise Exception("DEEPL_API_KEY is not set")

    url = "https://api-free.deepl.com/v2/translate"

    payload = json.dumps({"source_lang": source_lang, "target_lang": target_lang, "text": [sequence]})

    headers = {'Authorization': api_key, 'Content-Type': 'application/json'}

    response = requests.request("POST", url, headers=headers, data=payload)
    print("Translation response", response.text, response.status_code)
    return json.loads(response.text)['translations'][0]['text']
