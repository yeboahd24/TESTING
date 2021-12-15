import requests

# Pulling repo from GitHub

# def pull_repo():
#     url = 'https://api.github.com/repos/yeboahd24/Django-Flutterwave/git/refs/heads/master'
#     response = requests.get(url)
#     response_json = response.json()
#     sha = response_json['object']['sha']
#     url = 'https://api.github.com/repos/yeboahd24/Django-Flutterwave/git/git/commits/' + sha
#     response = requests.get(url)
#     response_json = response.json()
    
# pull_repo()


# Pulling request from GitHub

# def pull_request():
#     url = 'https://api.github.com/repos/yeboahd24/Django-Flutterwave/pulls/1'
#     response = requests.get(url)
#     response_json = response.json()
#     print(response_json['user'])
    
# pull_request()




def full_email(people):
    results = []
    for email, name in people:
        results.append(f'{name} <{email}>')
        return results
    
people = [('linux@gmail.com', 'linux'), ('dominic@gmail.com', 'dominic'),]

print(full_email(people))