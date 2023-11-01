import psycopg2


from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgres://lfw_lab10db_user:YU0QBOASi64a4TKGi6Z434YDgCYNWXKA@dpg-cl19te2s1bgc73ekto30-a/lfw_lab10db")
    conn.close()
    return("Successful Database Connection")
