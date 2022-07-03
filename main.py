from flask import Flask, jsonify

from flask import Flask
app= Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')
@app.route('/home' , methods=['POST'])
def create_newpage():
  request_data = request.get_json()
  new_page = {
    'name':request_data['name'],
    'items':[]
  }
  newpage.append(new_page)
  return jsonify(new_page)

app.run(port=5000)
