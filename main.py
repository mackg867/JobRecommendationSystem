import ngrams as ng
import job_fetcher as jf
from webbrowser import open 
from time import sleep
from database_plumbing import DB_Connection 

def get_search_results():
    search_results = []
    for num in ['1','2','3','4']:
        response = jf.make_dice_request('data',num)
        search_results += jf.get_dice_results(response)
    return search_results

def get_job_data(search_results,post):
    scores = []
    job_titles = []
    job_summaries = []
    job_websites = []
    for job in search_results:
        summary = jf.get_dice_job_summary(job)
        job_websites.append(job['detailUrl'])
        job_titles.append(job['jobTitle'])
        scores.append(ng.score_text(summary,post))
        job_summaries.append(summary)
    return zip(scores,job_titles,job_summaries,job_websites)
            
def open_websites(data):
    for job in data:
        if job[0] > .03:
            open(job[3])
            sleep(2)

if __name__ == "__main__":
    base_post = ng.build_ideal_post()
    
    results = get_search_results()
    data = get_job_data(results,base_post)
    data = sorted(data,key=lambda tup: tup[0],reverse=True)
    open_websites(data)
    
    d = DB_Connection('jobs.db')
    d.write_data(data)
    d.remove_dups()
    d.close_connection()
    

