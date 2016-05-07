import unittest
import job_fetcher as jf
import json
import ngrams as n

class test_cases(unittest.TestCase):
    
    response = jf.make_dice_request("data","1")
    base = n.build_ideal_post()
    
    #job_fetcher.py test cases
    def test_get_dice_results(self):
        data = json.loads(self.response.text)
        self.assertTrue(len(data['resultItemList'])>0)

    #ngrams.py test cases
    def test_get_text(self):
        self.assertTrue(n.get_text("ideal_post")[:9]=='attention')
        
    def test_remove_stopwords(self):
        self.assertEqual(n.remove_stopwords("remove the words"),
        "remove words")
        
    def test_remove_punc(self):
        self.assertEqual(n.remove_punc("!r, .a? \"a 'n"),"r a a n")
        
    def test_get_bigrams(self):
        self.assertEqual(n.get_bigrams("hey there person"),
        {("hey","there"),("there","person")})
        
    def test_get_unigrams(self):
        self.assertEqual(n.get_unigrams("hey there person"),
        {"hey","there","person"})
        
    def test_get_jiccard(self):
        self.assertEqual(n.get_jiccard({('a','c'),('a','d')},
        {('a','b'),('a','c')}),1/float(3))
        
    def test_score_text(self):
        self.assertEqual(n.score_text("data",self.base),
        0.010309278350515464)

        
        
if __name__ == '__main__':
    unittest.main()        
