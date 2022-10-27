from flask import Flask , render_template , request , redirect
import pymysql


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/' , methods=['GET','POST','DELETE'])
def index():
    if request.method =='POST':        
        name = request.form.get('name')
        age = request.form.get('age')
        hobby = request.form.get('hobby')
        
        set_data(name , age , hobby)
        return render_template('index.html', data=get_data() )
    elif request.method == 'GET':                
        return render_template('index.html',  data=get_data())
    elif request.method == 'DELETE':
        print('delete')
        return render_template('index.html',  data=get_data())

@app.route('/<int:seq>' , methods=['GET'])
def delete(seq):    
    del_data(seq)
    #return render_template('index.html',  data=get_data())
    return redirect("/")

    

def get_data():
    ip = 'testdb1.cmuksnmlogp1.ap-northeast-2.rds.amazonaws.com'
    id = 'admin'
    ps = 'admin1234'
    db_nm = 'testdb'
    set = 'utf8'

    con = pymysql.connect( host=ip 
                           , user = id 
                           , password = ps 
                           , db = db_nm 
                           , charset = set
                           , autocommit=True # 결과 DB 반영 (Insert or update)
                           , cursorclass=pymysql.cursors.DictCursor # DB조회시 컬럼명을 동시에 보여줌 
                           )
    cur = con.cursor()
    sql = 'select  * from dev_table '
    cur.execute(sql)
    rows = cur.fetchall()    
    return rows

def set_data( _name , _age , _hobby):
    ip = 'testdb1.cmuksnmlogp1.ap-northeast-2.rds.amazonaws.com'
    id = 'admin'
    ps = 'admin1234'
    db_nm = 'testdb'
    set = 'utf8'

    con = pymysql.connect( host=ip 
                           , user = id 
                           , password = ps 
                           , db = db_nm 
                           , charset = set
                           , autocommit=True # 결과 DB 반영 (Insert or update)
                           , cursorclass=pymysql.cursors.DictCursor # DB조회시 컬럼명을 동시에 보여줌 
                           )
    cur = con.cursor()
    sql = ''' INSERT INTO dev_table (name, age, hobby) VALUES(\'{0}\',{1} , \'{2}\') '''.format(_name , _age , _hobby)
    print('sql : ', sql)
    cur.execute(sql)
    con.close()

def del_data( _seq ):
    ip = 'testdb1.cmuksnmlogp1.ap-northeast-2.rds.amazonaws.com'
    id = 'admin'
    ps = 'admin1234'
    db_nm = 'testdb'
    set = 'utf8'

    con = pymysql.connect( host=ip 
                           , user = id 
                           , password = ps 
                           , db = db_nm 
                           , charset = set
                           , autocommit=True # 결과 DB 반영 (Insert or update)
                           , cursorclass=pymysql.cursors.DictCursor # DB조회시 컬럼명을 동시에 보여줌 
                           )
    cur = con.cursor()
    sql = ''' delete from dev_table where seq = {0} '''.format(_seq )
    print('sql : ', sql)
    cur.execute(sql)
    con.close()    
        
                 

if __name__=='__main__':
    app.run(host='0.0.0.0', port=80 , debug=True )