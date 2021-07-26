import json
employee = {'name':'veerareddy','age':22,'salary':10000.0,'ismarried':False,'ishavingbike':None}

json_string = json.dumps(employee,indent=4)
print(json_string)

with open('emp.json','w') as f:
    json.dump(employee,f,indent=4)
