from flask import render_template
from flask.views import View
from flask import request
from kat import mongo
import json


class TranscriptProcessor(View):

    methods = ['GET', 'POST']

    def dispatch_request(self):
        '''
        '''
        #Convert the Transcript to JSON
        transcript = json.loads(request.data)

        #If transcript is set, insert the json to mongodb
        if transcript:
            mongo.db.transcripts.insert(transcript)
        print(transcript)
        return render_template('form.html')
