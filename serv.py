# MSN TV 2 server
# By yourlocaltoaster (https://github.com/yourlocaltoaster0)

#TODO:
# Figure out how to validate BoxId's [Not Done]
# Figure out what to send back to the MSN TV 2 box. [Done] (Thanks to @msntv2 on discord) 
# Add HTTPS? [Not Done]
# TO DO last updated: 05/12/2024 @ 10:12


from flask import Flask, Response, render_template

app = Flask(__name__)

# /boxcheck and /usercheck will be handled by DNS to point to the right configuration.
@app.route('/')
def returnBootstrap():
     return render_template("/service/bootstrap.html")

@app.route('/boxcheck')
def returnBootstrap():
     return render_template("/service/boxcheck_mock.html")      

@app.route('/usercheck')
def returnBootstrap():
     return render_template("/service/usercheck_mock.html")                                          

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=False)
    
