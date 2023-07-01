from flask import Flask,request,json
from countconso import consonant_count
app=Flask(__name__)

@app.route("/", methods=["POST"])
def fn():
    return consonant_count(request.data)


if __name__ == "__main__":
    app.run(host="localhost",port=4321)