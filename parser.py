import requests

def fetch_vacancies(pages, text, area_list=None):
	all_vacancies = []

	if area_list is None:
		area_list = [1]

	for area in area_list:
		for page in range(pages):
			params = {
				"area" : area,
				"text" : text,
				"per_page" : 20,
				"page" : page,
			}

			r = requests.get("https://api.hh.ru/vacancies", params=params)
			data = r.json()
			all_vacancies.extend(data.get('items', []))
	return all_vacancies