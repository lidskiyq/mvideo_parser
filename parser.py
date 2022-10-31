import requests
import json
from cookies import cookies, headers

def get_data():

	params = {
	    'categoryId': '118',
	    'offset': '0',
	    'limit': '24',
	    'filterParams': [
	        'WyJza2lka2EiLCIiLCJkYSJd',
	        'WyJ0b2xrby12LW5hbGljaGlpIiwiIiwiZGEiXQ==',
	    ],
	    'doTranslit': 'true',
	}

	response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies, headers=headers).json()

	#print(response)

	product_ids = response.get('body').get('products')

	with open('1_product_ids.json', 'w') as file:
		json.dump(product_ids, file, indent=4, ensure_ascii=False)

	#print(product_ids)

	json_data = {
	    'productIds': product_ids,
	    'mediaTypes': [
	        'images',
	    ],
	    'category': True,
	    'status': True,
	    'brand': True,
	    'propertyTypes': [
	        'KEY',
	    ],
	    'propertiesConfig': {
	        'propertiesPortionSize': 5,
	    },
	    'multioffer': False,
	}

	response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers, json=json_data).json()

	with open('2_items.json', 'w', encoding='utf-8') as file:
		json.dump(response, file, indent=4, ensure_ascii=False)

	#print(len(response.get('body').get('products')))

	product_ids_str = ','.join(product_ids)

	params = {
	    'productIds': product_ids_str,
	    'addBonusRubles': 'true',
	    'isPromoApplied': 'true',
	}

	response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies, headers=headers).json()

	with open('3_items.json', 'w', encoding='utf-8') as file:
		json.dump(response, file, indent=4, ensure_ascii=False)

	items_prices = {}

	material_prices = response.get('body').get('materialPrices')
	for item in material_prices:
		item_id = item.get('price').get('productId')
		item_base_price = item.get('price').get('basePrice')
		item_sale_price = item.get('price').get('salePrice')
		item_bonus = item.get('bonusRubles').get('total')
		items_prices[item_id] = { 
			'item_basePrice' : item_base_price,
			'item_salePrice' : item_sale_price,
			'item_bonus': item_bonus
		}

	with open("4_items_prices.json", 'w', encoding='utf-8') as file:
		json.dump(items_prices, file, indent=4, ensure_ascii=False)

def get_result():

	with open('2_items.json', encoding='utf-8') as file:
		product_data = json.load(file)

	with open('4_items_prices.json', encoding='utf-8') as file:
		product_prices = json.load(file)

	product_data = product_data.get('body').get('products')

	for item in product_data:
		product_id = item.get('productId')

		if product_id in product_prices:
			prices = product_prices[product_id]

		item['item_basePrice'] = prices.get('item_basePrice')
		item['item_salePrice'] = prices.get('item_salePrice')
		item['item_bonus'] = prices.get('item_bonus')

	with open('5_result.json', 'w', encoding = 'utf-8') as file:
		json.dump(product_data, file, indent = 4, ensure_ascii = False)

def main():
	get_data()
	get_result()

if __name__ == '__main__':
	main()

