# Text_to_Speech - Eden AI API
## Description
This repositery provides code to implement Eden AI Text-to-Speech API. Eden AI Text-to-Speech API allows to call Text-to-Speech APIs from multpile text-to-speech providers. It permits to get results from these providers, compare the results, siwtch between providers or combine them.

## What is Eden AI ?
[Eden AI](https://www.edanai.co/) is a SaaS providing APIs connected to big (AWS, GCP, etc.) and small AI providers for vision, text, audio, OCR, prediction and translation AI engines. Our solution allows users to compare the performance of these providers APIs according to their data and use them directly via our API thus offering great flexibility and making it very easy to change supplier. In particular, we offer better performance with the "Genius" feature that cleverly combines results from multiple providers.

Eden AI offers community offer (free) when you [create your account for free](https://app.edenai.run/user/login). You can then use [APIs](https://api.edenai.run/v1/redoc/), use the [interface](https://app.edenai.run/bricks/default), manage your account, access to cost management.

You can find APIs documentation here : https://api.edenai.run/v1/redoc/

## Usage
### Initialization
Enter your access token and select your API endpoint. You can get your token on your account manager [here](https://www.ai-compare.com/accounts/login/?next=/my_apis/my_account).
```python
import requests
headers = {  'Authorization': 'Bearer your API Key'}
url = 'https://api.edenai.run/v1/pretrained/audio/text_to_speech'
```
### Select parameters 
Set text to transcribe into audio, the language, the gender (optional), and providers APIs you want to run :
```python
payload = {'providers':'[\'ibm\', \'microsoft\', \'aws\', \'google_cloud\']','text':'Bonjour, je suis Martin','language':'fr-FR','option':'MALE'}
```
### Get results
```python
response = requests.request("POST", url, headers=headers, data = payload)
print(response.text.encode('utf8'))
```

## Response example
```json
{"result": [{"solution_name": "Google Cloud", "execution_time": "0.390108", "result": {"text": "I am very happy", "audio_path": "media/data/files/audio/texttospeech_fa2bfc86-fd10-40d0-a4f5-08ce679ba7a0/google_cloud.mp3", "voice_type": 1}, "status": "Success"}, {"solution_name": "Microsoft Azure", "execution_time": "1.252769", "result": {"text": "I am very happy", "audio_path": "media/data/files/audio/texttospeech_fa2bfc86-fd10-40d0-a4f5-08ce679ba7a0/microsoft.mp3", "voice_type": 1}, "status": "Success"}, {"solution_name": "Amazon Web Services", "execution_time": "0.229175", "result": {"text": "I am very happy", "audio_path": "media/data/files/audio/texttospeech_fa2bfc86-fd10-40d0-a4f5-08ce679ba7a0/amazon_web_service.mp3", "voice_type": 1}, "status": "Success"}, {"solution_name": "IBM Watson", "execution_time": "1.352666", "result": {"text": "I am very happy", "audio_path": "media/data/files/audio/texttospeech_fa2bfc86-fd10-40d0-a4f5-08ce679ba7a0/ibm.mp3", "voice_type": 1}, "status": "Success"}]}
```

## Blog articles
We provides on our website some [blog articles on AI engines](https://www.edenai.co/blog)

## Contact
If you have any question or request, you can contact us at contact@edenai.com

## Terms of use
You can access to our terms [here](https://www.edenai.co/terms) on our website.

#
![Screenshot](https://github.com/ai-compare/Speech_to_text-API/blob/ba9d4f1668d8758141f24240d1287640b4211c63/Logo%20complet%20Eden%20AI%20-%20format%20PNG.png)
