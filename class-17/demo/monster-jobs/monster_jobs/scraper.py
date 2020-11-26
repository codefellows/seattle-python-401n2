"""
Walk through of https://realpython.com/beautiful-soup-web-scraper-python/
"""

###############
# step 1
###############

# import requests

# URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
# page = requests.get(URL)

# print(page.content)


###############
# step 2
###############

# # Move import to top of course
# from bs4 import BeautifulSoup

# soup = BeautifulSoup(page.content, 'html.parser')


###############
# step 3
###############

# results = soup.find(id="ResultsContainer")

# # print(results.prettify())


###############
# step 4
###############

# job_elems = results.find_all('section', class_='card-content')

# print(job_elems)


###############
# step 5
###############

# for job_elem in job_elems:
#     print(job_elem, end='\n'*2)


###############
# step 6
###############

# for job_elem in job_elems:
#     # Each job_elem is a new BeautifulSoup object.
#     # You can use the same methods on it as you did before.
#     title_elem = job_elem.find('h2', class_='title')
#     company_elem = job_elem.find('div', class_='company')
#     location_elem = job_elem.find('div', class_='location')
#     print(title_elem)
#     print(company_elem)
#     print(location_elem)
#     print()

###############
# step 7
###############

# for job_elem in job_elems:
#     title_elem = job_elem.find('h2', class_='title')
#     company_elem = job_elem.find('div', class_='company')
#     location_elem = job_elem.find('div', class_='location')
#     print(title_elem.text)
#     print(company_elem.text)
#     print(location_elem.text)
#     print()


###############
# step 8
###############

# # note the use of and for safe access
# for job_elem in job_elems:
#     title_elem = job_elem.find('h2', class_='title')
#     company_elem = job_elem.find('div', class_='company')
#     location_elem = job_elem.find('div', class_='location')
#     print(title_elem and title_elem.text)
#     print(company_elem and company_elem.text)
#     print(location_elem and location_elem.text)
#     print()


###############
# step 9 - alternate way to prevent error
###############

# for job_elem in job_elems:
#     title_elem = job_elem.find('h2', class_='title')
#     company_elem = job_elem.find('div', class_='company')
#     location_elem = job_elem.find('div', class_='location')
#     if None in (title_elem, company_elem, location_elem):
#         continue
#     print(title_elem.text.strip())
#     print(company_elem.text.strip())
#     print(location_elem.text.strip())
#     print()


###############
# step 10
###############

# python_jobs = results.find_all('h2', string='Python Developer')
# print(python_jobs)


###############
# step 11
###############

# python_jobs = results.find_all('h2',
#                                string=lambda text: 'python' in text.lower())

# print(len(python_jobs))


###############
# step 12
###############

# for p_job in python_jobs:
#     link = p_job.find('a')['href']
#     print(p_job.text.strip())
#     print(f"Apply here: {link}\n")
