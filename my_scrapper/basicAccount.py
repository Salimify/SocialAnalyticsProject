from bs4 import BeautifulSoup
import urllib2
import pandas as pd
import requests
# get source code of the page
def get_url(url):
    return urllib2.urlopen(url).read()

# makes the source tree format like 
def beautify(url):
    source = get_url(url)
    return BeautifulSoup(source,"html.parser")

def login(s):
    USERNAME = "salimism@outlook.com"
    PASSWORD = "123ak123"

    r = s.get('https://www.linkedin.com/uas/login')  
       
    soup = BeautifulSoup(r.text, "lxml")  
    soup = soup.find(id="login")       
  
    loginCsrfParam = soup.find('input', id = 'loginCsrfParam-login')['value']  
    csrfToken = soup.find('input', id = 'csrfToken-login')['value']  
    sourceAlias = soup.find('input', id = 'sourceAlias-login')['value']  
    isJsEnabled = soup.find('input',attrs={"name" :'isJsEnabled'})['value']  
    source_app = soup.find('input', attrs={"name" :'source_app'})['value']  
    tryCount = soup.find('input', id = 'tryCount')['value']  
    clickedSuggestion = soup.find('input', id = 'clickedSuggestion')['value']  
    signin = soup.find('input', attrs={"name" :'signin'})['value']  
    session_redirect = soup.find('input', attrs={"name" :'session_redirect'})['value']  
    trk = soup.find('input', attrs={"name" :'trk'})['value']  
    fromEmail = soup.find('input', attrs={"name" :'fromEmail'})['value']  
   
    payload = {  
        'isJsEnabled':isJsEnabled,  
        'source_app':source_app,  
        'tryCount':tryCount,  
        'clickedSuggestion':clickedSuggestion,  
        'session_key':USERNAME,  
        'session_password':PASSWORD,  
        'signin':signin,  
        'session_redirect':session_redirect,  
        'trk':trk,  
        'loginCsrfParam':loginCsrfParam,  
        'fromEmail':fromEmail,  
        'csrfToken':csrfToken,  
        'sourceAlias':sourceAlias  
    }  
  
    s.post('https://www.linkedin.com/uas/login-submit', data=payload)  
    return s  

links = []

s = requests.session()  
s = login(s)
#loop over all pages to get the posting details
for i in range(50): #range(n_pages)   
    # define the base url for generic searching 
    url = ("https://www.linkedin.com/search/results/people/v2/?facetGeoRegion=%5B%22tn%3A0%22%5D&facetNetwork=%5B%22S%22%2C%22O%22%5D&origin=FACETED_SEARCH&page=nPostings")
    url = url.replace('nPostings',str(10*i))
    soup = beautify(url)
    # Build lists for each type of information
    results = soup.find_all('html')
    print(results)
    results.sort()
    # print "there are ", len(results) , " results"
    with open('your_file.txt', 'w') as f2:
        for res in results:
            # set only the value if get_text() 
            r = res.find('a',{'class' : 'search-result__result-link'}).get('href')
            links.append(r)
            f2.write("%s\n" % r)
            f2.write("%s\n" % "")