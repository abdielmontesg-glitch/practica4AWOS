from flask import Flask, render_template,request, jsonify, make_response, session
app = Flask(__name__)

@app.route('/productos')
def productos():
    import mysql.connector
    mydb = mysql.connector.connect(
      host="localhost",
      user="",
      password="yourpassword",
      database="mydatabase"
    )    
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM customers")
    myresult = mycursor.fetchall()
    return make_response(jsonify(myresult))
