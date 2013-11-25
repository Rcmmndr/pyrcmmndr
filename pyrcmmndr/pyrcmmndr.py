from common import *
import json

__author__ = 'codemomentum'


class RcmmndrClient(object):
    def __init__(self, apiKey, server_url="http://api.rcmmndr.com/"):
        self.apiKey = apiKey
        self.server_url = server_url

    def get_root_url(self, datatype):
        if datatype is None:
            return self.server_url + '/api_key/' + self.apiKey
        else:
            return self.server_url + '/api_key/' + self.apiKey + '/type/' + datatype

    def get_preference_url(self, user_id, datatype=None):
        return self.get_root_url(datatype) + '/preference/' + str(user_id)

    def create_preference(self, user_id, item_id, preference, datatype=None):
        post_content(self.get_preference_url(user_id,datatype=datatype) + '/' + str(item_id) + '/' + str(preference), None)

    def get_recommendation(self, user_id, datatype=None):
        return get_content(self.get_root_url(datatype) + '/recommend/' + str(user_id))

    def get_usage_stats(self):
        return get_content(self.get_root_url(None) + '/_stats')

    def delete_preferences_of_user(self, user_id, datatype=None):
        delete_content(self.get_preference_url(user_id,datatype=datatype))

    def delete_all_preferences(self, datatype=None):
        delete_content(self.get_root_url(datatype) + '/preference/_all')

    def bulk_update_preferences(self, file, datatype=None):
        data = open(file).read()
        post_content(self.get_root_url(datatype) + '/preference/_bulk', data,
                     request_headers={'Content-Type': 'text/plain'})

    def get_settings(self, datatype=None):
        return get_content(self.get_root_url(datatype) + '/_settings')

    def update_settings(self, settings_dict, datatype=None):
        post_content(self.get_root_url(datatype) + '/_settings', json.dumps(settings_dict))