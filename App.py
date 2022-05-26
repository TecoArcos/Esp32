from  flask import  Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'ESP32'
sql = MySQL(app)

@app.route('/contac')
def add_contac():
    return 'asdasd'



@app.route('/edit')
def edit_contac():
    return '123456789'

@app.route('/delete')
def delete_contac():
    return 'asdasd'


if __name__ == '__main__': 
    app.run( debug = True )
