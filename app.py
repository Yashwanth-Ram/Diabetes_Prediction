from flask import Flask, render_template, request
#from flask.wrappers import Request
import joblib

app = Flask(__name__)

#load model
model = joblib.load('dib_79.pkl')

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/home')
def homepage():
    return render_template('home.html')

@app.route('/blog', methods= ['POST'])
def blog():

    a = request.form.get('preg')
    b = request.form.get('plas')
    c = request.form.get('pres')
    d = request.form.get('skin')
    e = request.form.get('test')
    f = request.form.get('mass')
    g = request.form.get('pedi')
    h = request.form.get('age')

    #print([a,b,c,d,e,f,g,h])

    pred = model.predict([[int(a),int(b),int(c),int(d),int(e),int(f),int(g),int(h)]])

    if pred[0]==1:
        output = 'diabetic'

    else:
        output = 'not diabetic'

    return render_template('blog.html', pred_text=f'The person is {output}')

#run the app
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080)
    #app.run(debug=True)