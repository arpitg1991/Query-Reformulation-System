# -*- coding: utf-8 -*-
import urllib
import urllib2
import base64
import json
import sys

def main():
    query = raw_input('Please enter the query you want to search for : ')
    query = query.replace(" ",'+')
    targetPrec = raw_input('Please enter the precision(@10) you want to search with (0-1) : ')
    bing_search(query, targetPrec)

def bing_search(query,targetPrec):
    bingUrl = 'https://api.datamarket.azure.com/Bing/Search/Web?Query=%27' + query + '%27&$top=10&$format=json'
    print bingUrl
    #Provide your account key here
    accountKey = 'JsV9AIVwzY0l654YiaIXAppMcpvpm7lvkcYdmzJrNcs'

    accountKeyEnc = base64.b64encode(accountKey + ':' + accountKey)
    headers = {'Authorization': 'Basic ' + accountKeyEnc}
    req = urllib2.Request(bingUrl, headers = headers)
    response = urllib2.urlopen(req)
    content = response.read()
    print content
    #content contains the json response from Bing. 
    json_result = json.loads(content)
    result_list = json_result['d']['results']
    print getRelevantFB(query, result_list,targetPrec)

def getRelevantFB(query, result_list, targetPrec):
    userPrec = 0.0;
    relevant = []
    for result in result_list:
        desc = result[u'Description'].encode("iso-8859-15", "replace")
        title = result[u'Title'].encode("iso-8859-15", "replace")
        url = result[u'Url'].encode("iso-8859-15", "replace")
        print '\nTitle: ' + title + '\n' + 'Url: ' + url + '\n' + 'Desc: ' + desc
        isRel = raw_input('Is this link relevant to your search or not (y or n)?: ')
        if isRel == 'y' or isRel=='Y':
            userPrec = userPrec+1

    print userPrec
    userPrec = userPrec/10
    print userPrec
    # If targetPrecision is achieved
    if userPrec == 0 or userPrec >= targetPrec:
        sys.exit()
    else:
        keyWordEngine(query,targetPrec)


def keyWordEngine(query,targetPrec):
    print 'Finding new key words'
    print 'Determining new key words'
    print 'Updated the query' + query
    bing_search(query,targetPrec)

if __name__ == "__main__":
    main()
