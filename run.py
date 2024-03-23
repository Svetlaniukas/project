# run.py
from app import app
import sys
sys.path.insert(0, '/Users/svetlanamelichova/Desktop/wooden-products-website')


if __name__ == '__main__':
    app.run(port=8000, debug=True)
