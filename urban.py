import json
from urllib.parse import quote
import urllib.request
def getDef(word):
    url = "https://api.urbandictionary.com/v0/define?term="+quote(word)
    resp = urllib.request.urlopen(url)
    resp = json.loads(resp.read().decode('utf-8'))
    list = resp["list"]
    words = []
    for word in list:
        worddict = {
            "word":word["word"],
            "definition":word["definition"],
            "permalink":word["permalink"],
            "thumbs_up":word["thumbs_up"],
            "thumbs_down":word["thumbs_down"],
            "example":word["example"],
            "written_on":word["written_on"],
            "author":word["author"],
            "definition_id":word["defid"]
        }
        words.append(worddict)
    return words
