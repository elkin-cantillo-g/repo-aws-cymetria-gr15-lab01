from flask import Flask
from controllers.admin_s3 import *

app = Flask(__name__)
from routes.route import *

if __name__ == "__main__":    
    host = "172.31.29.219"
    port = 80
    app.run(host, port, True)
