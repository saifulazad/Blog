from flask import render_template, flash, redirect, session, g

from app import app, login_manager
from app import models
from .forms import LoginForm

@app.before_request
def call():
    session['user_id'] = 1
    print 'before'
    id =  session.get('user_id')
    print id

    g.user =  models.User.query.get(id)


    print 'endbefore'
    # user = login_manager.user_callback()
    #
    # print user.email
@login_manager.user_loader
def user_loader(id):

    return models.User.query.get(id)

@app.route('/')
def post():
    return render_template('post.html')


