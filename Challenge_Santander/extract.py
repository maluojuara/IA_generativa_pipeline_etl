import pandas as pd
import requests
import json

API_URL = "https://sdw-2023-prd.up.railway.app"

def execute_extract(file_path):
	data_frame = pd.read_csv(file_path)
	users_id = data_frame["UserID"].tolist()
	users = []

	def get_user(id):
		response = requests.get(API_URL + "/users/" + str(id))
		if not (response.status_code == 200):
			return None
		return response.json()

	for id in users_id:
		user = get_user(id)
		if user is not None:
			users.append(user)
	
	return users
