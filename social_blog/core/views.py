#social_blog/core/view.py

from flask import render_template, redirect, url_for, request, Blueprint
from social_blog.models import BlogPost
from social_blog.core.forms import BlogPostSearchForm

core = Blueprint('core', __name__)

@core.route('/', methods=["GET","POST"])
def index():
    form = BlogPostSearchForm()

    if form.validate_on_submit():
        search_param = form.search.data
        return redirect(url_for('core.search', search_param=search_param))

    page = request.args.get('page', 1, type=int)
    blog_posts = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=page, per_page=2) 
    return render_template('index.html', form_search=form, blog_posts=blog_posts)

@core.route('/search/<search_param>', methods=["GET","POST"])
def search(search_param):

    form = BlogPostSearchForm()

    if form.validate_on_submit():
        search_param = form.search.data
        return redirect(url_for('core.search', search_param=search_param))

    form.search.data = search_param
    page_search = request.args.get('page', 1, type=int)
    blog_posts = BlogPost.query.whooshee_search(search_param).paginate(page=page_search, per_page=2) 
    
    return render_template('search.html', search_param=search_param, form_search=form, blog_posts=blog_posts)

@core.route('/info')
def info():
    return render_template('info.html')