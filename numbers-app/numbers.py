from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
	return 'Something Super Awesome At Root Level!'

if __name__ == '__main__':
	app.run()

