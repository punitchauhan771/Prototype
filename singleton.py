import pymongo
from pymongo import MongoClient

def singleton(class_):
    '''a singleton design decorator used for creating a singleton'''
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance

@singleton
class DBConnection:
    ''' Class for creating a connection with Database server.
        Change MongoClient to your desire db connector sdk/module,
        in this case we are using Mongodb so we are using pymongo module
    '''

    def __init__(self,constr = None):
        """ Initialize your database connection here. """
        try:
            if constr is None:
                self.ctx = MongoClient('localhost','<port-no>') #replace port no with your port no
            else:
                self.ctx = MongoClient(constr) 
        except Exception as e:
            print(f"Error:{e}")

    def getinstance(self):
        '''Returns database connection object'''
        return self.ctx
