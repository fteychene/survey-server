'''
Created on Sep 21, 2015

@author: fteychene
'''
from eve import Eve
from settings import SETTINGS
from settings import HOOKS_REGISTERS

def generateApp():
    app = Eve(settings = SETTINGS)
    for register in HOOKS_REGISTERS:
        register(app)
    return app
        
app = generateApp()

if __name__ == '__main__':
    app.run()

# def startEveApplication():
#     filePath = './'+'settings.py'
#     print('Loading configuration')
#     app = Eve(settings = filePath)
#     
#     for register in HOOKS_REGISTERS:
#         register(app)
#     
#     app.run()
# 
# if __name__ == '__main__':
#     startEveApplication()