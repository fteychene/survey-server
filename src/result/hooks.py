'''
Created on Sep 21, 2015

@author: fteychene
'''
from flask import current_app as app, abort


def register(app):
    app.on_insert_results += validate_results


def validate_results(results):
    survey_collection = app.data.driver.db['survey']
    for result in results:
        survey = survey_collection.find_one({'_id': result['survey']})
        if len(result['responses']) > len(survey['question']) :
            abort(409, "More responses than questions of the survey ...")
        for index, responses in enumerate(result['responses']):
            question = survey['question'][index]
            for response in responses:
                response['valid'] = question['responses'][response['response_index']]['valid']