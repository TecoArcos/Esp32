
from  flask import  Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'ESP32'
sql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')
    

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
       dato =  request.form['dato']
       print(dato)
       return dato

        
@app.route('/delete')
def delete_contac():
    return 'asdasd'


if __name__ == '__main__': 
    app.run( debug = True )
