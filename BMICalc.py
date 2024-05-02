from flask import *
app = Flask(__name__)

@app.route('/') #decorator for home page
def home():
       return render_template("index.html")

@app.route('/calculate', methods = ["POST"])
def calculate():
       data = request.form
       #retrieve values from webpage and store into data which is a dict 
       h = float(data["height"])      
       w = float(data["weight"])

       #now assuming user input to be valid
       #to be coded - perform data validation on client side
       #to be coded - render index.html if data is invalid
       
       bmi = round(w/(h**2),2)

       return render_template("viewcalc.html", bmi = bmi)
       
if __name__ == '__main__':
    app.run()
    



