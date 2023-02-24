import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

def english_to_french(english_text):
    #write the code here
    if english_text is None :
        return ''
    french_text_dict = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()

    french_text=french_text_dict['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    #write the code here
    if french_text is None:
        return ''
    english_text_dict = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    english_text=english_text_dict['translations'][0]['translation']

    return english_text

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version='2018-05-01'

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=version,
    authenticator=authenticator
)

language_translator.set_service_url(url)