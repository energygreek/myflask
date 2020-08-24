from flask import Blueprint, render_template
from myflask.util.blog_dbmanager import BlogSQL

blog = Blueprint("blog", __name__)


@blog.route("/", methods=('GET', 'POST'))
def index():
    blog_manager = BlogSQL()
    blog = blog_manager.query_by_id(blog_id= 1)
    #return render_template(title = blog.title, content=blog.content)
    return render_template("blog.html", title = "博客", content="正文")