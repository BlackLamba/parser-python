from parser import fetch_vacancies
from storage import save_to_json
from analysis import filter_by_keyword, filter_by_salary
from visualize import plot_city_distribution, plot_salary_distribution

# Получаем 5 страниц вакансий по запросу "python junior"
vacancies = fetch_vacancies(pages=5, area_list=[1,2], text="python junior")

# Сохраняем в файл
save_to_json(vacancies, "vacancies.json")

filtered = filter_by_keyword(vacancies, keyword="python")
filtered_salary = filter_by_salary(vacancies, salary_min=10000)

# Рисуем график по городам
plot_city_distribution(filtered)
plot_salary_distribution(filtered_salary)