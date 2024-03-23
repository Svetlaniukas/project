from flask import Flask

app = Flask(__name__)
app.secret_key = '1234567890'
from . import routes  # noqa: F401
