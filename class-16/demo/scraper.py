import requests
from bs4 import BeautifulSoup

url = 'https://www.monster.com/jobs/search/?q=Software-Engineer&where=seattle'

response = requests.get(url)
# print(response.content)
# print (dir(response))
# print(response.headers)

content = response.content
# print(content)

soup = BeautifulSoup(content, 'html.parser')
# print(soup)
# print(dir(soup))
# print(soup.prettify())

result = soup.find(id='SearchResults')
# print(result)
# print(result.prettify())

job_results = result.find_all('section', class_='card-content')
# print(len(job_results))

# print(job_results[2])

# for job in job_results:
#     # print(job, end='\n' *3)
#     title = job.find('h2', class_='title')
#     company = job.find('div', class_='company')
#     location = job.find('div', class_='location')
#     if None in (title, company, location):
#         continue
#     print(title.text.strip())
#     print(company.text.strip())
#     print(location.text.strip())
#     print()

final_result = []

for jobs in job_results:
    job_dict = {}
    if jobs.find('h2', class_='title'):
        title = jobs.find('h2', class_='title').text.strip()
        job_dict['title']  = title
        location = jobs.find('div', class_='location').text.strip()
        job_dict['location'] = location
        company = jobs.find('div', class_='company').text.strip()
        job_dict['company'] =company

        final_result.append(job_dict)

print(final_result)