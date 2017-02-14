import http.client
import json

# Virker ikke lenger siden Twitter nå krever autentisering
# Se f.eks. python-twitter på github.

conn = http.client.HTTPConnection('search.twitter.com')
conn.request('GET', '/search.json?q=pluralsight')
resp = conn.getresponse()
data = resp.read()
data_string = str(data, 'utf-8')
obj = json.loads(data_string)
tweets = obj['results']
for tweet in tweets:
    print(tweet['text'])
