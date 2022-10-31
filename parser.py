import requests
import json

def get_data():

	cookies = {
    'CACHE_INDICATOR': 'false',
    'COMPARISON_INDICATOR': 'false',
    'HINTS_FIO_COOKIE_NAME': '1',
    'MVID_AB_PDP_CHAR': '2',
    'MVID_AB_SERVICES_DESCRIPTION': 'var4',
    'MVID_AB_TOP_SERVICES': '1',
    'MVID_BLACK_FRIDAY_ENABLED': 'true',
    'MVID_CALC_BONUS_RUBLES_PROFIT': 'false',
    'MVID_CART_AVAILABILITY': 'true',
    'MVID_CART_MULTI_DELETE': 'false',
    'MVID_CATALOG_STATE': '1',
    'MVID_CITY_ID': 'CityCZ_1638',
    'MVID_CREDIT_AVAILABILITY': 'true',
    'MVID_CRITICAL_GTM_INIT_DELAY': '3000',
    'MVID_FILTER_CODES': 'true',
    'MVID_FILTER_TOOLTIP': '1',
    'MVID_FLOCKTORY_ON': 'true',
    'MVID_GEOLOCATION_NEEDED': 'true',
    'MVID_GET_LOCATION_BY_DADATA': 'DaData',
    'MVID_GIFT_KIT': 'true',
    'MVID_GLC': 'true',
    'MVID_GLP': 'true',
    'MVID_GUEST_ID': '21731484973',
    'MVID_HANDOVER_SUMMARY': 'true',
    'MVID_IS_NEW_BR_WIDGET': 'true',
    'MVID_KLADR_ID': '7800000000000',
    'MVID_LAYOUT_TYPE': '1',
    'MVID_LP_SOLD_VARIANTS': '3',
    'MVID_MCLICK': 'true',
    'MVID_MINDBOX_DYNAMICALLY': 'true',
    'MVID_MINI_PDP': 'true',
    'MVID_MOBILE_FILTERS': 'true',
    'MVID_NEW_ACCESSORY': 'true',
    'MVID_NEW_DESKTOP_FILTERS': 'true',
    'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
    'MVID_NEW_LK_OTP_TIMER': 'true',
    'MVID_NEW_MBONUS_BLOCK': 'true',
    'MVID_PROMO_CATALOG_ON': 'true',
    'MVID_REGION_ID': '6',
    'MVID_REGION_SHOP': 'S904',
    'MVID_SERVICES': '111',
    'MVID_SERVICES_MINI_BLOCK': 'var2',
    'MVID_TIMEZONE_OFFSET': '3',
    'MVID_WEBP_ENABLED': 'true',
    'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
    'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'false',
    'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
    'SENTRY_ERRORS_RATE': '0.1',
    'SENTRY_TRANSACTIONS_RATE': '0.5',
    'flacktory': 'no',
    'searchType2': '3',
    '_gid': 'GA1.2.1651130032.1666978319',
    '_ym_uid': '1666978325181824906',
    '_ym_d': '1666978325',
    '_sp_ses.d61c': '*',
    '_ym_isad': '1',
    'partnerSrc': 'yandex',
    'admitad_uid': '%D0%BC%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE',
    'utm_term': '%D0%BC%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE',
    '__SourceTracker': 'yandex__cpc',
    'admitad_deduplication_cookie': 'yandex__cpc',
    '__cpatrack': 'yandex_cpc',
    '__sourceid': 'yandex',
    '__allsource': 'yandex',
    'SMSError': '',
    'authError': '',
    'tmr_lvid': '6dca98f7a6e7d8712e482a4f865f8373',
    'tmr_lvidTS': '1666978327466',
    'advcake_track_id': '5e372748-20ba-6506-6394-15c5f10ca842',
    'advcake_session_id': 'f8726deb-8f6d-0bf3-ad43-f7ff93defbf3',
    'advcake_track_url': 'https%3A%2F%2Fwww.mvideo.ru%2F%3Futm_source%3Dyandex%26utm_medium%3Dcpc%26utm_campaign%3Dipr_Spb_Image_Name_Pure_search_desktop%26utm_content%3Dpid%7C21914267954_21914267954%7Ccid%7C54501639%7Cgid%7C4285483795%7Caid%7C9547781183%7Cpos%7Cpremium1%7Ckey%7C%25D0%25BC%25D0%25B2%25D0%25B8%25D0%25B4%25D0%25B5%25D0%25BE%7Caddphrases%7Cno%7Cdvc%7Cdesktop%7Cregion%7C2%7Cregion_name%7C%25D0%25A1%25D0%25B0%25D0%25BD%25D0%25BA%25D1%2582-%25D0%259F%25D0%25B5%25D1%2582%25D0%25B5%25D1%2580%25D0%25B1%25D1%2583%25D1%2580%25D0%25B3%7Ccoef_goal%7C0%7Cdesktop%26utm_term%3D%25D0%25BC%25D0%25B2%25D0%25B8%25D0%25B4%25D0%25B5%25D0%25BE%26reff%3Dyandex_cpc_ipr_Spb_Image_Name_Pure_Search%26etext%3D2202.xSgOKrlKEs4y2QLMw2K113hjcHV6d3Z0cnJ2bGZ4dHc.83b3419dc985554977636bc2b54da765a9e1104b%26_openstat%3DZGlyZWN0LnlhbmRleC5ydTs1NDUwMTYzOTs5NTQ3NzgxMTgzO3lhbmRleC5ydTpwcmVtaXVt%26yclid%3D6380981208989884913',
    'advcake_utm_partner': 'ipr_Spb_Image_Name_Pure_search_desktop',
    'advcake_utm_webmaster': 'pid%7C21914267954_21914267954%7Ccid%7C54501639%7Cgid%7C4285483795%7Caid%7C9547781183%7Cpos%7Cpremium1%7Ckey%7C%25D0%25BC%25D0%25B2%25D0%25B8%25D0%25B4%25D0%25B5%25D0%25BE%7Caddphrases%7Cno%7Cdvc%7Cdesktop%7Cregion%7C2%7Cregion_name%7C%25D0%25A1%25D0%25B0%25D0%25BD%25D0%25BA%25D1%2582-%25D0%259F%25D0%25B5%25D1%2582%25D0%25B5%25D1%2580%25D0%25B1%25D1%2583%25D1%2580%25D0%25B3%7Ccoef_goal%7C0%7Cdesktop',
    'advcake_click_id': '',
    'uxs_uid': '7258c340-56e6-11ed-b96a-43d830e24617',
    'flocktory-uuid': 'a682a9ca-81ff-4605-9314-b831b23f608c-8',
    'BIGipServeratg-ps-prod_tcp80': '1912921098.20480.0000',
    'bIPs': '155255760',
    'afUserId': 'f60e3f6a-e93c-45c0-b733-321ebe1ab44e-p',
    'AF_SYNC': '1666978328969',
    '_ga': 'GA1.2.1611458591.1666978319',
    'tmr_detect': '1%7C1666978356500',
    'MVID_ENVCLOUD': 'prod1',
    '__lhash_': 'c413a288ac85dfdbbaa9c5a47f5fe07d',
    '_dc_gtm_UA-1873769-1': '1',
    '_dc_gtm_UA-1873769-37': '1',
    '_sp_id.d61c': '3dd2b0cc-cb24-4c60-b0f1-39408aa2daa3.1666978325.1.1666978540..109e17dc-b59b-423f-a754-eed0bdc39c75..6017004e-5ccb-4695-8083-0113c37dd581.1666978325479.26',
    'tmr_reqNum': '25',
    'JSESSIONID': 'psVDjcTRvrsMDFSNMmJkKt8J9m98JmpvTRbN0Hf7kKGG91JbyYYM!-2021553668',
    '_ga_CFMZTSS5FM': 'GS1.1.1666978319.1.1.1666978578.0.0.0',
    '_ga_BNX5WPP3YK': 'GS1.1.1666978319.1.1.1666978578.60.0.0',
	}

	headers = {
	    'authority': 'www.mvideo.ru',
	    'accept': 'application/json',
	    'accept-language': 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
	    'baggage': 'sentry-transaction=%2F,sentry-public_key=1e9efdeb57cf4127af3f903ec9db1466,sentry-trace_id=a4811687d17d4fabafdc61e2b8643ee2,sentry-sample_rate=0%2C5',
	    # Requests sorts cookies= alphabetically
	    # 'cookie': 'CACHE_INDICATOR=false; COMPARISON_INDICATOR=false; HINTS_FIO_COOKIE_NAME=1; MVID_AB_PDP_CHAR=2; MVID_AB_SERVICES_DESCRIPTION=var4; MVID_AB_TOP_SERVICES=1; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CALC_BONUS_RUBLES_PROFIT=false; MVID_CART_AVAILABILITY=true; MVID_CART_MULTI_DELETE=false; MVID_CATALOG_STATE=1; MVID_CITY_ID=CityCZ_1638; MVID_CREDIT_AVAILABILITY=true; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GET_LOCATION_BY_DADATA=DaData; MVID_GIFT_KIT=true; MVID_GLC=true; MVID_GLP=true; MVID_GUEST_ID=21731484973; MVID_HANDOVER_SUMMARY=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=7800000000000; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MINDBOX_DYNAMICALLY=true; MVID_MINI_PDP=true; MVID_MOBILE_FILTERS=true; MVID_NEW_ACCESSORY=true; MVID_NEW_DESKTOP_FILTERS=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PROMO_CATALOG_ON=true; MVID_REGION_ID=6; MVID_REGION_SHOP=S904; MVID_SERVICES=111; MVID_SERVICES_MINI_BLOCK=var2; MVID_TIMEZONE_OFFSET=3; MVID_WEBP_ENABLED=true; NEED_REQUIRE_APPLY_DISCOUNT=true; PRESELECT_COURIER_DELIVERY_FOR_KBT=false; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; flacktory=no; searchType2=3; _gid=GA1.2.1651130032.1666978319; _ym_uid=1666978325181824906; _ym_d=1666978325; _sp_ses.d61c=*; _ym_isad=1; partnerSrc=yandex; admitad_uid=%D0%BC%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE; utm_term=%D0%BC%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE; __SourceTracker=yandex__cpc; admitad_deduplication_cookie=yandex__cpc; __cpatrack=yandex_cpc; __sourceid=yandex; __allsource=yandex; SMSError=; authError=; tmr_lvid=6dca98f7a6e7d8712e482a4f865f8373; tmr_lvidTS=1666978327466; advcake_track_id=5e372748-20ba-6506-6394-15c5f10ca842; advcake_session_id=f8726deb-8f6d-0bf3-ad43-f7ff93defbf3; advcake_track_url=https%3A%2F%2Fwww.mvideo.ru%2F%3Futm_source%3Dyandex%26utm_medium%3Dcpc%26utm_campaign%3Dipr_Spb_Image_Name_Pure_search_desktop%26utm_content%3Dpid%7C21914267954_21914267954%7Ccid%7C54501639%7Cgid%7C4285483795%7Caid%7C9547781183%7Cpos%7Cpremium1%7Ckey%7C%25D0%25BC%25D0%25B2%25D0%25B8%25D0%25B4%25D0%25B5%25D0%25BE%7Caddphrases%7Cno%7Cdvc%7Cdesktop%7Cregion%7C2%7Cregion_name%7C%25D0%25A1%25D0%25B0%25D0%25BD%25D0%25BA%25D1%2582-%25D0%259F%25D0%25B5%25D1%2582%25D0%25B5%25D1%2580%25D0%25B1%25D1%2583%25D1%2580%25D0%25B3%7Ccoef_goal%7C0%7Cdesktop%26utm_term%3D%25D0%25BC%25D0%25B2%25D0%25B8%25D0%25B4%25D0%25B5%25D0%25BE%26reff%3Dyandex_cpc_ipr_Spb_Image_Name_Pure_Search%26etext%3D2202.xSgOKrlKEs4y2QLMw2K113hjcHV6d3Z0cnJ2bGZ4dHc.83b3419dc985554977636bc2b54da765a9e1104b%26_openstat%3DZGlyZWN0LnlhbmRleC5ydTs1NDUwMTYzOTs5NTQ3NzgxMTgzO3lhbmRleC5ydTpwcmVtaXVt%26yclid%3D6380981208989884913; advcake_utm_partner=ipr_Spb_Image_Name_Pure_search_desktop; advcake_utm_webmaster=pid%7C21914267954_21914267954%7Ccid%7C54501639%7Cgid%7C4285483795%7Caid%7C9547781183%7Cpos%7Cpremium1%7Ckey%7C%25D0%25BC%25D0%25B2%25D0%25B8%25D0%25B4%25D0%25B5%25D0%25BE%7Caddphrases%7Cno%7Cdvc%7Cdesktop%7Cregion%7C2%7Cregion_name%7C%25D0%25A1%25D0%25B0%25D0%25BD%25D0%25BA%25D1%2582-%25D0%259F%25D0%25B5%25D1%2582%25D0%25B5%25D1%2580%25D0%25B1%25D1%2583%25D1%2580%25D0%25B3%7Ccoef_goal%7C0%7Cdesktop; advcake_click_id=; uxs_uid=7258c340-56e6-11ed-b96a-43d830e24617; flocktory-uuid=a682a9ca-81ff-4605-9314-b831b23f608c-8; BIGipServeratg-ps-prod_tcp80=1912921098.20480.0000; bIPs=155255760; afUserId=f60e3f6a-e93c-45c0-b733-321ebe1ab44e-p; AF_SYNC=1666978328969; _ga=GA1.2.1611458591.1666978319; tmr_detect=1%7C1666978356500; MVID_ENVCLOUD=prod1; __lhash_=c413a288ac85dfdbbaa9c5a47f5fe07d; _dc_gtm_UA-1873769-1=1; _dc_gtm_UA-1873769-37=1; _sp_id.d61c=3dd2b0cc-cb24-4c60-b0f1-39408aa2daa3.1666978325.1.1666978540..109e17dc-b59b-423f-a754-eed0bdc39c75..6017004e-5ccb-4695-8083-0113c37dd581.1666978325479.26; tmr_reqNum=25; JSESSIONID=psVDjcTRvrsMDFSNMmJkKt8J9m98JmpvTRbN0Hf7kKGG91JbyYYM!-2021553668; _ga_CFMZTSS5FM=GS1.1.1666978319.1.1.1666978578.0.0.0; _ga_BNX5WPP3YK=GS1.1.1666978319.1.1.1666978578.60.0.0',
	    'referer': 'https://www.mvideo.ru/noutbuki-planshety-komputery-8/noutbuki-118/f/skidka=da/tolko-v-nalichii=da',
	    'sec-ch-ua': '"Chromium";v="106", "Microsoft Edge";v="106", "Not;A=Brand";v="99"',
	    'sec-ch-ua-mobile': '?0',
	    'sec-ch-ua-platform': '"Windows"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'sentry-trace': 'a4811687d17d4fabafdc61e2b8643ee2-9b389f2c2456b6c0-0',
	    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52',
	    'x-set-application-id': '78715b70-771d-4f59-9690-98f3463e40d9',
	}

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

