from flask import Flask, render_template, request
from search_eng import search, search_met

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def search_box():
    if request.method == "POST":
        query = request.form["searchTerm"]
        res = search(query)
        hits = res["hits"]["hits"]
        aggs = res["aggregations"]
        num_results = len(hits)
        return render_template(
            "index.html", query=query, hits=hits, num_results=num_results, aggs=aggs
        )
    if request.method == "GET":
        return render_template("index.html", init="True")


@app.route("/metaphor", methods=["POST", "GET"])
def search_box_metaphor():
    if request.method == "POST":
        query = request.form["searchTermMet"]
        res = search_met(query)
        hits = res["hits"]["hits"]
        aggs = res["aggregations"]
        num_results = len(hits)
        return render_template(
            "index.html", query=query, hits=hits, num_results=num_results, aggs=aggs
        )
    if request.method == "GET":
        return render_template("index.html", init="True")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
