from flask import Flask, render_template, request
from model import predict_image
import utils

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/testPage', methods=['GET'])
def testPage():
    return render_template('testPage.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        file = request.files['file']
        img = file.read()
        prediction = predict_image(img)
        print(prediction)

        # Check if the predicted category is a corn leaf disease
        if prediction.startswith("Corn_(maize)"):
            res = utils.disease_dic[prediction]
            formatted_result = format_result(res)
            return render_template('display.html', result=formatted_result)
        else:
            message = 'This leaf is not a corn type of plant'
            return render_template('error.html', message=message)
    except:
        message = ' Please upload a real corn leaf'
        return render_template('error.html', message=message)

def format_result(result):
    # Format the result as needed
    formatted_result = " " + result
    return formatted_result

if __name__ == "__main__":
    app.run(debug=True)
