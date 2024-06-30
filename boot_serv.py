from flask import Flask, render_template

bootstrap = Flask(__name__)

@bootstrap.route('/')
def returnBootstrap():
    return render_template("bootstrap.html")

if __name__ == '__main__':
    bootstrap.run(host='0.0.0.0', port=81)
