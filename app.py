import openai
import os

app = Flask(__name__)

openai.api_key = os.environ.get("OPENAI_API_KEY")

def summarize_text(text):
    prompt = f"Please summarize the following text in 30-60 words:\n{text}\nSummary:"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.5,
    )
    summary = response.choices[0].text.strip()
    return summary

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sub", methods=["POST"])
def summarize():
    sourcename = request.form["source-name"]
    sourcelink = request.form["source-link"]

    
    text = request.form["newstext"]
    summary = summarize_text(text)
    return render_template("uploadblog.html", summary=summary, sname=sourcename, slink=sourcelink)
    
    

@app.route("/uploadblog", methods=["POST"])
def upload():
    sourcename = request.form["source-name"]
    sourcelink = request.form["source-link"]
    text = request.form["newstext"]
    img = request.form["news-image"]    

if __name__ == "__main__":
    app.run(debug=True)
    
    
  