# MSN TV 2 server
# By thatdingus (https://github.com/thatdingus0)
# This server isn't perfect yet. It will be fixed whenever I get a MSN TV 2 box.

from flask import Flask, Response, request

app = Flask(__name__)

@app.route('/')
def check():
    phase = request.args.get('phase')
    purpose = request.args.get('purpose')
    BoxId = request.args.get('BoxId')
    WANProvider = request.args.get('WANProvider')
    version = request.args.get('version')
    ConnectorName = request.args.get('ConnectorName')
    domain = request.args.get('domain')
    NightlyEnabled = request.args.get('NightlyEnabled')
    x = request.args.get('x')
    # Being checking args
    if phase or purpose or BoxId or WANProvider or version or ConnectorName or domain or NightlyEnabled or x == None:
        return Response('Error while checking box. One or more args are missing from the string, please fix and try again.')
    else:
        if phase.lower() == "boxcheck":
            if purpose.lower() == "authorize":
                if BoxId:
                    if WANProvider: # I don't know what to put here
                        if version: # I'm not writing all of the versions out.
                            if ConnectorName: # Again, I don't know what to put here
                                if domain: # I don't have a MSN TV 2 box, I don't know what to put here.
                                    if NightlyEnabled == 0 or 1:
                                        if x == "y":
                                            # Figure out what to send to the box when it has authorized.
                                            return Response('Box') # Placeholder
                                          

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=False)
    
