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
            'url': 'survey/<regex("[a-f0-9]{24}"):survey>/results',
            'schema': ResultConfiguration.schema(),
            'datasource': {
                'source': 'results'
            },
            'resource_title': 'results',
            'resource_methods': ['GET', 'POST'],
            'item_methods': ['GET', 'DELETE'],
        }

    @staticmethod
    def schema():
        return {
            'commiter': {
                'type': 'dict',
                'schema': {
                    'firstName': {
                        'type': 'string',
                        'minlength': 1,
                    },
                    'lastName': {
                        'type': 'string',
                        'minlength': 1,
                        'required': True,
                    }
                },
                'unique': True,
            },
            'survey': {
                'type': 'objectid',
                'data_relation': {
                    'resource': 'survey'
                },
                'required': True,
            },
            'responses': {
                'type': 'list',
                'schema': {
                    'type': 'list',
                    'schema': {
                        'type': 'dict',
                        'schema': {
                            'response_index': {
                                'type': 'integer',
                            },
                            'text': {
                                'type': 'string',
                            },
                            'valid': {
                                'type': 'boolean'
                            },
                        },
                    },
                },
                'required': True,
            }
        }
