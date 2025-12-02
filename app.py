from flask import Flask, render_template
import feedparser

app = Flask(__name__)

@app.route('/')
def index():
    feed_url = 'https://static.cricinfo.com/rss/livescores.xml'
    feed = feedparser.parse(feed_url)
    return render_template('index.html', matches=feed.entries)

if __name__ == '__main__':
    app.run(debug=True)
