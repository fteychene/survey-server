'''
Created on Sep 21, 2015

@author: fteychene
'''
from eve import Eve
from settings import HOOKS_REGISTERS

def startEveApplication():
    filePath = './'+'settings.py'
    app = Eve(settings = filePath)
    
    for register in HOOKS_REGISTERS:
        register(app)
    
    app.run()

if __name__ == '__main__':
    startEveApplication()