# Text_to_Speech - AI-Compare API
## Description
This repositery provides code to implement [AI-Compare Text-to-Speech API](https://www.ai-compare.com/audio_apis/text_to_speech). [AI-Compare Text-to-Speech API](https://www.ai-compare.com/audio_apis/text_to_speech) allows to call Text-to-Speech APIs from Google Cloud Platform Speech API, AWS Transcribe, Microsoft Azure Cognitives Services Speech, and IBM Watson Text-to-Speech. It permits to get results from these providers and compare the results.

## What is AI-Compare ?
[AI-Compare](https://www.ai-compare.com/) is a SaaS providing APIs connected to big (AWS, GCP, etc.) and small AI providers: [object detection](https://www.ai-compare.com/vision_apis/object_detection), [OCR](https://www.ai-compare.com/vision_apis/ocr), [NLP](https://www.ai-compare.com/text_apis/sentiment_analysis/), [speech-to-text](https://www.ai-compare.com/audio_apis/speech_recognition), custom vision, etc. Our solution allows users to compare the performance of these providers APIs according to their data and use them directly via our API thus offering great flexibility and making it very easy to change supplier. In particular, we offer better performance with the "Genius" feature that cleverly combines results from multiple providers.

AI-Compare offers 2$ free credits when you [create your account for free](https://www.ai-compare.com/accounts/login/?next=/my_apis). You can then use [APIs](https://www.ai-compare.com/v1/redoc/), use the [interface](https://www.ai-compare.com/my_apis), manage your account and have access to all the APIs.

You can find APIs documentation here : https://www.ai-compare.com/v1/redoc/

## Usage
### Initialization
Enter your access token and select your API endpoint. You can get your token on your account manager [here](https://www.ai-compare.com/accounts/login/?next=/my_apis/my_account).
```python
import requests
headers = {  'Authorization': 'Bearer your API Key'}
url = 'https://www.ai-compare.com/v1/pretrained/audio/text_to_speech'
```
### Select parameters 
Set text to transcribe into audio, the language, the gender (optional), and providers APIs you want to run :
```python
payload = {'providers':'[\'ibm\', \'cognitives_service\', \'aws\', \'google_cloud\']','text':'Bonjour, je suis Martin','language':'fr-FR','option':'MALE'}
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

## FAQ
Here you can access to AI-Compare [FAQ](https://www.ai-compare.com/faq/).

## Use cases
We provides on our website some [use cases examples for audio APIs](https://www.ai-compare.com/use_cases_audio/)

## Contact
If you have any question or request, you can contact us at contact@ai-compare.com

## Terms of use
You can access to our terms [here](https://www.ai-compare.com/terms/) on our website.

#
![Screenshot](Ai-compare_new.png)
