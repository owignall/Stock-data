from bs4 import BeautifulSoup
import requests


def data_fetch(code):
	code = code.upper()
	source = requests.get('https://uk.finance.yahoo.com/quote/%s?' %(code)).text
	soup = BeautifulSoup(source, 'lxml')
	quote_header = soup.find(id = 'quote-header-info')
	div = quote_header.find(class_='My(6px) Pos(r) smartphone_Mt(6px)').div
	data_dict = {}
	pdata = div.find_all('span')
	data_dict.update({'Live_price' : pdata[0].text})
	data_dict.update({'Change' : pdata[1].text})
	tables = soup.find_all('table')
	table_number = 1
	for table in tables:
		if table_number >= 3:
			break
		dps = table.find_all('td')
		dp_index = 0
		for dp in dps:
			if dp_index % 2 == 0:
				key = dp.span.text.replace("(","").replace(")","").replace(" ", "_").replace("'", "_").replace("-", "_").replace("&", "and").replace("", "")
				try:
					value = dps[dp_index+1].span.text
				except Exception as e:
					value = "(Not found)"
				data_dict.update({key : value})
			dp_index += 1
		table_number += 1
	# # Print data to console
	# for key,value in data_dict.items():
	# 	print('%s : %s' %(key, value))
	# print('__________________')
	# Return collected stock data
	return data_dict