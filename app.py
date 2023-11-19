from flask import Flask, render_template, url_for, request, jsonify
from sentiment_analysis import *

app = Flask(__name__)

text=""
predicted_emotion=''
predicted_emotion_img_url=''
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict-emotion', methods=["POST"])
def predict_emotion():
    
    # Get Input Text from POST Request
    input_text=request.json.get("text")
    print("Input Text:", input_text)
    print("JSON Data:", request.json)
    
    if not input_text:
        # Response to send if the input_text is undefined
       response = {
           'status':'error',
           'message':'Please enter some text to predict emotion'
       }
       return jsonify(response)
   
    else:
        predicted_emotion,predict_emotion_img_url = predict(input_text)
        
        # Response to send if the input_text is not undefined
        response ={
           "status":"success",
           "data":{
              "predicted_emotion":predicted_emotion,
              "predicted_emotion_img_url":predict_emotion_img_url
           }
        }
        # Send Response         
        return jsonify(response)
    
if __name__ == "__main__":
    app.run(debug=True)