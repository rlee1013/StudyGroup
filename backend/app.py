from flask import Flask
 
# Initializing flask app
app = Flask(__name__)
 
 
# Home
@app.route('/home')
def get_home():
 
    # Returning an api for showing in  reactjs
    return {
        'Name':"Ryan", 
        "Age":"19",
        "Day":"4/13/24"
        }
 
     
# Running app
if __name__ == '__main__':
    app.run(port = 5000, debug=True)
