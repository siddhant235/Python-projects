import requests
from bs4 import BeautifulSoup
import pprint
res=requests.get("https://news.ycombinator.com/")
soup=BeautifulSoup(res.text,'html.parser')
links=soup.select('.storylink')
subtexts=soup.select('.subtext')
def sort_stories(hnlist):
    return sorted(hnlist,key=lambda k:k['votes'])

def create_custom_hn(links,subtexts):
    hn=[]
    for idx,item in enumerate(links):

        title=links[idx].getText()
        href=links[idx].get('href',None)   
        vote=subtexts[idx].select('.score')
        if len(vote):     
            points=int(vote[0].getText().replace('points',''))
    
            print(points)
            hn.append({'title':title,'link':href,'votes':points})
    return sort_stories(hn)
pprint.pprint(create_custom_hn(links,subtexts))