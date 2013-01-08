##PyRcmmndr
Python Client for the Rcmmndr platform. It is using httplib2 for communicating with the server

###Creating a Client Instance

	pyrcmmndr=RcmmndrClient("API_KEY")


###Adding Preferences

	pyrcmmndr.create_preference(1,101,1.0)
	
###Making Recommendations
	recs=pyrcmmndr.get_recommendation(1)
the dictionary 'recs' will contain the recommendation results as itemid,value pairs

###Usage Statistics
You can check the usage statistics for your account as follows:

        stats=pyrcmmndr.get_usage_stats()
        assert stats['total_preferences'] == 1
        assert stats['distinct_keys'] == 1
        
        
###Deleting Preferences

####Deleting Preferences for specific user
	pyrcmmndr.delete_preferences_of_user(1)

####Deleting All Preferences
	pyrcmmndr.delete_all_preferences()
	
	
###Bulk API
Bulk API is a better way of inserting many number of preference values. It is done by posting a text file (comma or tab separated) to the server.

	pyrcmmndr.bulk_update_preferences('preferences.tsv')
	
where the contents of preferences.tsv are similar to the following: (userID,itemID,preference)

	196,242,3
	186,302,3
	22,377,1
	244,51,2
	166,346,1

###Additional Notes
Make sure to check the unit test which shows the basic usage scenario.

