from flask import Flask, render_template, request, redirect
from database import collection

app = Flask(__name__)

# Home Page
@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        data = {
            "name": request.form["name"],
            "college": request.form["college"],
            "domain": request.form["domain"],
            "duration": request.form["duration"]
        }

        collection.insert_one(data)
        return redirect("/")

    return render_template("index.html")


# View Page
@app.route("/view")
def view():
    users = collection.find()
    return render_template("view.html", users=users)


if __name__ == "__main__":
    app.run(debug=True)