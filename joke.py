import requests

def random_joke():
    joke = requests.get('https://geek-jokes.sameerkumar.website/api')
    return joke.text

print(random_joke())

