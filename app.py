from flask import Flask,request
from send_email import send_email_to_recipients
import os
import socket
import json
SMTP_HOST=os.environ.get('SMTP_HOST','smtp.gmail.com')
SMTP_PORT=os.environ.get('SMTP_PORT',465)
SMTP_USERFROM=os.environ.get("SMTP_USERFROM",'ksaiprakash01@gmail.com')
SMTP_PASSWORD=os.environ.get("SMTP_PASSWORD",None)

app = Flask(__name__)
@app.route("/")
@app.route('/health')
def health():
    with open('version.json',mode='r') as read_json:
         data = json.load(read_json)
    return {
        "Notify": "Up and Running",
        "Container": socket.gethostname(),
        "version"  : data['version']


    }
@app.route('/notify',methods=["GET","POST"])
def notify():
    try:
        id        = request.args.get('id')
        firstname = request.args.get('firstname')
        lastname  = request.args.get('lastname')
        email     = request.args.get('email')
        body = f"""Registration Successful for Softglacier for {id},{firstname},{lastname}"""
        send_email_to_recipients('/tmp',email,SMTP_HOST,SMTP_PORT,SMTP_USERFROM,SMTP_PASSWORD,body)
        return "successfully sent email"
    except Exception as err:
        return {
            "error":err
        }
if __name__ == "__main__":
    app.run("0.0.0.0",port=8080,debug=True)