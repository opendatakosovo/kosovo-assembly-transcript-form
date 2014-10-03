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

        transcript = request.data

        #Convert the Transcript to JSON and insert the json to mongodb
        if transcript:
            mongo.db.transcripts.insert(json.loads(transcript))

        return render_template('form.html')
