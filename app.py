from flask import Flask,request, render_template ,request,redirect, url_for
import os
import subprocess




app = Flask(__name__)

 

@app.route('/')

def index():
    return render_template("index.html")



@app.route('/resulton/')
def funksiya():
    try:
        os.system('cmd /k"netsh advfirewall set all state on"')
    except:
        print('could not execute command')

@app.route('/resultoff/')
def funksiyaiki():
    try:
        os.system('cmd /k"netsh advfirewall set all state off"')
    except:
        print('could not execute command')

@app.route('/success/<name>', methods = ['POST','GET'])
def success(name):
      command = os.system('cmd /k"ping {} "'.format(name))
      pro = os.Popen(command, shell=True,stdout=subprocess.PIPE)
      return pro
      return render_template('index.html')

@app.route('/func', methods = ['POST','GET'])
def qiymetalma():
    ping = request.form['input']
    return redirect(url_for('success',name = ping))


@app.route('/blok', methods = ['POST','GET'])
def qiymetialma():
    blok = request.form['blok']
    return redirect(url_for('blok',ad = blok))

@app.route('/blok/<ad>', methods = ['POST','GET'])
def blok(ad):
      command = os.system('cmd /k"netsh advfirewall firewall add rule name="BLOCK IP ADDRESS by senanisko and semasisko" dir=in action=block remoteip={} "'.format(ad))
      pro = subprocess.Popen(command, shell=True,stdout=subprocess.PIPE)
      print(pro.communicate()[0]) # prints the stdout
      return render_template('index.html')

@app.route('/blok', methods = ['POST','GET'])
def qiymetdenalma():
    blok = request.form['blok']
    return redirect(url_for('blok',ad = blok))

@app.route('/icaze/<allow>', methods = ['POST','GET'])
def icaze(allow):
      command = os.system('cmd /k"netsh advfirewall firewall add rule name="ALLOW IP ADDRESS by senanisko and semasisko" dir=in action=allow remoteip={} "'.format(allow))
      pro = subprocess.Popen(command, shell=True,stdout=subprocess.PIPE)
      print(pro.communicate()[0]) # prints the stdout
      return render_template('index.html')

@app.route('/icaze', methods = ['POST','GET'])
def qiymetleralma():
    icaze = request.form['icaze']
    return redirect(url_for('icaze',allow = icaze))
    
if __name__ == "__main__":
    app.run(debug=False,host = "0.0.0.0",port 443)


# pymysql, mysql-connector, mysql-connector-python
