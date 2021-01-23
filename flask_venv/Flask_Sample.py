'''example
u can use requests library to do this operation.

GET
    http://localhost:8003/
    http://localhost:8003/Deepak
    http://localhost:8003/hello?name=Luis

POST
    http://localhost:1234/messages
    H "Content-type: application/json" or "Content-type: text/plain"
    body '{"message":"Hello Data"}

html:

'''

#Note : Create templates folder and dump html files insidepos

from flask import request,Flask,json,render_template,jsonify


app = Flask(__name__)
@app.route('/',methods = ['GET','POST'])
def index():
    if request.method=="GET":return render_template('input.html')
    elif  request.method=="POST":
        data = request.form
        fname = data['fname']
        sname = data['sname']
        return render_template("output.html", first_name=fname, sec_name=sname)

@app.route("/<string:resource>/", methods = ['GET','POST'])
def api_hello(resource):
    if resource == "deepak":return render_template('deepak.html', name="test")
    elif 'name' in request.args and request.method=='GET':return 'who is ' + request.args['name']
    elif request.method == 'POST':
        if request.headers['Content-Type'] == 'text/plain':return "Text Message: " + str(request.data)
        elif request.headers['Content-Type'] == 'application/json': return "JSON Message: " + json.dumps(request.json)
    else:return "did u mean -- 0.0.0.0:port_num/{}?name=something".format(resource)

@app.errorhandler(500)
def not_found(error=None):
    message = {  'status': 500,  'message': 'Not Found: ' + request.url}
    resp = jsonify(message)
    resp.status_code = 500
    return resp


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8003)