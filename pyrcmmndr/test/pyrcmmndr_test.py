import unittest
from pyrcmmndr import RcmmndrClient
import json

__author__ = 'codemomentum'


class TestRcmmndrClient(unittest.TestCase):
    def test_basic_flow(self):
        pyrcmmndr = RcmmndrClient("0000000000000000000000000000000000000000001", "http://localhost:8001")
        #initialize
        pyrcmmndr.delete_all_preferences()

        #create some preferences
        pyrcmmndr.create_preference(1, 101, 1.0)

        #check the stats
        stats = pyrcmmndr.get_usage_stats()
        assert stats['total_preferences'] == 1
        assert stats['distinct_keys'] == 1

        pyrcmmndr.create_preference(2, 101, 1.0)
        pyrcmmndr.create_preference(2, 102, 2.0)

        stats = pyrcmmndr.get_usage_stats()
        assert stats['total_preferences'] == 3
        assert stats['distinct_keys'] == 2

        pyrcmmndr.delete_preferences_of_user(2)
        stats = pyrcmmndr.get_usage_stats()
        assert stats['total_preferences'] == 1
        assert stats['distinct_keys'] == 1

        pyrcmmndr.delete_all_preferences()
        stats = pyrcmmndr.get_usage_stats()
        assert stats['total_preferences'] == 0
        assert stats['distinct_keys'] == 0

        pyrcmmndr.create_preference(1, 101, 5)
        pyrcmmndr.create_preference(1, 102, 3)
        pyrcmmndr.create_preference(1, 103, 2.5)

        pyrcmmndr.create_preference(2l, 101l, 2)
        pyrcmmndr.create_preference(2l, 102l, 2.5)
        pyrcmmndr.create_preference(2l, 103l, 5)
        pyrcmmndr.create_preference(2l, 104l, 2)

        pyrcmmndr.create_preference(3l, 101l, 2.5)
        pyrcmmndr.create_preference(3l, 104l, 4)
        pyrcmmndr.create_preference(3l, 105l, 4.5)
        pyrcmmndr.create_preference(3l, 107l, 5)

        pyrcmmndr.create_preference(4l, 101l, 5)
        pyrcmmndr.create_preference(4l, 103l, 3)
        pyrcmmndr.create_preference(4l, 104l, 4.5)
        pyrcmmndr.create_preference(4l, 106l, 4)

        pyrcmmndr.create_preference(5l, 101l, 4)
        pyrcmmndr.create_preference(5l, 102l, 3)
        pyrcmmndr.create_preference(5l, 103l, 2)
        pyrcmmndr.create_preference(5l, 104l, 4)
        pyrcmmndr.create_preference(5l, 105l, 3.5)
        pyrcmmndr.create_preference(5l, 106l, 4)

        #get recommendations
        recs = pyrcmmndr.get_recommendation(1)
        print recs

        assert '104' in recs

        print pyrcmmndr.get_settings()

        rec = """
        {
             "recommender": {
                  "impl":"GenericUserBasedRecommender",
                  "params":{
                       "UserSimilarity" : {
                            "impl":"PearsonCorrelationSimilarity"
                       },
                       "UserNeighborhood":{
                            "impl":"NearestNUserNeighborhood",
                            "params": {
                                 "n":2
                            }
                       }
                  }
             }
        	}
         """

        pyrcmmndr.update_settings(json.loads(rec))

        print pyrcmmndr.get_settings()

        pyrcmmndr.create_preference(1, 101, 5, datatype="type1")
        recs2 = pyrcmmndr.get_recommendation(1, datatype="type1")
        print recs2
        assert recs <> recs2

        rec2 = """
        {
             "recommender": {
                  "impl":"GenericUserBasedRecommender",
                  "params":{
                       "UserSimilarity" : {
                            "impl":"PearsonCorrelationSimilarity"
                       },
                       "UserNeighborhood":{
                            "impl":"NearestNUserNeighborhood",
                            "params": {
                                 "n":40
                            }
                       }
                  }
             }
        	}
         """

        pyrcmmndr.update_settings(json.loads(rec2), datatype="type1")

        print pyrcmmndr.get_settings(datatype="type1")

    def test_bulk_update(self):
        pyrcmmndr = RcmmndrClient("0000000000000000000000000000000000000000001", "http://localhost:8001")
        #initialize
        pyrcmmndr.delete_all_preferences()
        stats = pyrcmmndr.get_usage_stats()
        assert stats['total_preferences'] == 0
        assert stats['distinct_keys'] == 0

        #bulk update
        pyrcmmndr.bulk_update_preferences('preferences.tsv')
        stats = pyrcmmndr.get_usage_stats()
        assert stats['total_preferences'] == 22
        assert stats['distinct_keys'] == 21


    def test_create_some_load(self):
        pyrcmmndr = RcmmndrClient("0000000000000000000000000000000000000000001", "http://localhost:8001")
        #initialize
        pyrcmmndr.delete_all_preferences()

        #create some preferences
        for x in range(0, 1000):
            pyrcmmndr.create_preference(x + 1, 101, 5)
            pyrcmmndr.create_preference(x + 1, 102, 3)
            pyrcmmndr.create_preference(x + 1, 103, 2.5)

            pyrcmmndr.create_preference(x + 2l, 101l, 2)
            pyrcmmndr.create_preference(x + 2l, 102l, 2.5)
            pyrcmmndr.create_preference(x + 2l, 103l, 5)
            pyrcmmndr.create_preference(x + 2l, 104l, 2)

            pyrcmmndr.create_preference(x + 3l, 101l, 2.5)
            pyrcmmndr.create_preference(x + 3l, 104l, 4)
            pyrcmmndr.create_preference(x + 3l, 105l, 4.5)
            pyrcmmndr.create_preference(x + 3l, 107l, 5)

            pyrcmmndr.create_preference(x + 4l, 101l, 5)
            pyrcmmndr.create_preference(x + 4l, 103l, 3)
            pyrcmmndr.create_preference(x + 4l, 104l, 4.5)
            pyrcmmndr.create_preference(x + 4l, 106l, 4)

            pyrcmmndr.create_preference(x + 5l, 101l, 4)
            pyrcmmndr.create_preference(x + 5l, 102l, 3)
            pyrcmmndr.create_preference(x + 5l, 103l, 2)
            pyrcmmndr.create_preference(x + 5l, 104l, 4)
            pyrcmmndr.create_preference(x + 5l, 105l, 3.5)
            pyrcmmndr.create_preference(x + 5l, 106l, 4)


if __name__ == '__main__':
    unittest.main()