import json

json_string = """
{
    "name": "veerareddy",
    "age": 22,
    "salary": 10000.0,
    "ismarried": false,
    "ishavingbike": null
}
"""

emp_data = json.loads(json_string)
print(type(emp_data))

for k,v in emp_data.items():
    print('{} : {}'.format(k,v)) 
