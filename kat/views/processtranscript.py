from flask import render_template
from flask.views import View
from flask import request
from kat import mongo,utils
from slugify import slugify
import json


class TranscriptProcessor(View):

    methods = ['GET', 'POST']

    def dispatch_request(self):
        '''
        '''
        transcripts_cursor = mongo.db.transcripts.find()
        transcript = request.data

        #Convert the Transcript to JSON and insert the json to mongodb
        if transcript:
            mongo.db.transcripts.insert(json.loads(transcript))

        for doc in transcripts_cursor:
            for speaker in doc["speech"]:
                party =  utils.get_mp_party(slugify(speaker["speaker"]), str(speaker["date"])[:4])
                if party == "None":
                    mongo.db.transcripts.update({"speech.speaker": speaker["speaker"],"speech.date": speaker["date"]},{"$set":{"speech.$.party": "Other"}})
                else:
                    mongo.db.transcripts.update({"speech.speaker": speaker["speaker"],"speech.date": speaker["date"]},{"$set":{"speech.$.party": party}})
                print str(speaker["speaker"]) + "s party was set to " + str(party)

        return render_template('form.html')
