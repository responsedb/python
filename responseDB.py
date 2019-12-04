import pandas as pd
import numpy as np
from sklearn import preprocessing
import os as os

class DatasetManager:
    def __init__(self, responses):
        self.responses = responses

    def type(self):
        return self.responses.keys()

    def read(self):
        self.data = responses[self.responses]
        for key in self.data.keys():
        	self.data[key].read()
        return self

    def describe(self):
        des = {}
        for keys in self.data.keys:
            des[keys] = self.data[keys].describe()
        self.data

class Dataset:
    def __init__(self, url):
        self.url = url
    def type(self):
        '''
        This method is intended to return the types of databases available.

        Example :

            db = responses['open_ended']['stats101-2019-03-11.csv']

            db.type()

        Return :

            responses.keys()
        '''
        return responses.keys()
    def read(self, folder = 'datasets'):
        '''
        This method has as argument 'folder', by default folder = 'datasets', has the function to 
        check if the file is in the current directory, if there are any errors, download the file.

        Example :

            db = responses['open_ended']['stats101-2019-03-11.csv']

            db.read(folder = 'datasets')

        Return :

            self
        '''
        filename = self.url.split('/')[-1]
        try:
            self.data = pd.read_csv(os.path.join(folder, filename), index_col=0)
        except:
            self.data = pd.read_csv(self.url, index_col=0)
            if not os.path.exists(folder):
                os.makedirs(folder)
            self.data.reset_index().to_csv(os.path.join(folder, filename), index=None)
        
        return self
    def describe(self):
        '''
        This method has as function returns the descriptive of the data belonging to the object.

        Example :

            db = responses['open_ended']['stats101-2019-03-11.csv']

            db.read().describe()
        
        Return :

            self.data.describe()
        '''
        return self.data.describe()

    def normalize(self):
        '''
        This method has the function of normalizing, between 0 and 1, the data belonging to the object.

        Example :

            db = responses['open_ended']['stats101-2019-03-11.csv']

            db.read().normalize()

        Return :

            self.data
        '''
        x = self.data
        min_max_scaler = preprocessing.MinMaxScaler()
        x_scaled = min_max_scaler.fit_transform(x.values)
        self.data = pd.DataFrame(data=x_scaled, columns=self.data.columns, index=self.data.index)
        return self.data


responses = {
    'open_ended': {
        'stats101-2019-03-07.csv': Dataset('https://raw.githubusercontent.com/responsedb/datasets/master/open-ended/error-counts/stats101-2019-03-07.csv'),
        'stats101-2019-03-28.csv': Dataset('https://raw.githubusercontent.com/responsedb/datasets/master/open-ended/error-counts/stats101-2019-03-28.csv'),
        'stats101-2019-05-02.csv': Dataset('https://raw.githubusercontent.com/responsedb/datasets/master/open-ended/error-counts/stats101-2019-05-02.csv'),
        'stats101-2019-07-04.csv': Dataset('https://raw.githubusercontent.com/responsedb/datasets/master/open-ended/error-counts/stats101-2019-07-04.csv'),
        'stats101-2019-07-25.csv': Dataset('https://raw.githubusercontent.com/responsedb/datasets/master/open-ended/error-counts/stats101-2019-07-25.csv'),
        'stats101-2019-23-10.csv': Dataset('https://raw.githubusercontent.com/responsedb/datasets/master/open-ended/error-counts/stats101-2019-23-10.csv'),
        'stats101-2019-24-10.csv': Dataset('https://raw.githubusercontent.com/responsedb/datasets/master/open-ended/error-counts/stats101-2019-24-10.csv'),
        'stats101-2019-25-10.csv': Dataset('https://raw.githubusercontent.com/responsedb/datasets/master/open-ended/error-counts/stats101-2019-25-10.csv'),
        'stats101-2019-26-10.csv': Dataset('https://raw.githubusercontent.com/responsedb/datasets/master/open-ended/error-counts/stats101-2019-26-10.csv'),
        'stats101-2019-27-10.csv': Dataset('https://raw.githubusercontent.com/responsedb/datasets/master/open-ended/error-counts/stats101-2019-27-10.csv'),
        'stats101-2019-28-10.csv': Dataset('https://raw.githubusercontent.com/responsedb/datasets/master/open-ended/error-counts/stats101-2019-28-10.csv'),
        'stats101-2019-29-10.csv': Dataset('https://raw.githubusercontent.com/responsedb/datasets/master/open-ended/error-counts/stats101-2019-29-10.csv'),
        'stats101-2019-30-10.csv': Dataset('https://raw.githubusercontent.com/responsedb/datasets/master/open-ended/error-counts/stats101-2019-30-10.csv'),
        'stats101-2019-31-10.csv': Dataset('https://raw.githubusercontent.com/responsedb/datasets/master/open-ended/error-counts/stats101-2019-31-10.csv'),
        'stats101-2019-01-11.csv': Dataset('https://raw.githubusercontent.com/responsedb/datasets/master/open-ended/error-counts/stats101-2019-01-11.csv'),
        'stats101-2019-02-11.csv': Dataset('https://raw.githubusercontent.com/responsedb/datasets/master/open-ended/error-counts/stats101-2019-02-11.csv'),
        'stats101-2019-03-11.csv': Dataset('https://raw.githubusercontent.com/responsedb/datasets/master/open-ended/error-counts/stats101-2019-03-11.csv')
        },
    'scale': {

    },
    'dichotomous':{

    }
    }

db = responses['open_ended']['stats101-2019-03-11.csv']

print(db.type())



