from urllib2 import urlopen 
from json import load 

url = "http://api.npr.org/query?apiKey="
key = "API_KEY"
numresults = "&numResults=3"
format = "&format=json"
id = "&id="
npr_id = raw_input("Which NPR ID do you want to query?")
url = ''.join([url, key, numresults, format, id, npr_id])
print(url)
response = urlopen(url)
json_obj=load(response)



for story in json_obj['list']['story']:
    print(story['title']['$text'])

