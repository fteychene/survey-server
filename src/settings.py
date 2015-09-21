'''
Created on Sep 21, 2015

@author: fteychene
'''
from survey.settings import SurveyConfiguration
from result.settings import ResultConfiguration

DOMAIN = {
    'survey': SurveyConfiguration.domain(),
    'results': ResultConfiguration.domain()
}

HOOKS_REGISTERS = [
        ResultConfiguration.hooks()
    ]

PROPAGATE_EXCEPTIONS=True

## DB Configuration
MONGO_HOST= 'localhost'
MONGO_PORT= 27017
MONGO_DBNAME = 'survey_server'