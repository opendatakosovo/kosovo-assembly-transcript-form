from flask import render_template
from flask.views import MethodView
from form import TranscriptForm


class TranscriptionFormInterface(MethodView):

    methods = ['GET','POST']

    def get(self):
        '''
        '''
        form = TranscriptForm()
        return render_template(
            'form.html',
            form=form)
    def post():
        print " Update the motherfucking databse"
        form = TranscriptForm()
        for entry in form.speech.data:
            print '{}'.format(entry)
        form.request()
        print form
        return render_template(
            'form.html',
            form=form)
