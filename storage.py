import json
import pandas as pd

# Сохранение вакансий в json.
def save_to_json(data, path):
	with open(path, 'w', encoding='utf-8') as f:
		json.dump(data, f, ensure_ascii=False, indent=4)

# Сохранение вакансий в csv.
def save_to_csv(data, path):
	df = pd.json_normalize(data) # превращаем список словарей в таблицу.
	df.to_csv(path, index=False)