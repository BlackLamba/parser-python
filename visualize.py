import matplotlib.pyplot as plt
from collections import Counter
from analysis import extract_salaries

def plot_city_distribution(vacancies, top_n=10):
	cities = [v['area']['name'] for v in vacancies]
	counts = Counter(cities).most_common(top_n)

	labels, values = zip(*counts)

	plt.bar(labels, values)
	plt.xticks(rotation=15)
	plt.title('Где больше всего вакансий')
	plt.tight_layout()
	plt.show()

def plot_salary_distribution(vacancies):
	salaries = extract_salaries(vacancies)

	if not salaries:
		print('Нет данных о зарплатах для построения графика')
		return

	plt.hist(salaries, bins=10, color='skyblue', edgecolor='black')
	plt.title('Распределение зарплата (от)')
	plt.xlabel('Зарплата, RUB')
	plt.ylabel('Количество вакансий')
	plt.tight_layout()
	plt.show()


