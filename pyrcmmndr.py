from common import *

__author__ = 'codemomentum'

class RcmmndrClient(object):
    def __init__(self, apiKey, server_url="http://api.rcmmndr.com/"):
        self.apiKey = apiKey
        self.server_url = server_url

    def get_preference_url(self, user_id):
        return self.server_url + '/api_key/' + self.apiKey + '/preference/' + str(user_id)

    def create_preference(self,user_id,item_id,preference):
        post_content(self.get_preference_url(user_id) +'/'+str(item_id)+'/'+str(preference),None)

    def get_recommendation(self,user_id):
        return get_content(self.server_url+'/api_key/'+self.apiKey+'/recommend/'+str(user_id))

    def get_usage_stats(self):
        return get_content(self.server_url+'/api_key/'+self.apiKey+'/_stats')

    def delete_preferences_of_user(self,user_id):
        delete_content(self.get_preference_url(user_id))

    def delete_all_preferences(self):
        delete_content(self.server_url + '/api_key/' + self.apiKey + '/preference/_all')

    def bulk_update_preferences(self,file):
        data = open(file).read()
        post_content( self.server_url + '/api_key/' + self.apiKey + '/preference/_bulk',data,request_headers = {'Content-Type': 'text/plain'})
