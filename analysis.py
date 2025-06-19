def filter_by_keyword(vacancies, keyword):
	result = []

	for v in vacancies:
		requirements = v['snippet'].get('requirement') or ""

		if keyword.lower() in requirements.lower():
			result.append(v)

	return result

def filter_by_salary(vacancies, salary_min):
	result = []

	for v in vacancies:
		salary_data = v.get('salary')
		if not salary_data:
			continue

		salary_from = salary_data.get('from')
		if salary_from and salary_from >= salary_min:
			result.append(v)

	return result

def extract_salaries(vacancies):
	salaries = []
	for v in vacancies:
		salary = v.get('salary')
		if salary and salary.get('from'):
			salaries.append(salary['from'])

	return salaries