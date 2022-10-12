import requests
from bs4 import BeautifulSoup
import pandas as pd

city = input("Enter your City: ")
restaurants = []
cuisine = []
ratings = []
delivery_time = []
cost = []
offers = []
links = []
address = []
for i in range(9):
	url = 'https://www.swiggy.com/city/' + city + '/top-rated-collection?page='+str(2)
	header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}

	response = requests.get(url, headers = header)
	html = response.text



	soup = BeautifulSoup(html, 'html.parser')
	print(soup.title.text)
	print('-------------------------------------')

	top_res = soup.find('div', class_= "_129-b")
	list_tr = top_res.find_all('div', class_ = "_3XX_A")


	

	for tr in list_tr:
		name = tr.find(class_= "nA6kb").text

		link = tr.find('a')
		links.append(link.get('href'))
		for x in links:
			response1 = requests.get("https://www.swiggy.com" + x, headers = header)
			html1 = response1.text
			soup1 = BeautifulSoup(html1, 'html.parser')
			add = soup1.find('div', class_= "_396MD").text
			address.append(add)

		all_in_one = tr.find(class_ = "_3Mn31").text

		cuis = tr.find( class_= "_1gURR").text

		offer = tr.find( class_= "sNAfh").text

		restaurants.append(name)
		cuisine.append(cuis)
		ratings.append(all_in_one[0:3])
		delivery_time.append(all_in_one[4:11])
		cost.append(all_in_one[13:25])
		offers.append(offer)
		
		

	print(restaurants)
	print(cuisine)
	print(ratings)
	print(delivery_time)
	print(cost)
	print(offers)
	#print(links)
	print(address)
	# header = ['Restaurants', 'Cuisine', 'Ratings', 'Delivery Time','Cost for 2', 'Offers', 'Address']
	# indices = [i for i in range(1, len(restaurants)+1)]
	# all_rests = zip(restaurants, cuisine, ratings, delivery_time, cost, offers, address)
	# dt = pd.DataFrame(list(all_rests), columns = header, index = indices)
	# dt.to_csv('Top Restaurants in ' + city +'.csv')
	# print(dt)


