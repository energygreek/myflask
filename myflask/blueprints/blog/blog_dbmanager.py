from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from flask import current_app

Base = declarative_base()


# concret class
class Blog(Base):
    __tablename__ = 'blogs'
    # set id column as primary key
    blog_id = Column(Integer, primary_key=True)
    # specify name to name column
    title = Column(String(32))
    content = Column(String(32))


class BlogSQL:

    def __init__(self):
        self._engine = create_engine(
            current_app.config['SQLALCHEMY_BLOG_DATABASE_URI'], echo=True)
        # create table
        Base.metadata.create_all(self._engine)
        self._session_maker = sessionmaker(bind=self._engine)


    def add_user(self, blog: Blog):
        try:
            session = self._session_maker()
            session.add(blog)
            session.commit()
            session.close()

        # exception
        print('Exception occur')
        return None

    def query_user_by_id(self, blog_id):
        # fetch only one record use where
        with self._session_maker() as session:
            u = session.query(Blog).filter(Blog.blog_id == blog_id).one()
            user = {'id':u.id, 'name':u.name, 'password':u.password}

            session.commit()
            session.close()
            return user
        # exception
        print('Exception occur')
        return None

    def query_user_by_title(self, title):
        with self._session_maker() as session:
            u = session.query(Blog).filter(Blog.title == title).one()
            blog = {'blog_id':u.blog_id, 'title':u.title, 'content':u.content}

            session.commit()
            session.close()
            return blog
        # exception
        print('Exception occur')
        return None

    def delete_blog(self, blog_id):
        with self._session_maker() as session:
            u = session.query(Blog).filter(Blog.id == blog_id).one()
            session.delete(u)
            session.commit()
            session.close()

        # exception
        print('Exception occur')
        return None

# su = SysUser(id=2,name='John',password='123')
# add_user(su)
