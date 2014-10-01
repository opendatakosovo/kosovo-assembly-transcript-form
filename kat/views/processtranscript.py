from flask import render_template
from flask.views import MethodView


class TranscriptionFormInterface(MethodView):

    methods = ['GET','POST']

    def get(self):
        '''
        '''
        return render_template('form.html')

    def post():
        print 'index data to ES.'
        return render_template('form.html')
