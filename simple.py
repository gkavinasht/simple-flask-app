from flask import Flask
from flask import render_template
from argparse import ArgumentParser

app = Flask(__name__)

parser = ArgumentParser()
parser.add_argument('--name')
args = parser.parse_args()

@app.route("/")
@app.route("/<name>")
def hello_msg(name=None):
	return render_template('hello.html', name=name if args.name is None else args.name)

if __name__ == "__main__":
   app.run(host='0.0.0.0', debug=True)