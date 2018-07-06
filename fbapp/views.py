#coding: utf-8
import logging
from flask import Flask, render_template, url_for, request
#import utils   
#from .utils import OpenGraphImage 
app = Flask(__name__)

app.config.from_object(u'config')

@app.route('/')
@app.route(u'/index/')
def index():
    description = u"""
            Toi, tu sais comment utiliser la console ! Jamais à court d'idées pour réaliser ton objectif, tu es déterminé-e et persévérant-e. Tes amis disent d'ailleurs volontiers que tu as du caractère et que tu ne te laisses pas marcher sur les pieds. Un peu hacker sur les bords, tu aimes trouver des solutions à tout problème. N'aurais-tu pas un petit problème d'autorité ? ;-)
        """

    if "img" in request.args:
        img = request.args['img']
        og_img = url_for('static', filename = img, _external = True ) 
        og_url = url_for("index", img = img, _external = True)
    


    else:

        

        og_img = url_for('static', filename = "tmp/sample", _external = True ) 
        og_url = url_for("index",  _external = True)
      
    return render_template(u"index.html",
                            user_name = u"names",
                            user_image = url_for(u"static", filename = u"img/profile.png"),
                            description = description,
                            blur = True,
                            og_url = og_url,
                            og_img = og_img)


@app.route(u'/result/')

def result():
    description = u"""
        Toi, tu n'as pas peur d'être seul ! Les grands espaces et les aventures sont faits pour toi. D'ailleurs, Koh Lanta est ton émission préférée ! Bientôt tu partiras les cheveux au vent sur ton radeau. Tu es aussi un idéaliste chevronné. Quelle chance !
    """
    #print "route demandée: {}, méthode utilisée: {}, params: {}".format(request.path, request.method, request.args)
     
    var = request.args.get('gender')
    print "var: ",var
    #user_name = request.args.get('first_name')
    gender = 0 if var == "female" else 1    
    user_name = utils.find_content(gender)
    uid = request.args.get('id')
    profile_pic = u'http://graph.facebook.com/' + uid + '/picture?type=large'

    img = OpenGraphImage(uid, user_name, description).location
    og_url = url_for("index", _external = True, img = img ) 
    return render_template(u"result.html",
                            user_name = user_name,
                            user_image= profile_pic,
                            description=description,
                            og_url = og_url)

#if(__name__) == "__main__":
#    app.run()