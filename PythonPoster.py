import requests
import json

url = 'http://localhost:9999/api/pepper/add'
headers = {'Authorization' : 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJjb25uZWxsIiwiaWF0IjoxNTkxNzA5MzkwLCJleHAiOjE1OTE3NjkzOTB9.02FykKqnRJ6QZRKuMarIhkPjkJeX4zIT5rgSWmf-bstwPF39XWzNxBJ373lBvUPhrn9M1AOs8P7sc-5LxQsryA', 'Accept' : 'application/json', 'Content-Type' : 'application/json'}

with open('pepperList.json') as data_file:
    json_file = json.load(data_file)
    for pepper in json_file['peppers']:
        temp = json.dumps(pepper)
        # temp = str(pepper).replace('"','###').replace("'", '"').replace("###",'"')
        print(temp)
        r = requests.post(url, data=temp, headers=headers)
        print(r)

#json = '{"name" : "Devil Tongue","species" : "chinense","origin" : "Pennsylvania","shuMin" : "125,000","shuMax" : "325,000","imageURL" : "http://www.chileplanet.eu/schede/pepper/Devil%20Tongue.jpg","description" : "Devil Tongue: C. chinense. Variety from Pennsylvania. Its exact origins are unknown. It a kind of chili closely related to Habanero. It is believed to have originated from an Amish farmer who discovered him few decades ago amongst others grow Habanero. The fruits are similar to the variety Fatalii but with a skin smoother and more compact. Mature from green to red or golden yellow depending on the variety. 125.000 - 325.000 SHU."}'
#r = requests.post(url, data=json, headers=headers)
#print(r)