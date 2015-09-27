'''
Created on Sep 21, 2015

@author: fteychene
'''

from result import hooks

class ResultConfiguration(object):
    
    @staticmethod
    def hooks():
        return hooks.register
    
    @staticmethod
    def domain():
        return {
            'schema' : ResultConfiguration.schema(),
            'datasource' : ResultConfiguration.datasource(),
            'resource_methods' : ['GET', 'POST'],
            'item_methods' : ['GET', 'DELETE'],
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
                        'minlength':1,
                    },
                    'lastName': {
                        'type':'string',
                        'minlength':1,
                        'required': True,
                    }
                },
            },
            'test': {
                'type':'objectid',
                'data_relation':{
                    'resource':'survey'
                },
                'required': True,
            },
            'result': {
                'type':'list',
                'schema':{
#                     'type':'dict',
#                     'schema': {
#                         'responses': {
                            'type':'list',
                            'schema':{
                                'type':'dict',
                                'schema': {
                                    'response': {
                                        'type':'integer',
                                    },
                                    'valid': {
                                        'type': 'boolean'
                                    },
                                },
                            },
#                         }
#                     }
                },
                'required': True,
            }
        }