import os
import datetime
import hashlib
import Crypto.Cipher
from flask import Flask, session, url_for, redirect, render_template, request, abort, flash
from database import db_connect,user_reg,owner_reg,owner_login,upload_file,owner_viewfiles,upload_clouddata,user_request,owner_request,dele_act,bserver_viewdata,dele_act1
from database import onwer_viewdata,user_loginact,user_viewfile,user_viewfiledata,user_down,user_finaldown,owner_update,user_down1,algo,addf_act,server_logact,server_viewdata,bchain_logact
from werkzeug.utils import secure_filename 
import random
import base64 
from hashlib import sha256, md5
import ecdsa
import os
import sys
from sendmail import sendmail
from ecdsa import SigningKey, VerifyingKey
from RSA import encrypt,decrypt,generate

#from cloud import uploadFile,downloadFile,close
from eval import main
import numpy as np
app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route("/")
def FUN_root():
    return render_template("index.html")


@app.route("/owner")
def FUN_admin():    
    return render_template("owner.html")

@app.route("/bhome")
def bhome():    
    return render_template("bhome.html")

@app.route("/ownerlogact",methods = ['GET','POST'])
def owner_logact():
   if request.method == 'POST':
      status=owner_login(request.form['username'],request.form['password'])
      if status:
         session['username'] = request.form['username']
         return render_template("ownerhome.html",m1="sucess")
      else:
         return render_template("owner.html",m1="sucess")

@app.route("/serverlogact",methods = ['GET','POST'])
def serverlogact():
   if request.method == 'POST':
      status=server_logact(request.form['username'],request.form['password'])
      if status:
         session['username'] = request.form['username']
         return render_template("shome.html",m1="sucess")
      else:
         return render_template("server.html",m1="sucess")

@app.route("/bchainlogact",methods = ['GET','POST'])
def bchainlogact():
   if request.method == 'POST':
      status=bchain_logact(request.form['username'],request.form['password'])
      if status:
         session['username'] = request.form['username']
         return render_template("bhome.html",m1="sucess")
      else:
         return render_template("bchain.html",m1="sucess")


@app.route("/user/")
def FUN_student():
       
    return render_template("user.html")   



@app.route("/server/")
def server():
    return render_template("server.html")  

@app.route("/bchain/")
def bchain():
    return render_template("bchain.html")  


@app.route("/userreg/")
def FUN_userreg():
    return render_template("userreg.html")


@app.route("/userregact", methods = ['GET','POST'])
def user_regact():
   if request.method == 'POST':
      status = user_reg(request.form['username'],request.form['password'],request.form['dob'],request.form['email'],request.form['city'],request.form['contactno'])
      if status:
       return render_template("user.html",m1="Success")
      else:
       return render_template("user.html",m1="Success")

@app.route("/userlogact",methods = ['GET','POST'])
def user_logact():
   if request.method == 'POST':
      status=user_loginact(request.form['email'],request.form['password'])
      if status:
         session['email'] = request.form['email']
         return render_template("userhome.html",m1="Success")
      else:
         return render_template("user.html",m1="Success")


@app.route("/userhome")
def user_home():
      return render_template("userhome.html")

@app.route("/vf/")
def user_vf():
       viewfile = user_viewfile(session['email'])
       return render_template("vf.html", viewfiledata = viewfile)

@app.route("/user_vf1/", methods = ['GET', 'POST'])
def user_vf1():
        fname = request.args.get('filename')
        owner = request.args.get('owner')
        data = request.args.get('data')
        print(fname,owner,data,session['email'])
        check = user_viewfiledata(fname,owner,data,session['email'])
        if check:
         return render_template("vf.html")         
        else:
         return render_template("vf.html") 


@app.route("/deleact/", methods = ['GET', 'POST'])
def deleact():
        filename = request.args.get('filename')
        print(filename)
        check = dele_act(filename)
        check1 = dele_act1(filename)
        if check:
         return render_template("bviewencfiles.html")         
        else:
         return render_template("bviewencfiles.html")



@app.route("/addf/", methods = ['GET', 'POST'])
def addf():
        fname = request.args.get('filename')
        owner = request.args.get('owner')
        return render_template("addf.html", fname=fname , owner=owner)         
       
            

@app.route("/download/")
def user_download():
      downloaddata = user_down(session['email'])
      return render_template("download.html", downloads = downloaddata)

@app.route("/downloadact/" , methods = ['GET', 'POST'])
def user_downloadact():
      fname = request.args.get('fname')
      downloaddata = user_down1(session['email'],fname)
      return render_template("downloadact.html", downloadview = downloaddata)

@app.route("/ownerreg/")
def FUN_ownerreg():
      return render_template("ownerreg.html")

@app.route("/ownerregact", methods = ['GET','POST'])
def FUN_ownerregact():
    if request.method == 'POST':
      status = owner_reg(request.form['username'],request.form['password'],request.form['dob'],request.form['email'],request.form['city'],request.form['contactno'])
      if status == True:
       return render_template("ownerhome.html",m1="Login sucess")
      else:
       return render_template("owner.html",m1="Login failed")

##############  ML CODE #####################################################

@app.route("/addfact", methods = ['GET','POST'])
def addfact():
    if request.method == 'POST':
        classes = {0:"normal",1:"dos",2:"r2l",3:"u2r",4:"probe"}   
        fname = request.form['fname']
        dur = request.form['dur']
        port =request.form['port']
        service = request.form['service']
        flag = request.form['flag']
        srcbytes =request.form['srcbytes']
        dstnbytes = request.form['dstnbytes']
        login_status = request.form['login_status']
        wrong = request.form['wrong']
        sdc = request.form['sdc']
        srv_count = request.form['srv_count']
        pred, prob = main(srv_count)
        result1=srv_count
        print("DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD")        
        print(pred)
        print(prob)
        result = np.argmax(prob)
        print(result)
        
        prediction = classes[int(result1)]
        print(prediction) 
        print("DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD")
        result = ""
        if prediction == "normal":
           result ="normal"
        else:
           result ="FaultPacket"
        status = addf_act(fname,result)
        if status == True:
            return render_template("viewencfiles.html",m1="submit sucess")
        else:
            return render_template("viewencfiles.html",m1="Login failed")



@app.route("/ownerhome")
def FUN_ownerhome():
    return render_template("ownerhome.html")

@app.route("/Upload", methods = ['GET','POST'])
def owner_upload():
   if request.method == 'POST':
      file = request.files['inputfile']
      check = upload_file(request.form['fname'],file,session['username'])
       
      print(check)
      if check:
         return render_template("fileupload.html",m1="success")
      else:
         return render_template("fileupload.html",m1="Failed")

@app.route("/fileupload")
def FUN_fileupload():
         return render_template("fileupload.html")

@app.route("/ownerviewfiles")
def FUN_ownerviewfiles():
    viewdata = owner_viewfiles(session['username'])
    if viewdata:
        return render_template("ownerviewfiles.html",showdata = viewdata)
    else:
        return render_template("ownerviewfiles.html",m1="Failed")

#  Globals begin.
hmsg=''
ds =''
pvk = ''
pbk = ''
#  Globals end.

@app.route("/Gensig/", methods = ['GET' , 'POST'])
def owner_split():
    fname = request.args.get('fname')
    owner = request.args.get('owner')
    data = request.args.get('data')
     #RSA ORIGHINAL
    key_pair = generate(8)
    print('Generated Key pairs')
    public_key = key_pair["public"]
    private_key = key_pair["private"]
    print(key_pair["public"])
    print(key_pair["private"])
     #Now encrypt
     
    #datas,key=generateblockchain('firstblock',data)
    #print("blockchain")
    #print(datas)
    #print(key)
    ciphertext = encrypt(public_key, data )
   
    txt = ', '.join(map(lambda x: str(x), ciphertext))
    print ("Ciphertext is: ")
    print (txt)
    print(ciphertext)
    fileRSA= open("C:/Users/adith/OneDrive/Desktop/input/RSA.txt", "w")
    fileRSA.write(txt)
    fileRSA.close()
    #uploadFile('RSA.txt',"C:/Users/Mrida/Desktop/input/RSA.txt")
    val = ', '.join(map(lambda x: str(x), private_key))
    
    #close()
    status = upload_clouddata(fname.rstrip(),owner,data,str(txt),str(val)) 
    
    #   Signing of the Message/Data using Private key and Hashed Message ends here.
    if status:
        return redirect(url_for('FUN_ownerviewfiles'))         
    else:
        return render_template("ownerviewfiles.html",m1="Failed")

@app.route("/viewencfiles")
def owner_viewencfiles():
    digitalsigndata = onwer_viewdata(session['username'])
    
    return render_template("viewencfiles.html",spliinfo = digitalsigndata)

@app.route("/sviewencfiles")
def sviewencfiles():
    digitalsigndata = server_viewdata()
    
    return render_template("sviewencfiles.html",spliinfo = digitalsigndata)

@app.route("/bviewencfiles")
def bviewencfiles():
    digitalsigndata = bserver_viewdata()
    
    return render_template("bviewencfiles.html",spliinfo = digitalsigndata)

@app.route("/vuserreq")
def owner_vuserreq():
    userrequest = user_request()
    return render_template("vuserreq.html",userreqdata = userrequest)

@app.route("/logout")
def FUN_logout():
    return render_template("index.html")

    # code for owner response to send key to user to get data 

@app.route("/response", methods = ['GET','POST'])
def owner_response():
       fname1 = request.args.get('filename')
       data1 = request.args.get('data')
       owner1 = request.args.get('owner')       
       email1 = request.args.get('email')
       result = owner_request(fname1,owner1,email1)
      
       rdata = result    
       status = owner_update(rdata,fname1,owner1,email1)
       if status == True:
          for hsmsg,pvk,status in rdata:
               print(hsmsg,pvk,status)
               sendmail(email1,pvk,hsmsg)                           
               return render_template("vuserreq.html")
       else:
               return render_template("vuserreq.html",m1="false")           
           
@app.route("/verify1", methods = ['GET','POST'])
def user_verfiy():
    filename =request.form['filename']
    hsmsg = request.form['hashmsg']    
    publickey = request.form['publickey']    
     #   Now the verification phase begins.
    status,datas = algo(filename,hsmsg,publickey)   
    print("ttttttttttttttttttttttttttttttttt")
    print(status)
    print(datas)
    if status == True:
        for data in datas:
            return render_template('successfulV.html',finaldata=data)   #  A redirect added.
   #   Verification phase ends here.
    else:
        return render_template('failed.html')   #  A redirect added.


@app.route("/logout")
def admin_logout():
    return render_template("index.html")
if __name__ == "__main__":
   app.run(debug=True,host='127.0.0.1', port=5000)

