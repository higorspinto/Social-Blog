# \social_blog\api\blog_posts.py

from flask_restful import Resource
from social_blog.models import BlogPost


class AllPostsAPI(Resource):

    def get(self):

        blog_posts = BlogPost.query.all()
        if blog_posts:
            return [blog_post.json() for blog_post in blog_posts]
        else:
            return {'result' : None}, 404


class BlogPostAPI(Resource):

    def get(self, blog_post_id):

        blog_post = BlogPost.query.get(blog_post_id)
        if blog_post:
            return blog_post.json()
        else:
            return {'result' : None}, 404

