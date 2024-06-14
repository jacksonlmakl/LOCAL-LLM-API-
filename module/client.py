import requests

class LLMApiClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def prompt(self, prompt):
        url = f"{self.base_url}/predict"
        response = requests.post(url, json={'prompt': prompt})
        response.raise_for_status()
        data = response.json()
        return data['response']

