from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['PNEAgv5UbBRm646hA5fE690zNsF5yNk844Hh6BS-TUhW']
url = os.environ['https://api.us-south.language-translator.watson.cloud.ibm.com/instances/57c83b75-0421-43d6-b518-62ce417b4310']
authenticator= IAMAuthenticator(PNEAgv5UbBRm646hA5fE690zNsF5yNk844Hh6BS-TUhW)
language_translator=LanguageTranslatorV3(version='2018-05-01',authenticator=authenticator)
language_translator.set_service_url(https://api.us-south.language-translator.watson.cloud.ibm.com/instances/57c83b75-0421-43d6-b518-62ce417b4310)
def english_to_french(text1):
    frenchtranslation=language_translator.translate(text=text1,model_id='en-fr').get_result()
    return frenchtranslation.get("translations")[0].get("translation")

@app.route("/frenchToEnglish")
def french_to_english(text1):
    englishtranslation = language_translator.translate(text=text1,model_id='fr-en').get_result()
    return englishtranslation.get("translations"[0].get("translation"))

@app.route("/")
def renderIndexPage():
    # Write the code to render template

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
