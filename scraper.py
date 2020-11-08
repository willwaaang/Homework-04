import requests
from bs4 import BeautifulSoup

keyword='dog'
page_number='5'
results = []


for i in range(1,11):
    #r = requests.get('https://www.ebay.com/sch/i.html?_nkw='+keyword)
    r = requests.get('https://www.ebay.com/sch/i.html?_nkw='+keyword+'&_pgn='+str(i))
    print('r.status_code',r.status_code)

    soup = BeautifulSoup(r.text, 'html.parser')

    '''
    items = soup.select('.s-item__title')
    for item in items:
        print('item=',item.text)

    prices = soup.select('.s-item__price')
    for price in prices:
        print('price=',price.text)
    ''' 

    # boxboxboxboxboxbox
    boxes = soup.select('.clearfix.srp-list.srp-results > li.s-item')
    for box in boxes:
        #print('---')
        result = {}
        # items item items ITEMStems item items ITEMStems item items ITEMStems item items ITEMStems item items ITEMStems item items ITEMStems item items ITEMStems item items ITEMStems item items ITEMStems item items ITEMStems item items ITEMStems item items ITEMStems item items ITEMStems item items ITEMS 
        titles = box.select('.s-item__title')
        for title in titles:
            #print('title=',title.text)
            result['title'] = title.text
        # prices prices
        prices = box.select('.s-item__price')
        for price in prices:
            #print('price=',price.text) 
            result['price'] = price.text
        #print('result=',result)
        results.append(result)
        # statuses sna stuff
        statuses = ()
        for status in statuses:
            #print ('status=',status.text)
            result['status'] = status.text
        #print('result=',result)
        results.append(result)

    print('len(results)=',len(results))

# asdbfasdfklsdhfkasldfh
import json 
j = json.dumps(results)
with open('items.json','w') as f:
    f.write(j)
#print('j=',j)