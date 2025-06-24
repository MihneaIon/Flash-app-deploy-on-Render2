from flask import Flask, jsonify

app = Flask(__name__)

my_array = ["Mihnea", "Adina"]

@app.route('/data')
def get_data():
    return jsonify(my_array)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)