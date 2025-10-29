import requests

# data = {
#     'title': 'Buy groceries',
# 	'description': 'Milk, eggs, bread'
#     }

# res = requests.post('http://127.0.0.1:5000/tasks', json=data)

# print('Status: ', res.status_code)
# print('Response: ', res.json())


data = {
	'description': 'Milk, bread, Juice'
    }

res = requests.put('http://127.0.0.1:5000/tasks/4', json=data)

print('Status: ', res.status_code)
print('Response: ', res.json())
