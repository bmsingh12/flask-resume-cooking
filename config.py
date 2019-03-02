import os

class Config(object):
    SECRET_KET = os.environ.get('SECRET_KEY') or 'resume-cooking-app'