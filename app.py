from flask import Flask , render_template
import requests

app = Flask(__name__)


@app.route("/")
def index():
    
    url = "Enter your news api"
    """ That is example of api Not a correct api
    # url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=25fd49e6d9474fce8d92"
    """
    r=requests.get(url).json()
    cases = {
        'articles':r['articles']
        }
    
    return render_template("index.html", case  =cases)

if __name__ =="__main__":
    app.run(debug=True)