from flask import Flask, jsonify, redirect
from scrapper import News

app = Flask(__name__)

@app.route('/', methods=['GET'])
def defaultRoute ():
    return jsonify({
        'author'      : 'Manoj T',
        'website'     : 'https://manojtummala.github.io',
        'email'       : 'tummmalamanoj2002@gmail.com',
        'Project-Name': 'Sathyabama-Event-API'
    })

######################
#       NEWS         #
######################

@app.route('/news', methods=['GET'])
def newsRoute ():
    result = News.getnews()
    return jsonify(result)

######################
#       EVENTS       #
######################

@app.route('/events', methods=['GET'])
def eventRoute ():
    result = News.getevents()
    return jsonify(result)

# ######################
# #         404        #
# ######################
# @app.route('/<path:dummy>')
# def fallback(dummy):
#     return redirect("http://manojtummala.github.io/IITBBSNewsAPI")

######################
#       HEALTH       #
######################

@app.route('/health', methods = ['GET', 'POST']) 
def health():
    return "working !!!"
    


######################
#    START FLASK     #
######################

if __name__ == "__main__":
	app.run()
