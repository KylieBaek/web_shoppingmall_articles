from flask import Flask, render_template,request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('shoppingmall_openapi.html')

@app.route('/order', methods=['POST'])
def saving():
    name = request.form['name_give']
    cnt = request.form['cnt_give']
    address = request.form['address_give']
    phone = request.form['phone_give']

    doc = {
        'name' : name,
        'cnt':cnt,
        'address' : address,
        'phone' :phone
    }

    db.shops.insert_one(doc)
    return jsonify({'result': 'success'})

@app.route('/order', methods=['GET'])
def listing():
    result = list(db.shops.find({}, {'_id': 0}))
    return jsonify({'result':'success', 'orders':result})


if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)
