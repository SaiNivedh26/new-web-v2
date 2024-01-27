from flask import Flask, render_template,jsonify
app = Flask(__name__)

JOBS = [
  {
    'id' : 1,
    'title' : 'Machine Learning Expert',
    'location' : 'Coimbatore, India',
    'salary' : 'Rs.5K-7K'
  },
  {
    'id': 2,
    'title' : 'Data Scientist',
    'location' : 'Coimbatore, India',
    'salary' : 'Rs.7K-12K'
  },
  {
    'id': 3,
    'title' : 'Frontend Engineer',
    'location' : 'Remote',
    'salary' : 'Based on experience'
  },
{
    'id': 4,
    'title' : 'Backend Engineer',
    'location' : 'Coimbatore,India',
    'salary' : 'Rs.3K-5K'  
}
]

@app.route("/")
def hellowoeld():
  return render_template('index.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
  

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True )
  
