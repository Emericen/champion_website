from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '0f88ed581f6913b05571b661b7c9f1e2'

from champion_webapp import routes

