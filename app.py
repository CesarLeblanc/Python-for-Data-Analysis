from flask import Flask,render_template,url_for,request
from flask_material import Material

# EDA PKg
import pandas as pd
import numpy as np

# ML Pkg
from sklearn.externals import joblib


app = Flask(__name__)
Material(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/preview')
def preview():
    df = pd.read_csv("data/dataset.csv")
    return render_template("preview.html",df_view = df)

@app.route('/',methods=["POST"])
def analyze():
	if request.method == 'POST':
		height = request.form['height']
		area = request.form['area']
		eccen = request.form['eccen']
		p_black = request.form['p_black']
		p_and = request.form['p_and']
		blackpix = request.form['blackpix']
		blackand = request.form['blackand']
		model_choice = request.form['model_choice']

		# Clean the data by convert from unicode to float
		sample_data = [height, area, eccen, p_black, p_and, blackpix, blackand]
		clean_data = [float(i) for i in sample_data]

		# Reshape the Data as a Sample not Individual Features
		ex1 = np.array(clean_data).reshape(1,-1)

		# ex1 = np.array([6.2,3.4,5.4,2.3]).reshape(1,-1)

		# Reloading the Model
		if model_choice == 'decision_tree_model':
		    decision_tree_model = joblib.load('data/ada_boosting_model.pkl')
		    result_prediction = decision_tree_model.predict(ex1)
		elif model_choice == 'random_forest_model':
			random_forest_model = joblib.load('data/ada_boosting_model.pkl')
			result_prediction = random_forest_model.predict(ex1)
		elif model_choice == 'ada_boosting_model':
			ada_boosting_model = joblib.load('data/ada_boosting_model.pkl')
			result_prediction = ada_boosting_model.predict(ex1)

	return render_template('index.html', height=height,
		area=area,
		eccen=eccen,
		p_black=p_black,
		p_and=p_and,
		blackpix=blackpix,
		blackand=blackand,
		clean_data=clean_data,
		result_prediction=result_prediction,
		model_selected=model_choice)


if __name__ == '__main__':
	app.run(debug=True)