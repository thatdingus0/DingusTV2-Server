# MSN TV 2 server
# By yourlocaltoaster (https://github.com/yourlocaltoaster0)

#TODO:
# Figure out what to send back to the MSN TV 2 box. [Done] (Thanks to @msntv2 on discord) 
# TO DO last updated: 05/12/2024 @ 10:12


from flask import Flask, Response, render_template
import threading

bootstrap = Flask(__name__)
service = Flask(__name__)

# /boxcheck and /usercheck will be handled by dns to point to the right ip.
@bootstrap.route('/')
def returnBootstrap():
     return render_template("bootstrap.html")

@service.route('/')
def returnNilIfNoHTML():
    return Response("No HTML file in path.")

@service.route('/connection/boxcheck_mock.html')
def returnboxcheck():
    return render_template("boxcheck_mock.html")

@service.route('/connection/usercheck_mock.html')
def returnusercheck():
    return render_template("usercheck_mock.html")

@service.route('/connection/kickstart.aspx')
def returnkickstart():
    return render_template('kickstart.aspx')

@service.route('/connection/GatePage.aspx')
def gobacktokickstartnow():
    return render_template("kickstart.aspx")

def run_flask(app, port):
    app.run(host=0.0.0.0', port=port)

if __name__ == '__main__':
    bootstrapThread = threading.Thread(target=run_flask, args=(bootstrap, 80))
    serviceThread = threading.Thread(target=run_flask, args=(service, 8082))
    bootstrapThread.start()
    serviceThread.start()
    bootstrapThread.join()
    serviceThread.join()
