import json
import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

data = json.loads(sampleJson)
print(data)
salary_key_level = data['company']['employee']['payable']['salary']
data['company']['employee']['birth_date'] = '1990-01-01'


with open('new_json','w') as json_fail:
    json.dump(data,json_fail,indent=2)

