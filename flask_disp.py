from flask import Flask,render_template,request
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='root'
app.config['MYSQL_DB']= 'minedb'

mysql=MySQL(app)

@app.route('/')
@app.route('/home')
def register():
    return render_template("register.html")


@app.route('/confirm',methods=['GET','POST'])
def confirm():
    if request.method == 'POST':
        n=request.form.get('name')
        a = request.form.get('age')
        g = request.form.get('gender')
        d = request.form.get('degree')
        cr = request.form.get('course')
        c = request.form.get('city')
        cur = mysql.connection.cursor()
        job = "INSERT INTO registered_students(Name,Age,Gender,Degree,Course,City) VALUES(%s,%s,%s,%s,%s,%s)"
        ips = (n,a,g,d,cr,c)
        cur.execute(job,ips)
        mysql.connection.commit()
        cur.close()

        return render_template('confirm.html',name=n,age=a,gender=g,degree=d,course=cr,city=c)


@app.route('/users')
def users():
    cur=mysql.connection.cursor()
    job="SELECT * FROM registered_students"
    cur.execute(job,)
    list1=cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return render_template("users.html",students=list1)


if __name__=='__main__':
    app.run(debug=True)