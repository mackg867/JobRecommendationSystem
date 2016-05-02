import requests
import json
from bs4 import BeautifulSoup

def make_indeed_request():
    """Note: the Indeed API only returns 10
    responses per search"""
    return requests.get('http://api.indeed.com/ads/apisearch?publisher=8088628362474696&q=data+-manager+-senior+-big+-director&l=Portland%2C+OR&&radius=25&limit=100&v=2&format=json&sort=date')
    
def make_dice_request(search_text,page_num):
    """Input parameters must be strings"""
    keys = {'text': search_text,'page': page_num,'pgcnt': '50','sort': '1','state': 'OR','city': 'Portland','sd': 'd'}
    return requests.get('http://service.dice.com/api/rest/jobsearch/v1/simple.json?',params=keys)

def get_results(response):
    """Designed to work with Dice JSON reponse"""
    data = json.loads(response.text)
    try:
        return data['resultItemList']
    except:
        return []
    
def get_job_summary(job_posting):
    """Designed to work with the Dice JSON 
    response"""
    try:
        data = requests.get(job_posting['detailUrl'])
    except:
        print "Error in getting job summary"
        return " "
    else:
        html_data = BeautifulSoup(data.text,'html.parser')
        job_desc = html_data.find(id="jobdescSec")
        if job_desc is not None:
            summary = job_desc.get_text()
            return summary.replace("\n"," ")
        else:
            return " "
    
def get_job_title(job_posting):
    """Designed to work with the Dice JSON
    response"""
    return job_posting['jobTitle']
