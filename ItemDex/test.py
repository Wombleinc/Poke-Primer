from Item import Item
import items_list

url = 'https://pokeapi.co/api/v2/item/?limit=1607'
data = items_list.request_data(url)
for i in data['results']:
    print(Item(i['url']))
