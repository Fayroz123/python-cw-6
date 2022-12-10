# write your code here
person = {
'name': "fayroz",
'age': "18",
'hobbies': ["swimming", "drawing"],


}
print(person['name'])
print(person['age'])
person["country"] = "sirya"

person['age']=19
print(person['age'])
print(person)
print(len(person))
person["hobbies"].append("reading") 
print(person["hobbies"])


def check_hobbies(person):
    if len(person["hobbies"]) >= 3 :
        print("WOW YOU ARE AMAZING")
    
    
check_hobbies(person)
