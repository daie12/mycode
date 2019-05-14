#!usr/bin/env python3
first_list=[]
first_dict={"first_name":"Monthy","last_name":"Python","actions":["Scooter",2,"Moscow"]}
print(f'In {first_dict["first_name"]} {first_dict["last_name"]}, Eric Idle rode a {first_dict["actions"][0]} {first_dict["actions"][1]} {first_dict["actions"][2]}')
second_list=["horse","to","the Holy Grail"]
first_list.extend(second_list)
first_dict["actions"]=first_list
print(f'In {first_dict["first_name"]} {first_dict["last_name"]}, Eric Idle rode a {first_dict["actions"][0]} {first_dict["actions"][1]} {first_dict["actions"][2]}')

