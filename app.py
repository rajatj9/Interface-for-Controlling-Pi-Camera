from flask import Flask, render_template, request, jsonify, json
import json
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('parameters.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      with open('data.json', 'w') as outfile:
          json.dump(result, outfile)

      # Instead make a posst request to a different end point of the app.
      # Running the python scripts on the different endpoint.
      return "Done"

if __name__ == '__main__':
   app.run(debug = True)
