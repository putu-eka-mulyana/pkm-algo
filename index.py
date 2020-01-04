import json

with open('data.json') as f:
    data = json.load(f)
    for i in data:
      print('======================')
      print('commit ', len(i['comments']))
      print('like ', i['likes']) 
      print(i['img_urls'])
      print('======================')
# print(len(data))