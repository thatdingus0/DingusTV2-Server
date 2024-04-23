# MSN TV 2 server
# By thatdingus (https://github.com/thatdingus0)
# This server isn't perfect yet. It will be fixed whenever I get a MSN TV 2 box.

#TODO:
# Figure out how to validate BoxId's [Not Done]
# Figure out what to send back to the MSN TV 2 box. [Not Done]
# Make a better auth system [Not Done] 
# Add HTTPS? [Not Done]
# TO DO last updated: 04/23/2024 @ 17:29


from flask import Flask, Response, request

app = Flask(__name__)

def checkBoxId(BoxId):
    # TODO 
    pass

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
    # The first two lines are probably going to stay the same
    # Any strings with "" is not checked because I don't know what to put here
    if phase.lower() == "boxcheck":
        if purpose.lower() == "authorize":
            print(BoxId)
            if BoxId == any:
                if WANProvider == "":
                    if version == "": 
                        if ConnectorName == "": 
                            if domain == "": #
                                if NightlyEnabled == "":
                                    if x == "y": 
                                        return Response("auth=true") # Placeholder string
                                else:
                                    return Response("No NightlyEnabled in query string.")
                            else:
                                return Response("No domain in query string.")
                        else:
                            return Response("No ConnectorName in query string.")   
                    else:
                        return Response("No version in query string.")
                else:
                    return Response("No WANProvider in query string.")
            else:
                return Response("No BoxID in query string.")
        else:
            return Response("No purpose in query string.")
    else:
        return Response("No phase in query string.")
                                          

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=False)
    
