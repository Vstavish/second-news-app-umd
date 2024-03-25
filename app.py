from flask import Flask
from flask import render_template
from peewee import *
app = Flask(__name__)  # Note the double underscores on each side!

db = SqliteDatabase('foreclosures.db')

class Notice(Model):
    id = IntegerField(unique=True)
    zip = CharField()
    month = DateField()
    notices = IntegerField()

    class Meta:
        database = db

@app.route("/")
def index():
    notice_count = Notice.select().count()
    notices_20906 = Notice.select().where(Notice.zip=='20906')
    template = 'index.html'
    return render_template(template, count = notice_count, notices = notices_20906)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)