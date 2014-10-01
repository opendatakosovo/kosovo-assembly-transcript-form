#-*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import DateField, TextAreaField, TextField


class TranscriptForm(Form):

    data = DateField('Data')
    agenda = TextAreaField('Agjenda')
    speaker = TextField('Speaker')
    speech = TextAreaField('Speech')
    main_speaker = TextField('Main Speaker')
