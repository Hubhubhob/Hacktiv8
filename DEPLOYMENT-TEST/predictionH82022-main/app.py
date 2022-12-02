import flask 
import numpy as np
import pickle 

app = flask.Flask(__name__, template_folder="templates")

model = pickle.load(open('model/model_classifier.pkl','rb'))

@app.route('/')
def index():
    return(flask.render_template('main.html'))

@app.route('/predict', methods=['POST'])
def predict():
    int_feature = [int(val) for val in flask.request.form.values()]
    final_feature = [np.array(int_feature)]
    prediction = model.predict(final_feature)
    output = {0: 'Not Placed' , 1: 'Placed'}
    
    return flask.render_template('main.html',prediction_text='Student must be {} to workplace'.format(output[prediction[0]]))

if __name__ == '__main__':
    app.run(debug=True)

