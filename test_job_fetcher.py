import unittest
import job_fetcher as jf
import json

class Test_job_fecther(unittest.TestCase):
    
    response = jf.make_dice_request()
    
    def test_make_dice_request(self):
        data = json.loads(self.response.text)
        self.assertTrue(len(data['resultItemList'])>0)
        
        
if __name__ == '__main__':
    unittest.main()        
