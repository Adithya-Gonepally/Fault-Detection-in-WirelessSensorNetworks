import sqlite3
import hashlib
import datetime

user_db_file_location = "database_file/Ecc_signature.db"


def db_connect():
     _conn = sqlite3.connect(user_db_file_location)
     return _conn
      
def user_reg(username,password,email,dob,city,cno):
      _conn = sqlite3.connect(user_db_file_location)
      _c = _conn.cursor()
      _c.execute("insert into user values(?,?,?,?,?,?)", (username,password,email,dob,city,cno))
      _conn.commit()
      _conn.close()  
      return True

def user_loginact(email,password):
      _conn = sqlite3.connect(user_db_file_location)
      _c = _conn.cursor()
      _c.execute("select * from user where email='"+email+"' and password='"+password+"'")
      result = _c.fetchall()
      _conn.close()  
      return result

def owner_reg(username,password,email,dob,city,cno):
      _conn = sqlite3.connect(user_db_file_location)
      _c = _conn.cursor()
      _c.execute("insert into owner values(?,?,?,?,?,?)", (username,password,email,dob,city,cno))
      _conn.commit()
      _conn.close()  
      return True

def owner_login(username,password):
      _conn = sqlite3.connect(user_db_file_location)
      _c = _conn.cursor()
      _c.execute("select * from owner where username='"+username+"' and password='"+password+"'")
      result = _c.fetchall()
      _conn.close()  
      return result



def server_logact(username,password):
      _conn = sqlite3.connect(user_db_file_location)
      _c = _conn.cursor()
      _c.execute("select * from server where username='"+username+"' and password='"+password+"'")
      result = _c.fetchall()
      _conn.close()  
      return result

def bchain_logact(username,password):
      _conn = sqlite3.connect(user_db_file_location)
      _c = _conn.cursor()
      _c.execute("select * from bc where username='"+username+"' and password='"+password+"'")
      result = _c.fetchall()
      _conn.close()  
      return result

def upload_file(filename,file,username):
    _conn = sqlite3.connect(user_db_file_location)
    _c = _conn.cursor()
    current_timestamp = str(datetime.datetime.now())
    name = file.filename
    data = file.read() 
   
    i =_c.execute("insert into file values(?,?,?,?,?)", (data,filename,current_timestamp,data.decode('utf-8'),username))
    _conn.commit()
    _conn.close()
    return i

def owner_viewfiles(username):
     _conn = sqlite3.connect(user_db_file_location)
     _c = _conn.cursor()
     _c.execute("select rowid, filename, data, CDate,owner from file where owner='"+username+"'")
     result = _c.fetchall()
     _conn.commit()
     _conn.close()
     return result

def upload_clouddata(fname,owner,data,hmsg,pvk):
     _conn = sqlite3.connect(user_db_file_location)
     _c = _conn.cursor()
     status="pending"
     i =_c.execute("insert into cloudadata values(?,?,?,?,?,?)", (fname,owner,data,hmsg,pvk,status))
     _conn.commit()
     _conn.close()
     return i

def onwer_viewdata(username):
     _conn = sqlite3.connect(user_db_file_location)
     _c = _conn.cursor()
     _c.execute("select filename,owner,hsmsg,pvk from cloudadata where owner='"+username+"'")
     result = _c.fetchall()
     _conn.commit()
     _conn.close()
     return result

def server_viewdata():
     _conn = sqlite3.connect(user_db_file_location)
     _c = _conn.cursor()
     _c.execute("select filename,owner,hsmsg,pvk,status from cloudadata ")
     result = _c.fetchall()
     _conn.commit()
     _conn.close()
     return result

def bserver_viewdata():
     _conn = sqlite3.connect(user_db_file_location)
     _c = _conn.cursor()
     _c.execute("select filename,owner,hsmsg,pvk,status from cloudadata ")
     result = _c.fetchall()
     _conn.commit()
     _conn.close()
     return result

def user_request():
    _conn = sqlite3.connect(user_db_file_location)
    _c = _conn.cursor()
    _c.execute("select filename,data,owner,email from request")
    result = _c.fetchall()
    _conn.commit()
    _conn.close()
    return result

def owner_request(fname,owner,email):
      _conn = sqlite3.connect(user_db_file_location)
      _c = _conn.cursor()
      _c.execute("select hsmsg,pvk,status from cloudadata where owner='"+owner+"' and filename='"+fname+"'")
      result = _c.fetchall()
     # owner_update(result,fname,owner,email)
      _conn.commit()
      _conn.close()
      return result

def owner_update(result,fname,owner,email):
     if result:
        for hsmsg,pbk,status in result:  
          print("777777777777777777777")
          print(status)
          _conn = sqlite3.connect(user_db_file_location)
          _c = _conn.cursor()
          if status == "normal":
              _c.execute("update request set status= 'yes', hsmsg='"+hsmsg+"' where filename='"+fname+"'and email='"+email+"' and owner = '"+owner+"'")
              _conn.commit()
              _conn.close()
          else:
             _c.execute("update request set status= 'No', hsmsg='"+hsmsg+"' where filename='"+fname+"'and email='"+email+"' and owner = '"+owner+"'")
             _conn.commit()
             _conn.close()
               
     return True 


def addf_act(fname,result):
    _conn = sqlite3.connect(user_db_file_location)
    _c = _conn.cursor()
         
    _c.execute("update cloudadata set status= '"+result+"'  where filename='"+fname+"'")
    _conn.commit()
    _conn.close()
    return True 






def user_viewfile(email):
    _conn = sqlite3.connect(user_db_file_location)
    _c = _conn.cursor()
    _c.execute("select filename,data,owner from file")
    result = _c.fetchall()
    _conn.commit()
    _conn.close()
    return result


def user_viewfiledata(fname,owner,data,email):
    _conn = sqlite3.connect(user_db_file_location)
    _c = _conn.cursor()
    i =_c.execute("insert into request(filename, data, owner,status,email) values ('"+fname+"','"+data+"','"+owner+"','No','"+email+"')")
    _conn.commit()
    _conn.close()
    return i

def dele_act(filename):
    _conn = sqlite3.connect(user_db_file_location)
    _c = _conn.cursor()
    i =_c.execute("delete from file where filename='"+filename+"'")
    _conn.commit()
    _conn.close()
    return i

def dele_act1(filename):
    _conn = sqlite3.connect(user_db_file_location)
    _c = _conn.cursor()
    i =_c.execute("delete from cloudadata where filename='"+filename+"'")
    _conn.commit()
    _conn.close()
    return i


def user_down(email):
    _conn = sqlite3.connect(user_db_file_location)
    _c = _conn.cursor()
    _c.execute("select filename,owner,hsmsg from request where email = '"+email+"' and status = 'yes'")
    result = _c.fetchall()
    _conn.commit()
    _conn.close()
    return result

def user_down1(email,fname):
    _conn = sqlite3.connect(user_db_file_location)
    _c = _conn.cursor()
    _c.execute("select filename,owner,hsmsg from request where email = '"+email+"' and status = 'yes' and filename = '"+fname+"'")
    result = _c.fetchall()
    _conn.commit()
    _conn.close()
    return result


def user_finaldown(filename,dkey):
    _conn = sqlite3.connect(user_db_file_location)
    _c = _conn.cursor()
    _c.execute("select filename,owner from cloudadata where filename='" + filename + "' and skey2 = '"+dkey+"'")
    result = _c.fetchall()
    _conn.commit()
    _conn.close()
    return result

def check(hsmsg,publickey):
     _conn = sqlite3.connect(user_db_file_location)
     _c = _conn.cursor()
     _c.execute("select pvk from cloudadata where hsmsg='"+hsmsg+"'")
     result = _c.fetchall()
     i=False;
     k=False;
     x=False;
     print("yyyyyyyyyyyyyyyyyyyyyyyy")     
     print(publickey)
     for pvk_tuple in result:
         #print(pvk)  
         pvk = pvk_tuple[0]       
         if pvk == publickey:
             i = True
             print("matched")
         else:
             i = False      

     _conn.commit()
     _conn.close()
     if (i ==True):
        return i
     else:
        return x

def algo(filename,hsmsg,publickey):
     _conn = sqlite3.connect(user_db_file_location)
     _c = _conn.cursor()
     i =check(hsmsg,publickey)
     data= ''
     
     if i == True:
         _c.execute("select data from cloudadata where filename='"+filename+"'  and hsmsg='"+hsmsg+"'")
         result = _c.fetchall()
         data=result
         _conn.commit()
         _conn.close()
     return i,data 



if __name__ == "__main__":
    print(db_connect())