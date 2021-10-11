from flask import Flask, render_template, request

#Change!!!???

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', \
    title="姓名判断bot", \
    message="あなたのお名前は？")

@app.route('/', methods=['POST','GET'])
def form():
    if request.method=='POST':
        try:
            field = request.form['field']
            print(len(field))
            if len(field) > 5:
                luck = '大吉'
            else: luck = '凶'

            with sql.connect("luckname.db") as con:
                cur=con.cursor()
                cur.execute("insert into luckname (name,foetune) VALUES (?,?)",(field,luck))
                con.commit()
        except:
            msg="error"
        
        finally:
            con.close()
            return render_template('index.html', \
        title="姓名判断bot", \
        message="あなたの運勢は「%s」です！" % field)

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost', port=12345)