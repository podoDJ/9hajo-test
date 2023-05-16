# pip install flask pymongo dnspython requests bs4
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.qihykt0.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

import requests
from bs4 import BeautifulSoup

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/teamatetest", methods=["POST"])
def teamatetest_post():
    name_receive = request.form['name_give']
    age_receive = request.form['age_give']
    residence_receive = request.form['residence_give']
    food_receive = request.form['food_give']
    mbti_receive = request.form['mbti_give']
    selfdesc_receive = request.form['selfdesc_give']
    respect_receive = request.form['respect_give']
    recentmovie_receive = request.form['recentmovie_give']
    #m_id는 mongdodb의 teamatetest 컬렉션에서 검색된 문서들의 개수이다.
    m_id = len(list(db.teamatetest.find({})))
    

    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    # data = requests.get(url_receive, headers=headers)

    # soup = BeautifulSoup(data.text, 'html.parser')

    # ogimage = soup.select_one('meta[property="og:image"]')['content']
    # ogtitle = soup.select_one('meta[property="og:title"]')['content']
    # ogdesc = soup.select_one('meta[property="og:description"]')['content']


    doc = {
		'name':name_receive,
        'age':age_receive,
        'residence':residence_receive,
        'food':food_receive,
        'mbti':mbti_receive,
        'selfdesc':selfdesc_receive,
        'respect':respect_receive,
        'recentmovie':recentmovie_receive,
        'm_id':m_id,
 
    }

    db.teamatetest.insert_one(doc)

    return jsonify({'msg':'저장완료!'})

@app.route("/teamatetest", methods=["GET"])
def teamatetest_get():
    all_teamates = list(db.teamatetest.find({},{'_id':False}))
    return jsonify({'result':all_teamates})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)