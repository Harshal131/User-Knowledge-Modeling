from flask import Flask, render_template, request
import pickle
import numpy as np


filename = 'model.pkl'
classifier = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('Index.html')

@app.route('/classify', methods=['POST'])
def classify():
    temp_array = list()        
    STG = float(request.form['STG'])
    SCG = float(request.form['SCG'])
    STR = float(request.form['STR'])
    LPR = float(request.form['LPR'])
    PEG = float(request.form['PEG'])
    temp_array = temp_array + [STG,SCG,STR,LPR,PEG]
        
    data = np.array([temp_array])
    my_classification = str(classifier.predict(data)[0])
    return render_template('Index.html', my_classification=my_classification)



if __name__ == '__main__':
	app.run(debug=True)