'''
Created on Sep 21, 2015

@author: fteychene
'''

class SurveyConfiguration(object):
    
    @staticmethod
    def domain():
        return {
            'schema' : SurveyConfiguration.schema(),
            'datasource' : SurveyConfiguration.datasource(),
            'item_methods' : ['GET', 'PATCH', 'PUT', 'DELETE'],
            'resource_methods' : ['GET', 'POST']
    }
        
    @staticmethod
    def datasource():
        return {
                'projection': {'question.response.valid': 0}
            }

    @staticmethod
    def schema():
        return {
            'name' : {
                'type':'string',
                'required':True,
                'unique':True},
            'question': {
                'type':'list',
                'schema':{
                    'type': 'dict',
                    'schema': {
#                         'number' : {
#                             'type':'integer',
#                             'required':True},
                        'text': {
                            'type':'string',
                            'minlength': 1},
                        'type':{
                            'type':'string',
                            'allowed':['One', 'Many']},
                        'response': {
                            'type':'list',
                            'schema':{
                                'type': 'dict',
                                'schema': {
                                    'text':{
                                        'type':'string',
                                        'minlength': 1},
                                    'valid':{
                                        'type':'boolean'}
                                }
                            }
                        }
                    }
                }
            }
        }