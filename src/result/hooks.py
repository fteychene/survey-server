'''
Created on Sep 21, 2015

@author: fteychene
'''
from flask import current_app as app
import json

def register(app):
    app.on_insert_results += validateResults
    
def validateResults(results):
    print(results)
    survey_collection = app.data.driver.db['survey']
    survey = survey_collection.find_one({'_id':results[0]['test']})
    for index, responses in enumerate(results[0]['result']):
        for response in responses:
            if survey['question'][index]['response'][response['response']]['valid'] == True:
                response['valid'] = True
            else:
                response['valid'] = False
        
    print survey
    pass