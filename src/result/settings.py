'''
Created on Sep 21, 2015

@author: fteychene
'''

import hooks

class ResultConfiguration(object):
    
    @staticmethod
    def hooks():
        return hooks.register
    
    @staticmethod
    def domain():
        return {
            'schema' : ResultConfiguration.schema(),
            'datasource' : ResultConfiguration.datasource()
    }
        
    @staticmethod
    def datasource():
        return {
                
            }

    @staticmethod
    def schema():
        return {
            'commiter' : {
                'type':'dict',
                'schema' : {
                    'firstName': {
                        'type':'string',
                        'minlength':1
                    },
                    'lastName': {
                        'type':'string',
                        'minlength':1
                    }
                }
            },
            'test': {
                'type':'objectid',
                'data_relation':{
                    'resource':'test'
                },
                'required': True   
            },
            'result': {
                'type':'list',
                'schema':{
                    'type':'dict',
                    'schema': {
                        'questionId': {
                            'type':'integer',
                            'required':True
                        },
                        'responses': {
                            'type':'list'
                        }
                    }
                }
            }
        }