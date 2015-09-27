'''
Created on Sep 21, 2015

@author: fteychene
'''
import os
from survey.settings import SurveyConfiguration
from result.settings import ResultConfiguration


SETTINGS = {
    'DOMAIN': {
               'survey': SurveyConfiguration.domain(),
               'results': ResultConfiguration.domain(),
               },
    'MONGO_HOST' : os.environ.get('MONGODB_PORT_27017_TCP_ADDR') or 'localhost',
    'MONGO_PORT' : int(os.environ.get('MONGODB_PORT_27017_TCP_PORT') or '27017'),
    'MONGO_DBNAME' : 'survey_server',
    'PROPAGATE_EXCEPTIONS' : True,
    }

HOOKS_REGISTERS = [
        ResultConfiguration.hooks(),
    ]


# DOMAIN = {
#     'survey': SurveyConfiguration.domain(),
#     'results': ResultConfiguration.domain(),
#     }
# 
# PROPAGATE_EXCEPTIONS = True
# 
# # # DB Configuration
# MONGO_HOST = os.environ.get('MONGODB_PORT_27017_TCP_ADDR') or 'localhost'
# MONGO_PORT = int(os.environ.get('MONGODB_PORT_27017_TCP_PORT') or '27017')
# MONGO_DBNAME = 'survey_server'
