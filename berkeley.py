__author__ = 'robin.tanner'
from nytimesarticle import articleAPI
import requests
from urllib import request
from pprint import pprint
import json
import requests
import datetime
import logging
import argparse
import sys
#api = articleAPI('11570be9bf6f23e37211b7fd38939195:18:72364286')
#articles = api.search(q = 'Obama')
def getArticles(sdate, edate, api_key):
     for date in daterange(sdate, edate):
          art_url = "http://api.nytimes.com/svc/search/v2/articlesearch.json?begin_date=" + date.strftime("%Y%m%d") + "&end_date=" + date.strftime("%Y%m%d") + "&api-key=" + api_key
          articles = requests.get(art_url).json()
          request_string = "http://api.nytimes.com/svc/search/v2/articlesearch.json?begin_date=" + sdate.strftime("%Y%m%d") + "&end_date=" + date.strftime("%Y%m%d") + "&api-key=" + api_key
          print(request_string)
          jsonview = requests.get(request_string)
          articles = jsonview.json()['response']['docs']
          print(articles)
          for article in articles:
               print("published: ", article['pub_date'], article['snippet'])

          #print (json.dumps(jsonview.json()))


# helper function to iterate through dates
def daterange( start_date, end_date ):
    if start_date <= end_date:
        for n in range( ( end_date - start_date ).days + 1 ):
            yield start_date + datetime.timedelta( n )
    else:
        for n in range( ( start_date - end_date ).days + 1 ):
            yield start_date - datetime.timedelta( n )

def Main():
    #searchtype = input("Please enter a search type:")
    nytfin_url = "http://api.nytimes.com/svc/elections/us/v3/finances/"
    art_key = "836afc9bbe86ee8c2a1236478f332bc4:11:72364286"
    nytfin_key = "&api-key=11570be9bf6f23e37211b7fd38939195:18:72364286"
    nytfin_cycle = "2008"
    nytfin_lname_query = "obama"
    nytfin_candidates_search_partial = "/candidates/search"

    response_format = ".json"
    query = "?query="
    callback = "&callback=JSONP"
    start = datetime.date(year = 2013, month = 1, day = 1)
    end = datetime.date(year = 2013, month = 1, day = 1)
    getArticles(start, end, art_key)

Main()