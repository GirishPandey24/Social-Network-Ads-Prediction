from flask import Flask,render_template,request
import pickle


app=Flask(__name__)

knn=pickle.load(open('model.pkl','rb'))

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    age=request.form.get('age')
    salary=request.form.get('salary')

    result=knn.predict([[age,salary]])[0]
    #return "The age is {} and the Salary is {}".format(age,salary)
    if result==1:
        return render_template('index.html',label=1)
    else:
        return render_template('index.html',label=-1)
if __name__=='__main__':
    app.run(debug=True)
