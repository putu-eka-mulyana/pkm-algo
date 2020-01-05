import json
resultcount =[]
with open('datatest.json') as f:
    data = json.load(f)
    for i in data:
      if 'comments' in i.keys():
        databaru ={
          "img_urls":i['img_urls'],
          "comments":len(i['comments']),
          "datetime":i['datetime'],
          "caption":i['caption'],
          "likes":i['likes']
        }
      else:
        databaru ={
          "img_urls":i['img_urls'],
          "comments":0,
          "datetime":i['datetime'],
          "caption":i['caption'],
          "likes":i['likes']
        }      
      resultcount.append(databaru)

resultcount.sort(key=lambda x: x["comments"],reverse=True)
with open('hasil-sorting.json', 'w') as outfile:
    json.dump(resultcount, outfile)
topten=[]
for i in range(10):
   topten.append(resultcount[i])

with open('topten.json', 'w') as t:
    json.dump(topten, t)