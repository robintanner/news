__author__ = 'robin.tanner'

from urllib import request
from pprint import pprint
import json
import requests
import datetime
import logging
import argparse
import sys


def getArticles(date, api_key, json_file_path, searchtype):
    if searchtype == 'candidate':
        nytfin_url_complete = ''.join([nytfin_url, nytfin_cycle, nytfin_candidates_search_partial, response_format, query, nytfin_lname_query, nytfin_key])
        response=request.urlopen(nytfin_url_complete)
        print(response.read().decode('utf-8'))
        resp=response.read().decode('utf-8')
        json_obj = requests.get(nytfin_url_complete, headers=headers).json()
        for candidate in json_obj['results']:
            print(candidate['candidate']['name'])
    elif searchtype == "articles":
        for page in range(101):
            #art_url = "http://api.nytimes.com/svc/search/v2/articlesearch.json?begin_date=" + date
            art_url = "http://api.nytimes.com/svc/search/v2/articlesearch.json?begin_date=" + date + "&end_date=" + date + "&page=" + str(page) + "&api-key=" + api_key
            articles = requests.get(art_url).json()

            if len(articles['response']['docs']) >= 1:
                json_file_name = getJsonFileName(date, page, json_file_path)
                json_file = open(json_file_name, 'w')
                json_file.write(articles)
                json_file.close()
            else:
                return

    headers = {'Accept-Encoding': 'deflate'}






    print(article_response)

    for article in article_response['response']['docs']:
        print(article)
        print(article['keywords'])

# helpful function to figure out what to name individual JSON files
def getJsonFileName(date, page, json_file_path):
    json_file_name = ".".join([date,str(page),'json'])
    json_file_name = "".join([json_file_path,json_file_name])
    return json_file_name

# helper function to iterate through dates
def daterange( start_date, end_date ):
    if start_date <= end_date:
        for n in range( ( end_date - start_date ).days + 1 ):
            yield start_date + datetime.timedelta( n )
    else:
        for n in range( ( start_date - end_date ).days + 1 ):
            yield start_date - datetime.timedelta( n )


def Main():
    searchtype = input("Please enter a search type:")

    nytfin_url = "http://api.nytimes.com/svc/elections/us/v3/finances/"

    art_key = "836afc9bbe86ee8c2a1236478f332bc4:11:72364286"
    nytfin_key = "&api-key=11570be9bf6f23e37211b7fd38939195:18:72364286"
    nytfin_cycle = "2008"
    nytfin_lname_query = "obama"
    nytfin_candidates_search_partial = "/candidates/search"

    parser = argparse.ArgumentParser(description="A Python tool for grabbing data from the NY Times API")
    parser.add_argument('-j', '--json', required=True, help="path to the folder where you want JSON files stored")
    args = parser.parse_args()

    json_file_path = args.json

    log_file = "".join([json_file_path,"getTimesArticles_testing.log"])
    logging.basicConfig(filename=log_file, level=logging.INFO)
    logging.info("Getting started.")


    response_format = ".json"
    query = "?query="
    callback = "&callback=JSONP"

    start = datetime.date(year = 2013, month = 1, day = 1)
    end = datetime.date(year = 2013, month = 1, day = 1)

    try:
        for date in daterange(start, end):
            date = date.strftime("%Y%m%d")
            logging.info("working on %s" % date)
            getArticles(date, art_key, json_file_path, searchtype)





#print(article_response)

#pprint(project_info)

#print(nytfin_url_complete)

#json_obj = json.load(response.read().decode('utf-8'))

#print(json_obj)

#for story in :
 #   print(story)

#print(nytfin_url_complete)


