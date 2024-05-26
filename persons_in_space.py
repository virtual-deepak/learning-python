import requests 

response = requests.get("http://api.open-notify.org/astros.json")
json = response.json()

if json['message'] == 'success':
    print(f"As of today, there are {json['number']} people in space. Names below:")
    for person in json['people']:
        print(person['name'])