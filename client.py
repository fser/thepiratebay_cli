#!/usr/bin/env python

import sys, urllib2, prettytable, itertools
from BeautifulSoup import BeautifulSoup

DOMAIN = 'http://thepiratebay.se'
BASE_URL = DOMAIN + '/s/?q=%s'

def list_all_page_results(pattern):
    pages = [ BASE_URL % urllib2.quote(pattern) ]
    try:
        body = urllib2.urlopen(pages[0]).read()
    except urllib2.HTTPError as e:
        print "blaaaa %s" % e
    soup = BeautifulSoup(body)
    nexts = soup.find('div', {'align': 'center'})
    
    for itm in nexts.findAll('a'):
        try:
            int(itm.text)
            pages.append ( DOMAIN + '/' + urllib2.quote(itm.get('href')) )
        except ValueError:
            break
    return pages

def list_items(url):
    results = []
    body = ''
    try:
        resp = urllib2.urlopen(url) # (BASE_URL % pattern)
        body = resp.read()
    except urllib2.HTTPError as e:
        print "Error in list_items getting %s" % e.geturl()
    soup = BeautifulSoup(body)

    searchResult = soup.find("div", {"id": "SearchResults"})

    if searchResult is None:
        return results
    
    for line in searchResult.findAll('tr')[1:]:
#        if line.tr['class'] == 'header':
#           continue

        magnet = None
        desc = None
        link = None

        (garbage,desc,se,le) = line.findAll('td')

        for a in desc.findAll('a'):
            if a.get('href').startswith('magnet'):
                magnet = a.get('href')
                break
        
        ddiv = desc.find('div', {'class': 'detName'})
        desc = ddiv.getText()
        link = ddiv.find('a', {'class': 'detLink'}).get('href')
        item = {'se': int(se.getText()),
                'le': int(le.getText()),
                'desc': desc,
                'magnet': magnet,
                'link': link,
                }
        results.append(item)

    return results

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print "Usage: %s <<pattern>>" % sys.argv[0]
    else:
        pattern = ' '.join(sys.argv[1:])
        pages = list_all_page_results(pattern)
        results = []
        for page in pages:
            results += list_items(page)

        if len(results) == 0:
            print "No match found"
        else:
            print "%d match found." % len(results)
            t = prettytable.PrettyTable(["id", "desc", "se", "le"])
            for (idx,result) in enumerate(results):
                t.add_row([idx, result['desc'], result['se'], result['le']]) # , result['link'], result['magnet']])
            print t

            ep = raw_input('which ID(s) (separated by spaces)? ')
            for sep in ep.split(" "):
                print results[int(sep)]['magnet']
        
