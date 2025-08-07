import extract
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_message_ai(user):
	completion = openai.ChatCompletion.create(
		model="gpt-3.5-turbo",
		messages=[
			{"role": "system", "content": "You are a banking marketing expert"},
			{"role": "user", "content": f"Create a message for {user['name']} about \
			the importance of banking investiments (max 100 characters).\
			You must use the name of the person in the message and must not use emojis."}
		]
	)

	response_gpt = completion.choices[0].message.content.strip('\"')
	return response_gpt

def execute_transform(file_path):
	users = extract.execute_extract(file_path)

	for user in users:
		news = generate_message_ai(user)
		user.setdefault('news', []).append({
			"icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
			"description": news
		})
	return users
