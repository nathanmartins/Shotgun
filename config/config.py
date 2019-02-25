import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    UPLOAD_FOLDER = '/tmp/shotgun'
    SQLALCHEMY_DATABASE_URI = 'postgresql://shotgun:shotgun@0.0.0.0/shotgun'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
