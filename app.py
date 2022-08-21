import pickle
from flask import Flask,render_template,request

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prediction',methods=['GET','POST'])
def prediction():
    prediction_value = model.predict([[request.form.get('area')]])
    prediction_value = round(prediction[0],2)
    return render_template('index.html',prediction_text=f'Rate of the house is {prediction_value}/-')


if __name__ == '__main__':
    app.run(debug=True)