# from flask import Flask,request, url_for, redirect, render_template
# import pickle
# import numpy as np

# app = Flask(__name__)

# model=pickle.load(open('randomForest.pkl','rb'))


# @app.route('/')
# def hello_world():
#     return render_template("forest_fire.html")


# @app.route('/predict',methods=['POST','GET'])
# def predict():
#     # int_features=[int(x) for x in request.form.values()]
#     # final=[np.array(int_features)]
#     int_features = [int(x) for x in request.form.values()]
#     final = np.array(int_features).reshape(1, -1)
#     print(int_features)
#     print(final)
#     prediction=model.predict(final)
#     # output='{0:.{1}f}'.format(prediction[0][1], 2)
#     output = '{0:.{1}f}'.format(prediction[0], 2)

#     if output>str(0.5):
#         return render_template('forest_fire.html',pred='Your Forest is in Danger.\nProbability of fire occuring is {}'.format(output),bhai="kuch karna hain iska ab?")
#     else:
#         return render_template('forest_fire.html',pred='Your Forest is safe.\n Probability of fire occuring is {}'.format(output),bhai="Your Forest is Safe for now, Gand Mara")


# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
selected_features = ['day', 'month', 'year', 'Temperature', 'RH', 'Rain', 'Classes']
model = pickle.load(open('randomForest.pkl', 'rb'))

@app.route('/')
def hello_world():
    return render_template("forest_fire.html")

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final = np.array(int_features).reshape(1, -1)
    type(final)
    # Make prediction using the trained model
    prediction = model.predict[final]
    output = '{0:.{1}f}'.format(prediction[0], 2)

    if prediction > 0.5:
        return render_template('forest_fire.html', pred='Your Forest is in Danger.\nProbability of fire occurring is {}'.format(output), bhai="kuch karna hain iska ab?")
    else:
        return render_template('forest_fire.html', pred='Your Forest is safe.\n Probability of fire occurring is {}'.format(output), bhai="Your Forest is Safe for now, Gand Mara")

if __name__ == '__main__':
    app.run(debug=True)
