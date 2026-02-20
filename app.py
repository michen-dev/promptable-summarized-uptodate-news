from flask import Flask, render_template, url_for, request, jsonify
from functions.ai_agent import AI_Agent
from functions.request_data import requests_data
from functions.hash_url import hash_url
from functions.get_content import get_content
from functions.manage_database import Database

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/generate", methods=["POST"])
def generate():
    try:
        data = request.get_json()
        category = data["option"]
        prompt = data["prompt"]

        ai_agent = AI_Agent()
        keyword = ai_agent.get_keyword(prompt)
        data = requests_data(category, keyword)
        res = []
        db = Database()
        db.set_collection(category)
        for d in data:
            if len(res) >= 5:
                break
            _id = hash_url(d["url"])
            fetched_data = db.get_data(_id)
            if fetched_data:
                res.append(fetched_data)
                print(fetched_data["summary"])
            else:
                content = get_content(d["url"])
                if not content:
                    continue
                summary = ai_agent.summarize(content)
                d["summary"] = summary
                d["_id"] = _id
                res.append(d)
                db.store_data(d)
        return jsonify({'status': 'success', 'articles': res})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)