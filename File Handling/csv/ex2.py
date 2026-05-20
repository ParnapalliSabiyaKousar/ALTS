import json
person={
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScript","React","python"]
}
with open ('person.json','w', encoding='utf-8')as f:
    json.dump(person , f, ensure_ascii=False, indent=4)
print(person)
