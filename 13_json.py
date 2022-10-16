import json
from random import shuffle #*
#json gets converted to dict

data1='''{  
    "employee": [1,2,3],
    "123": {
        "salary":1800000,
        "married":"True"
    },
    "dummy":[123]
}'''


print(data1)
jsondata=json.loads(data1)
print(jsondata)