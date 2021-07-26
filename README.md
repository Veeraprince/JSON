OBJECT SERIALIZATION:
The process on converting an object from python supported form to file suppoeted form or network supported form,is called serialization.(Marshalling or pickling)

DESRRIALIZATION:
The process of converting an object from either file supported or network supported form to python supported form, is called Deserialization.(UnMarshalling or Unpickling)

Object Serialization by using pickle. 
Object Serialization by using JSON.
Object Serialization by using Yaml.

OBJECT SERIALIZATION BY USING JSON:
-----------------------------------
JSON ==> JavaSscript Object Notation. 

The most commonly used message format for applications
irrespective of any programmming language.

JSON is human readable format.


PYTHON--------JAVASCEIPT:
-------------------------
int ---------------Number
float--------------Number
list---------------Array
tuple--------------Array
dict---------------Object
True---------------true
False--------------false
None---------------null

JSON is similar to python dict
JS object contains a group of key value pairs.


WHY JSON IS VERY POPULAR.

Any programming language can understand.

JSON is language independent.

Light weight and required less memory.
Note==>(in past XML message format is used but it is heavy weight)

JSON MODULE:
------------

As a part of programming requirement, it is very common requirement to convert python object into json form and from json form into python object so python provides a inbuilt module json.

JSON MODULE DEFINES THE FOLLOWING IMPORTANT FUNCTIONS:

SERIALIZATION PURPOSE(From Python form to JSON form):
----------------------------------------------------
1.dumps() ==> it serializes python dict to json string.

2.dump()  ==>  converting python dict to json and wrie that json to provided json file.

ex(1,2): see emp.py file from that we genarated emp.json


DESERIALIZATION PURPOSE(From JSON form to Python form):
------------------------------------------------------

1.loads() ==> Converting JSON string to python dict. It Deserializes a string.

2.load()  ==> Reading JSON from a file and converting to python dict object.
Deserializes from a json file.
ex:(look at EMP.py and prac.py)


REALWORD EXAMPLE 

to know the bitcoin prices

for this we need to send a http request to that coindesk

we reuire to install the module using - pip3 install requests

search for bitcoin api json and there will be coindesk link click on it.

copy the Api like below: 
https://api.coindesk.com/v1/bpi/currentprice.json 

we get data like this(see realex.py) 

I got this data as output:

{'time': {'updated': 'Jul 26, 2021 13:18:00 UTC', 'updatedISO': '2021-07-26T13:18:00+00:00', 'updateduk': 'Jul 26, 2021 at 14:18 BST'}, 

'disclaimer': 'This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org', 

'chartName': 'Bitcoin', 

'bpi': {'USD': {'code': 'USD', 'symbol': '&#36;', 'rate': '38,115.7450', 'description': 'United States Dollar', 'rate_float': 38115.745},

'GBP': {'code': 'GBP', 'symbol': '&pound;', 'rate': '27,662.0827', 'description': 'British Pound Sterling', 'rate_float': 27662.0827},

'EUR': {'code': 'EUR', 'symbol': '&euro;', 'rate': '32,347.9180', 'description': 'Euro', 'rate_float': 32347.918}}}





 







