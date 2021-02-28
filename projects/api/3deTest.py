import requests
import json

# api-endpoint
response = requests.get("https://epistat.sciensano.be/Data/COVID19BE_CASES_AGESEX.json")
items = response.json()

# load the json data


# # Input the item name that you want to search
# item = input("Enter an item name:\n")
#
#
# # # Define a function to search the item
# def search_price(name):
#     for keyval in items:
#         if name.lower() == keyval['PROVINCE'].lower():
#             return keyval['CASES']
# #
# #
# # # Check the return value and print message
# if (search_price(item) != None):
#     print("there is/are", search_price(item), 'case')
# else:
#     print("Item is not found")






# Search data based on key and value using filter and list method
all = list(filter(lambda x: (x["PROVINCE"] if "PROVINCE" in x else None) == "OostVlaanderen", items))
total = 0
i=0
for case in all:
    i+=1
    total += case['CASES']
print (total)

avg_value = total / i
print(round(avg_value,2))
# print(list(filter(lambda x: (x["PROVINCE"] if "PROVINCE" in x else None) == "Brussels",items)))
