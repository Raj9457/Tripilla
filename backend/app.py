



from flask import Flask
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

app = Flask(__name__)
db = client['homestead_horizon']
hosts_collection = db['hosts']
@app.route('/hosts', methods=['GET'])
def get_hosts():
    # Retrieve all hosts from the database and return as JSON response
    hosts = list(hosts_collection.find())
    return jsonify(hosts)

if __name__ == '__main__':
    app.run(debug=True)
