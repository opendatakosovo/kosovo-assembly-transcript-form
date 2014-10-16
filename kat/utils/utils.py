from flask import request, current_app
from pymongo import MongoClient
import flask_pymongo
import re


class Utils(object):

    def __init__(self):
        pass

    def get_mp_party(self, mp, year):
        mongo = MongoClient()
        collection_name = "mpassetdeclarations"
        #print "GETTING MP PARTY"
        cursor = mongo.kosovoassembly[collection_name].find()

        party_year = int(year)

        for cur in cursor:
            if mp == cur["mp"]["slug"] and party_year == cur["year"]:

                return cur["party"]["name"]
              
        '''
        for party in party_members:
            #print party["party"]
            for mps in party["mps"]:
                #print mps
                if mp == mps['slug']:
                    #print mp+ " belongs to " + party["party"]["slug"]
        '''
