##PyRcmmndr
Python Client for the Rcmmndr platform. It is using httplib2 for communicating with the server

##Installation

	pip install git+https://github.com/Rcmmndr/pyrcmmndr.git

	>>>import pyrcmmndr

###Creating a Client Instance

	pyrcmmndrClient=pyrcmmndr.RcmmndrClient("API_KEY")


###Adding Preferences

	pyrcmmndrClient.create_preference(1,101,1.0)
	
###Making Recommendations
	recs=pyrcmmndrClient.get_recommendation(1)
the dictionary 'recs' will contain the recommendation results as itemid,value pairs

###Usage Statistics
You can check the usage statistics for your account as follows:

        stats=pyrcmmndrClient.get_usage_stats()
        assert stats['total_preferences'] == 1
        assert stats['distinct_keys'] == 1
        
        
###Deleting Preferences

####Deleting Preferences for specific user
	pyrcmmndrClient.delete_preferences_of_user(1)

####Deleting All Preferences
	pyrcmmndrClient.delete_all_preferences()
	
	
###Bulk API
Bulk API is a better way of inserting many number of preference values. It is done by posting a text file (comma or tab separated) to the server.

	pyrcmmndrClient.bulk_update_preferences('preferences.tsv')
	
where the contents of preferences.tsv are similar to the following: (userID,itemID,preference)

	196,242,3
	186,302,3
	22,377,1
	244,51,2
	166,346,1

###Settings API
Using the settings API, you can finetune your recommender and try different recommendation algorithms. Please refer to the Restful API documentation for detailed usage of the Settings API.

####Getting Current Settings

		pyrcmmndrClient.get_settings()
	
Returns the current settings as a dictionary.

####Updating Settings
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


###Additional Notes
You can also check the unit test which shows the basic usage scenario.


