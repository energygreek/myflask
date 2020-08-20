from flask import Blueprint, redirect, request, url_for, render_template

blog = Blueprint("blog", __name__)

@blog.route("/<blog_id:int>", methods=('GET','POST'))
def log(blog_id):
    return render_template()