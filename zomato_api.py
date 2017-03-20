import requests
import csv
import json
import pandas as pd
import numpy as np
import difflib

## Load RestaurantMasterData into pandas
restaurant_list = pd.read_csv('RestaurantMasterData.csv', sep=None, engine='python')
restaurant_list.rename(columns={'brand': 'name'}, inplace=True)
# print(restaurant_list.head(n=5))
# print("Number of restaurants: " + str(len(restaurant_list)))

## Try loading json into Python with pandas
durban = pd.read_json('durban_flat.json')
capetown = pd.read_json('capetown_flat.json')
jozi = pd.read_json('johannesburg_flat.json')
# print(durban.head(n=5))

# Match to names in the original restuarant list
capetown_matches = pd.merge(restaurant_list, capetown, on='name', how='inner')
print(capetown_matches)
durban_matches = pd.merge(restaurant_list, durban, on='name', how='inner')
print(durban_matches)
jozi_matches = pd.merge(restaurant_list, jozi, on='name', how='inner')
print(jozi_matches)

## Search the Zomato API for a specific restaurant
# def z_search(query):
#     name = query.replace(' ', '%20')
#     payload = {'entity_id': '65', 'entity_type': 'city', 'q': name}
#     headers = {'user_key': '098dd6866a1b9f76cd02492617518666', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
#     url = 'https://developers.zomato.com/api/v2.1/search'
#     r = requests.get(url, params=payload, headers=headers)
#     print(r.content.decode())
#
# for name in restaurantNames:
#     z_search(name)
