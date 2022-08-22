import pickle
from flask import Flask, render_template, request

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/prediction', methods=['GET', 'POST'])
def prediction():

    area = request.form.get('area')
    bathrooms = request.form.get('bathrooms')
    stories = request.form.get('stories')
    airconditioning = 1 if request.form.get('airconditioning') == 'Yes' else 0
    parking = request.form.get('parking')

    prediction_value = model.predict([[int(area), int(bathrooms),
                                    int(stories), airconditioning, int(parking)]])
    prediction_value = round(prediction_value[0], 2)

    return render_template('index.html', prediction_text=f'Rate of the house is {prediction_value}/-')


if __name__ == '__main__':
    app.run(debug=True)
