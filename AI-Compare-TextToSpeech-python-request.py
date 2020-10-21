import requests

# You can find the documentation here : https://www.ai-compare.com/v1/redoc/#operation/Text%20To%20Speech

#Enter your API Token
headers = {'Authorization': 'Bearer your API Key'} #You can get your free API token here https://www.ai-compare.com/accounts/login/?next=/my_apis

# Select API
url = 'https://www.ai-compare.com/v1/pretrained/audio/text_to_speech'

# Select providers, and audio to transcribe
payload = {'providers':'[\'ibm\', \'cognitives_service\', \'aws\', \'google_cloud\']','text':'Hi, my name is Martin','language':'en-US', 'option':'MALE'}

# Request to AI COMPARE
response = requests.request("POST", url, headers=headers, data = payload)

# Print result
print(response.text.encode('utf8'))
