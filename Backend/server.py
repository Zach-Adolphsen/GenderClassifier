from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)

class Gender(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    shoe_size = db.Column(db.Integer)
    def to_dict(self):
        return {
            'id': self.id,
            'height': self.height,
            'weight': self.weight,
            'shoe_size': self.shoe_size,
        }

@app.route('/api/data')
def get_data():
    return {
        'name':"geek",
        'age':"19",
    }

if __name__ == '__main__':
    app.run(debug=True)