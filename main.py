import ngrams as ng
import job_fetcher as jf
import webbrowser as wb
import time
import database_plumbing as db

def get_search_results():
    search_results = []
    for num in ['1','2','3','4']:
        response = jf.make_dice_request('data',num)
        search_results += jf.get_results(response)
    return search_results

def get_job_data(search_results,post):
    scores = []
    job_titles = []
    job_summaries = []
    job_websites = []
    for job in search_results:
        summary = jf.get_job_summary(job)
        job_websites.append(job['detailUrl'])
        job_titles.append(job['jobTitle'])
        scores.append(ng.score_text(summary,post))
        job_summaries.append(summary)
    return zip(scores,job_titles,job_summaries,job_websites)

def write_data(data):
    f_handle = open('data.txt','w')
    for tup in data:
        for element in tup:
            f_handle.write('%s,' % element)
        f_handle.write('\n')
    f_handle.close()
            
def open_websites(data):
    for job in data:
        if job[0] > .03:
            wb.open(job[3])
            time.sleep(2)
    
if __name__ == "__main__":    
    base_post = ng.build_ideal_post()
    results = get_search_results()
    data = get_job_data(results,base_post)
    data = sorted(data,key=lambda tup: tup[0],reverse=True)
    open_websites(data)
    
    #Write data to database
    d = db.DB_Connection('jobs.db')
    d.write_data(data)
    d.remove_dups()
    d.close_connection()
    

