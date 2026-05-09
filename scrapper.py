import requests as rq
from bs4 import BeautifulSoup as bs

url = 'https://www.python.org/jobs/'

print(f'Connecting to {url}...')
response = rq.get(url)

if response.status_code == 200:
    print('Success! Page downloaded.')

soup = bs(response.text, 'html.parser')

print(f'Page Title: {soup.title.text}\n')

print('Extracting jobs...')
job_list = soup.find('ol', class_='list-recent-jobs')

if job_list:
    jobs = job_list.find_all('li')
    print(f'Found {len(jobs)} jobs on the page.\n')

    print("Here are the first 5 jobs:")
    for job in jobs[:5]:
        title_element = job.find('h2').find('a') if job.find('h2') else None
        if title_element:
            print(f"- {title_element.text.strip()}")
else:
    print("Could not find the job list. The page structure might have changed.")