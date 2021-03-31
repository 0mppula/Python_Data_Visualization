import requests

# Make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
limit_url = 'https://api.github.com/rate_limit'
r = requests.get(url)
r_2 = requests.get(limit_url)
print('Status code:', r.status_code)

# Store API response in a variable
response_dict = r.json()
print(f'Total repositories: {response_dict["total_count"]}')

# Explore information about the repositories
repo_dicts = response_dict['items']
print(f'Repositories returned: {len(repo_dicts)}')

# Examine the first repository
repo_dict = repo_dicts[0]

# Loop Through all repositories returned by API request
print('\nSelected information about each repository:')

for repo_dict in repo_dicts:
    print('\nName:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Created:', repo_dict['created_at'])
    print('Updated:', repo_dict['updated_at'])
    print('Desctiption:', repo_dict['description'])
