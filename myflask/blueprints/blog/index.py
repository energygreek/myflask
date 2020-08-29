import uuid

from flask import Blueprint, render_template, request, flash, url_for
from flask_login import current_user, login_required
from werkzeug.utils import redirect

from myflask.util.blog_database import BlogDB, Blog

blog = Blueprint("blog", __name__)


@blog.route("/", methods=('GET', 'POST'))
def index():
    # show all
    posts = BlogDB().query_all()
    return render_template("blog/blog.html", username=current_user, posts=posts)


@blog.route("/<id>", methods=('GET', 'POST'))
def content(id):
    # show all
    posts = BlogDB().query_by_id(id)
    return render_template("blog/blog.html",  posts=posts)


@blog.route("/create", methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = BlogDB()
            db.create_blog(Blog(blog_id=str(uuid.uuid4()),
                                title=title, content=body))
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')


@blog.route("/<int:id>/update", methods=('GET', 'POST'))
@login_required
def update(id):
    blog_manager = BlogDB()
    print(id)
    blog = blog_manager.query_by_id(blog_id= 1)
    #return render_template(title = blog.title, content=blog.content)
    return render_template("blog/blog_content.html", title = "博客", content=id)


@blog.route("/<int:id>/delete", methods=('GET', 'POST'))
@login_required
def delete(id):
    blog_manager = BlogDB()
    print(id)
    blog = blog_manager.query_by_id(blog_id= 1)
    #return render_template(title = blog.title, content=blog.content)
    return render_template("blog/blog_content.html", title = "博客", content=id)
