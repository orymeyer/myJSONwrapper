import requests,json


def getJSON(url):
    url = 'https://api.myjson.com/bins/1dcvl'
    r = requests.get(url)
    #print(r.json()["url"])
    return r.json()


def postJSON(data):
    url = 'https://api.myjson.com/bins'
    #data={"some":"data"}
    headers={'content-type':'application/json'}
    r = requests.post(url,data=json.dumps(data),headers=headers) 
    return r.content()

