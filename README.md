# JobRecommendationSystem
The is a repository for a system that recommends job postings that are similar to ones I have applied to in the past.  It uses the Dice.com API and Python.

At a high level this program builds a bigram and unigram model of an ideal job posting based off of jobs I have previously applied for.  Then it searches the Dice job board for jobs that are similar to my ideal job post.  It uses the Jiccard Index to measure how similar the postings are to each other.  Jobs that meet a certain thereshold (.03) have their website opened automatically for further review.  Finally all the job posting data is saved to a local SQLite database.
