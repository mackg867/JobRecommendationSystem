import sqlite3
import uuid as u

class DB_Connection:
    """Current DB Schema
       id|score|job_title|job_summary|job_website"""
        
    def __init__(self,db_name):
        """Setup database connection"""
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()

    def close_connection(self):
        """Commit changes before closing connction"""
        self.conn.commit()
        self.conn.close()
   
    def write_data(self,jobs):
        """Add a uuid as the primary key before saving data"""
        jobs = [(str(u.uuid4()),) + job for job in jobs]
        self.cur.executemany('INSERT INTO jobs VALUES (?,?,?,?,?)',jobs)
        
    def remove_dups(self):
        """Remove any duplicates from the database"""
        self.cur.execute('DELETE FROM jobs WHERE ID in (SELECT ID FROM jobs WHERE score=score and title=title group by score having count(*)>1);')
            

