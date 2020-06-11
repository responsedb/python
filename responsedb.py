import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import os as os
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='''Runs all the code''',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-r', '--_responses', dest='responses',
                        type=str,
                        default='open_ended',
                        help='''type''')
    parser.add_argument('-b', dest='bool',
                        type=bool,
                        default=False,
                        help='''boolean value''')  
    parser.add_argument('-n', '--name', dest='name',
                        type=str,
                        default='stats101-2019-03-07.csv',
                        help='''datasets unique''')
    return parser.parse_args()


def list_datasets(dataset_type=None):
    '''
    This method is intended to return the types of databases available.

    Example :

        list_datasets('open_ended')

    Return :

        All datasets in type
    '''
    if dataset_type:
        return _responses[dataset_type].keys()
    else:
        return _responses.keys()

def read_datasets(dataset_type, name=None):
    '''
    This method is intended to return the databases available (to the given name).

    Example :

        read_datasets('open_ended',name='stats101-2019-03-11.csv')

    Return :

        if name is different than "None",:
            return the specified datasets bank
        else:
            return all datasets bank
    '''
    if name:
        return _responses[dataset_type][name]
    else:
        return _responses[dataset_type]


class DatasetManager:
    def __init__(self, responses='open_ended'):
        self.responses = responses

    def type(self):
        '''
        This method is intended to return all the types of databases available.

        Example :

            db = DatasetManager()
            print(db.type())

        Return :

            return types of databases
        '''
        return _responses.keys()

    def read(self,folder='datasets'):
        '''
        this argument is used to read all databases of a specific type
        Example :

            db = DatasetManager('open_ended')
            db.read()
            print(db)

        Return :

            A object the class DatasetManager
        '''
        self.data = _responses[self.responses]
        for key in self.data.keys():
        	self.data[key].read()
        return self

    def describe(self):
        '''
        This method has as function returns the descriptive of the data belonging to the object.

        Example :

            db = DatasetManager('open_ended')
            db.read()
            print(db.describe())
        
        Return :

            return all datasets .describe() of the specific type
        '''
        des = {}
        for keys in self.data.keys():
            des[keys] = self.data[keys].describe()
        return des

    def normalize(self):
        '''
        This method has the function of normalizing, between 0 and 1, the data belonging to the object.

        Example :

            db = DatasetManager('open_ended')
            db.read()
            db.normalize()
            print(db)

        Return :

            A object the class DatasetManager normalized
        '''
        for keys in self.data.keys():
            x = self.data[keys].data
            min_max_scaler = MinMaxScaler()
            x_scaled = min_max_scaler.fit_transform(x.values)
            self.data[keys].data = pd.DataFrame(data=x_scaled, columns=self.data[keys].data.columns, index=self.data[keys].data.index)
        return self.data


class Dataset:
    def __init__(self, url):
        self.url = url
    def type(self):
        '''
        This method is intended to return the types of databases available.

        Example :

            print(list_datasets('open_ended'))

        Return :

            a dict keys of data types
        '''
        return _responses.keys()

    def read(self, folder = 'datasets'):
        '''
        This method has as argument 'folder', by default folder = 'datasets', has the function to 
        check if the file is in the current directory, if there are any errors, download the file.

        Example :

            db = DatasetManager('open_ended')
            db.read()
            print(db)

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

            db = read_datasets('open_ended')['stats101-2019-03-07.csv']
            db.read()
            print(db.describe())
        
        Return :

            the datasets describe
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
        min_max_scaler = MinMaxScaler()
        x_scaled = min_max_scaler.fit_transform(x.values)
        self.data = pd.DataFrame(data=x_scaled, columns=self.data.columns, index=self.data.index)

        return self.data


_responses = {
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

if __name__ == '__main__':
    args = parse_arguments()
    if vars(args)['bool'] == False:
        db = read_datasets(dataset_type=vars(args)['responses'],name=vars(args)['name'])
        db.read()
    else:
        if vars(args)['bool'] == True:
            db = DatasetManager(vars(args)['responses'])
            db.read()