import ssl
from flask import Flask, render_template, request

service = Flask(__name__)

@service.route('/')
def returnNilIfNoHTML():
    return render_template('eval.html')

@service.route('/connection/bootstrap.html')
def strap():
    return render_template('boxcheck_shit.html')

@service.route('/connection/boxcheck.html')
def returnboxcheck():
    return render_template("boxcheck.html")

@service.route('/connection/usercheck.html')
def returnusercheck():
    return render_template("usercheck_mock.html")

@service.route('/connection/kickstart.aspx')
def returnkickstart():
    return render_template('kickstart.aspx')


@service.route('/connection/GatePage.aspx', methods=['GET'])
def gate_page():
    if request.args.get('phase') == 'Bootstrap' and request.args.get('purpose') == 'Authorize':
        return render_template('/connection/GatePage.aspx')
    else:
        return render_template('/connection/GatePage.aspx')

if __name__ == '__main__':
    host = '0.0.0.0'
    port = 80
    service.run(host=host, port=port)
