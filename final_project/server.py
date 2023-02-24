from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    result=translator.english_to_french(textToTranslate)
    output="Translated text to French:"  + textToTranslate + " -->" + result 
    return output

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    result = translator.french_to_english(textToTranslate)
    output="Translated text to French:"  + textToTranslate + " -->" + result 
    return output

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return 'hello'
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8088)
