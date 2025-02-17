from flask import Flask, render_template, request
import requests

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/674f5423f73deab1e9a7").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route("/form-login", methods=["POST"])
def recieve_data():
    print(request.form["name"])
    print(request.form["email"])
    print(request.form["phone"])
    print(request.form["message"])
    return f"<h1>Submitted response!</h1>"
   



if __name__ == "__main__":
    app.run(debug=True, port=5001)
