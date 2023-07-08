from flask import Flask,request,json
from countconso import consonant_count
app=Flask(__name__)

@app.route("/", methods=["POST"])
def fn():
    ip=request.data.decode('ascii')
    print(f"input = {ip}")
    return str(consonant_count(str(ip)))


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=4321)