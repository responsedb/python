# responsedb


# Python Code
This repository contains the python code for responsedb

## About 

The purpose of this package is the implementation of codes that allow easy access to certain data, as well as its free manipulation, using response databases from different sources, being used to implement _**Item Response Theory**_ models _**(IRT)**_ for testing.

## Importing Module

~~~Python

import responsedb as rdb

~~~

## Usage

### Databases

Here is the <a href = 'https://github.com/responsedb/datasets'> official repository </a> link for internally avaible databases. They are classified into the following types:


- open-ended ;

- scale ;

- dichotomous.


### Functions

Some basic uses of the package, how :

- **.types()**

~~~Python

rdb.Dataset('responses').type()

~~~

- **Viewing the database for a type** 

~~~Python

print(rdb.response['open_ended'].keys())

~~~

- **Selecting a specific basis** 

~~~Python
db = rdb.response['open_ended']['stats101-2019-03-11.csv'].data
print(db)

~~~

**Some Functions**

- **.normalize()** : data normalization 

~~~Python

db = rdb.response['open_ended']['stats101-2019-03-11.csv']

print(db.normalize())
~~~


- **.describe()** : descriptive data

~~~Python

db = rdb.response['open_ended']['stats101-2019-03-11.csv']

print(db.normalize())

~~~

