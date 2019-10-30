import pandas as pd
import numpy as np
from sklearn import preprocessing

#class DatasetManager:
#    def __init__(self, response_type):
#        self.response_type = response_type
#    def read(self):
#        self.data = responses[self.response_type]
#        return self
 
class DatasetManager:
    def __init__(self, responses):
        self.response = responses
    def read(self):
        self.data = responses[self.response]
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
    def read(self):
        self.data = pd.read_csv(self.url, index_col = 0)
        return self
    def describe(self):
        return self.data.describe()
#    def normalize(self):
#        self.norm = preprocessing.scale(self.data)
#        return self.norm
    def normalize(self):
        x = self.data
        min_max_scaler = preprocessing.MinMaxScaler()
        x_scaled = min_max_scaler.fit_transform(x)
        df = pd.DataFrame(x_scaled)
        return df

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
responses_type = list(responses.keys())

print(responses_type)

db = responses['open_ended']['stats101-2019-02-11.csv'].read()

print(db.normalize())
#

