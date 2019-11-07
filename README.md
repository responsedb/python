# Python Code
This repository contains the python code for responseDB

## About 

The purpose of this package is the implementation of codes that allow easy access to certain data, as well as its free manipulation, using response databases from different sources, being used to implement **Item Response Theory** models **(IRT)** for testing.

## Importing Module

'''Python

import responsedb as rdb

'''

## Usage

### Databases

Below is the official repository link for internally avaible databases. They are classified into the following types:
<ul>
<li> <strong> open-ended ;<strong> </li>
<li> <strong> scale ;<strong> </li>
<li> <strong> dichotomous. <strong> </li>
</ul>

### Functions

Some basic uses of the package, how :

<ul> 
<li> .types() </li>
<ul>

~~~Python

rdb.Dataset('responses').type()

~~~

<ul>
<li> Viewing the database for a type </li>
<ul>

~~~Python

print(rdb.response['open_ended'].keys())

~~~

<ul>
<li> Selecting a specific basis </li>
<ul>

~~~Python
db = rdb.response['open_ended']['stats101-2019-03-11.csv'].data
print(db)

~~~

**Some Functions**

<ul>
<li> .normalize() : data normalization </li>
<ul>

~~~Python

db = rdb.response['open_ended']['stats101-2019-03-11.csv']

print(db.normalize())
~~~

<ul>
<li> .describe() : descriptive data</li>
<ul>

~~~Python

db = rdb.response['open_ended']['stats101-2019-03-11.csv']

print(db.normalize())

~~~

