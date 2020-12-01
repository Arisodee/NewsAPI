import unittest
from app.models import Article


class ArticlesTest(unittest.TestCase):
    '''
    Test class to test behaviour of the article class
    '''
    def setUp(self):
        '''
        Method to run before every Test
        '''
        self.new_article = Article( "Matt Clinch","OPEC alliance considers delay to its output hike, but faces a U.S. shale industry 'itching to drill again' - CNBC","A planned 2 million bpd January production ramp-up looks set to be delayed, according to market consensus.","https://www.cnbc.com/2020/11/29/opec-alliance-considers-delay-to-its-output-hike.html","2020-11-29T17:41:00Z", "https://image.cnbcfm.com/api/v1/image/103931823-GettyImages-2823129.jpg?v=1601568116")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,article))

if __name__ == '__main__':
    unittest.main()