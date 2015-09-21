'''
Created on Sep 21, 2015

@author: fteychene
'''

def register(app):
    app.on_insert_results += validateResults
    
def validateResults(results):
    print(str(results))
    pass