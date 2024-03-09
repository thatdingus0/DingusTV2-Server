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
    print(phase,purpose,BoxId,WANProvider,version,ConnectorName,domain,NightlyEnabled,x)
    # Being checking args
    if phase and purpose and BoxId and WANProvider and version and ConnectorName and domain and NightlyEnabled and x == "":
        return Response('Error while checking box. One or more args are missing from the string, please fix and try again.')
    if phase.lower() == "boxcheck":
        if purpose.lower() == "authorize":
            if BoxId: # Every boxid is accepted lmao.
                if WANProvider: # I don't know all the WANProviders yet.
                    if version: # I'm not writing all of the versions out.
                        if ConnectorName: # Again, I don't know all of the connectornames.
                            if domain: # I don't have a MSN TV 2 box, I don't know what to put here.
                                if NightlyEnabled == 0 or 1:
                                    if x == "y":
                                        # congrats, the box is authorized!
                                        return Response("Your box is now authorized")
    

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=False)
