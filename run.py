#!flask/bin/python
from app import app, models,db
#
# user = models.User(email='Hi', username='Hi')
#
# db.session.add(user)
# db.session.commit()
#
# print models.User.query.filter_by(email='Hi').first()

app.run(debug=True)
