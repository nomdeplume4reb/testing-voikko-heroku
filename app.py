from flask import Flask, render_template, request, redirect
import os

import libvoikko
from libvoikko import Voikko
# v = libvoikko.Voikko(u"fi")

#Voikko.setLibrarySearchPath("/app/Voikko")
#v = libvoikko.Voikko("fi", "/app/Voikko/dict")

app = Flask(__name__)

def practice():
    test = v.analyze('kissoja')[0]
    return test

@app.route("/")
@app.route("/home", methods=["POST", "GET"])
def home():
    #test = practice()
    test='test'
    return render_template('home.html', test=test)

if __name__ == '__main__':
    app.run(debug=False)

# OUTPUT SHOULD BE:
# {'BASEFORM': 'KISSA', 'CLASS': 'NIMISANA', 'FSTOUTPUT': '[LN][XP]KISSA[X]KISS[SP][NM]OJA', 'NUMBER': 'PLURAL', 'SIJAMUOTO': 'OSANTO', 'STRUCTURE': '=PPPPPPP', 'WORDBASES': '+KISSA(KISSA)'}
