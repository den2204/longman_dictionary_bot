from typing import List
from bs4 import BeautifulSoup
import requests

class LongmanAdapter:

    DICTONARY_URL = 'https://www.ldoceonline.com/dictionary/'
    HEADERS = {
        "User-agent": "*",
    }

    def get_definitions(self, words: List[str]) -> str:
        query = '-'.join(words)
        url = self.DICTONARY_URL + query
        definitions = "Definitions:\n"
        
        r = requests.get(url, headers=self.HEADERS)

        parsed = BeautifulSoup(r.text, "html.parser")
        for idx, obj in enumerate(parsed.find_all(class_="DEF")):
            definitions += f"{idx + 1}: {obj.get_text()}\n"

        return definitions