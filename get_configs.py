import json

f = open('./config/config.json')

data = json.load(f)

token = data['bot_config'][0]['TOKEN']

prefix = data['bot_config'][0]['PREFIX']

guild = data['server_config'][0]['GUILD']

member_count_channel = data['server_config'][0]['member_count_channel']

ticket_channel = data['ticket_config'][0]['ticket_channel']

ticket_category = data['ticket_config'][0]['ticket_category']