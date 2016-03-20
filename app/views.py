import dateutil
from flask import render_template, flash, redirect, session, g, request
from flask.helpers import url_for
import flask_login
from sqlalchemy import desc

from app import app, login_manager
from app import models, db
from .forms import LoginForm

# @app.template_filter('strftime')
# def _jinja2_filter_datetime(date, fmt=None):
#     date = dateutil.parser.parse(date)
#     native = date.replace(tzinfo=None)
#     format='%b %d, %Y'
#     return native.strftime(format)


@app.before_request
def call():
    session['user_id'] = 1
    print 'before'
    id =  session.get('user_id')
    print id

    g.user =  models.User.query.get(id)

    g.post = models.Post.query.all()

    print 'endbefore'
    # user = login_manager.user_callback()
    #
    # print user.email











@login_manager.user_loader
def user_loader(id):

    return models.User.query.get(id)


@app.route('/')
def index():

    post = models.Post.query.get(1)


    return render_template('post.html', post = post)



@app.route('/post', methods=['POST'])
def post_comment():

    user_id = int(request.form['user_id'])
    post_id = int(request.form['post_id'])

    user= models.User.query.get(user_id)

    post = models.Post.query.get(post_id)
    print request.form['comment'], request.form['post_id'], request.form['user_id']



    comment = models.Comment(text= request.form['comment'], usr = user)

    post.comments.append(comment)

    db.session.add(comment)
    db.session.commit()
    return redirect(url_for('post',post_id= post_id))

@app.route('/<int:post_id>')
def post(post_id):

    post = models.Post.query.get(post_id)


    return render_template('post.html', post = post)

@app.route('/logout')
def logout():
    #print flask_login.current_user.id
    flask_login.logout_user()
    #print flask_login.current_user.id

    return redirect(url_for('index'))


