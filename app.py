from flask import Flask
from flask import render_template
from peewee import *
app = Flask(__name__)

db = SqliteDatabase('foreclosures.db')

class Notice(Model):
    id = IntegerField(unique=True)
    zip = CharField()
    month = DateField()
    notices = IntegerField()

    class Meta:
        table_name = "notices"
        database = db

@app.route("/")
def index():
    print("Total number of notices is", Notice.select().count())
    notice = Notice.select().where(Notice.id==3963).get()
    print(f"Zip code {notice.zip} had {notice.notices} in {notice.month}")
    notices_20906 = Notice.select().where(Notice.zip=='20906')
    for notice in notices_20906:
    print(notice.notices)
    template = 'index.html'
    return render_template(template)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)