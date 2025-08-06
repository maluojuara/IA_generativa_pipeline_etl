import extract
import transform
import requests


def update_user(user):
	url = extract.API_URL + "/users/" + str(user['id'])
	response = requests.put(url, json=user)
	if not (response.status_code == 200):
		return False
	return True

def execute_load(file_path):
	users = transform.execute_transform(file_path)

	for user in users:
		success = update_user(user)
		print(f"User {user['name']} updated? {success}!")
	
