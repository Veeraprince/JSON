import json
with open('emp.json','r') as f:

    emp_dict = json.load(f)

for k,v in emp_dict.items():
    print('{}  :  {}'.format(k,v))
    
    
    



