import unittest
import ngrams as n

class Test_ngrams(unittest.TestCase):

    base = n.build_ideal_post()

    def test_get_text(self):
        self.assertEqual(n.get_text("test_file"),"my test file\n")
        
    def test_remove_stopwords(self):
        self.assertEqual(n.remove_stopwords("remove the words"),"remove words")
        
    def test_remove_punc(self):
        self.assertEqual(n.remove_punc("!r, .a? \"a 'n"),"r a a n")
        
    def test_get_bigrams(self):
        self.assertEqual(n.get_bigrams("hey there person"),{("hey","there"),("there","person")})
        
    def test_get_unigrams(self):
        self.assertEqual(n.get_unigrams("hey there person"),{"hey","there","person"})
        
    def test_get_jiccard(self):
        self.assertEqual(n.get_jiccard({('a','c'),('a','d')},{('a','b'),('a','c')}),1/float(3))
        
    def test_score_posting(self):
        self.assertEqual(n.score_file("test_posting",self.base),0.0622568093385214)
            
if __name__ == '__main__':
    unittest.main()
