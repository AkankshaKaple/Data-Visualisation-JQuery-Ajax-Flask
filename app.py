from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index(chart1ID = 'chart1_ID', chart1_type = 'bar', chart1_height = 300,
chart2ID = 'chart2_ID', chart2_type = 'bar', chart2_height = 300):

  chart1 = {"renderTo": chart1ID, "type": chart1_type, "height": chart1_height}
  data = pd.read_csv("/home/my_hduser/FLASK_NEW-master/FLASK/Data.csv")
  male_count = data[data['Gender'] == 'M']["Gender"].count()
  female_count = data[data['Gender'] == 'F']["Gender"].count()
  series1 = [{"name": 'Male', "data": [male_count]}, {"name": 'Female', "data": [female_count]}]
  title1 = {"text": 'Gender Ratio'}
  xAxis1 = {"categories": ['Gender']}
  yAxis1 = {"title": {"text": 'Count'}}


  chart2 = {"renderTo": chart2ID, "type": chart2_type, "height": chart2_height,}
  technologies = []
  values = []
  for i in data.Technology.unique():
    technologies.append(i)
    values.append(data[data['Technology'] == i]["Technology"].count())

  series2 = [{"name": 'Technologies', "data": values}]
  title2 = {"text": 'Technologies'}
  xAxis2 = {"categories": technologies}
  yAxis2 = {"title": {"text": 'Count'}}

  return render_template('index.html', chart1ID=chart1ID, chart1=chart1, series1=series1, title1=title1, xAxis1=xAxis1, yAxis1=yAxis1,
                         chart2ID=chart2ID, chart2=chart2, series2=series2, title2=title2, xAxis2=xAxis2, yAxis2=yAxis2)
if __name__ == "__main__":
 app.run(debug = True, host='127.0.0.1', port=5000, passthrough_errors=True)