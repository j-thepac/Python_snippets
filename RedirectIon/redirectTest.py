# gunicorn -w 1 -b 0.0.0.0:5000 'redirectTest:app'
# shortUrl= pyshorteners.Shortener().isgd.short(url) 
# #pyshorteners.Shortener().isgd.expand(shortUrl)


from flask import Flask , redirect,request
import gunicorn
import pyshorteners
import sqlite3 as db
from dataclasses import dataclass
from datetime import datetime

@dataclass
class UrlData():
    url:str
    shortUrl:str


class DB():
    def init(self): 
        self.con= db.connect("UrlDB")
        self.con.execute("Create table if not Exists URL (url string PRIMARY KEY,shortUrl string)")

    def insertUrl(self,urldata:UrlData):
        self.init()
        with self.con:
            self.con.execute(f"insert into URL (url,shortUrl) values('{urldata.url}','{urldata.shortUrl}')")
            self.con.commit()
        return True 
    
    def getUrl(self,shortUrl):
        self.init()
        with self.con:
            res=self.con.execute(f"select url from URL where shortUrl='{shortUrl}'")
        url=list(res)
        return url[0][0]

app = Flask(__name__)
@app.route("/",methods=["POST"])
def fn():
    url=request.json["url"]
    shortUrl=str(datetime.now().timestamp()).replace(".","")
    db=DB()
    db.insertUrl(UrlData(url,shortUrl))
    return "http://0.0.0.0:5000/"+shortUrl

@app.route("/<shortUrl>")
def fn2(shortUrl):
    db=DB()
    url=db.getUrl(shortUrl)
    return redirect(url)

if (__name__=="__main__"):
    app.run(host="0.0.0.0",port=5000,debug=True)


