import requests
import json

url = "https://michaelgathara.com/api/python-challenge"

response = requests.get(url)

challenges = response.json()
print("Name : Rikitha Rudrangi , BlazerId : rudrangi")
for i in challenges:
    problem_field = i['problem']
    problem_field_no_qmark = problem_field.replace('?','')
    print("ID : ", i['id'], "Problem : ", eval(problem_field_no_qmark))