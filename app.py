from flask import Flask, render_template,request, jsonify, make_response, session
app = Flask(__name__)

@app.route('/usuarios')
def usuarios():
    import mysql.connector
    mydb = mysql.connector.connect(
      host="",
      user="",
      password="b",
      database=""
    )    
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM customers")
    myresult = mycursor.fetchall()
    return make_response(jsonify(myresult))
