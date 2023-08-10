import json

from flask import Flask, render_template

app = Flask(__name__)


class Post:
    def __init__(self, id, title, subtitle, body):
        self.id = id
        self.title = title
        self.subtitle = subtitle
        self.body = body


class BlogData:
    def __init__(self, post_data):
        self._posts = [Post(post["id"], post["title"], post["subtitle"], post["body"]) for post in post_data]

    def get_all_posts(self):
        """Return a list of all blog posts."""
        return self._posts

    def get_post_by_id(self, post_id):
        """Return a specific post by its ID."""
        for post in self._posts:
            if post.id == post_id:
                return post
        return None


# Load the blog posts from the JSON file
with open("blog_posts.json", "r") as file:
    posts_data = json.load(file)

blog_data = BlogData(posts_data)


@app.route('/')
def home():
    """Render the homepage with a list of all blog posts."""
    return render_template("index.html", all_posts=blog_data.get_all_posts())


@app.route('/post/<int:post_id>')
def get_post(post_id):
    """Render a specific blog post by its ID."""
    post = blog_data.get_post_by_id(post_id)
    if post is None:
        return render_template("404.html", message="A post with that id was not found.")
    else:
        return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)
