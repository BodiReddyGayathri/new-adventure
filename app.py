from flask import Flask,render_template

app = Flask(__name__)

JOBS=[
  {
  'id': 1,
  'title': 'Python Developer',
  'location':'banglore',
  'salary':'rs 150000'
},
  {
    'id': 2,
    'title': 'frontend designer',
    'location':'newyork',
    'salary':'$50000'
  },

{
  'id': 3,
  'title': 'backend Developer',
  'location':'texas',
  'salary':'250000$'
}

]

@app.route("/")
def hello_world():
    return render_template('home.html')

if __name__ =="__main__":
  app.run(host= '0.0.0.0', debug =True )
