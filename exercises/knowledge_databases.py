from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(topic,title,rating):
    knowledge = Knowledge(
        topic=topic,
        title=title,
        rating=rating)
    session.add(knowledge)
    session.commit()

add_article("weather","rain",8)

def query_all_articles():
    knowledge= session.query(Knowledge).all()
    return knowledge

def query_article_by_topic(topic):
    knowledge = session.query(Knowledge).filter_by(
       topic=topic).first()
    return knowledge

print(query_article_by_topic("weather"))

def delete_article_by_topic(topic):
    session.query(Knowledge).filter_by(
       topic=topic).delete()
    session.commit()

delete_article_by_topic("weather")

def delete_all_articles():
    session.query(Knowledge).delete()
    session.commit()

delete_all_articles()

def edit_article_rating(update_rating,article_title):
    knowledge = session.query(Knowledge).filter_by(
        rating=update_rating,title=article_title).all()
    session.commit()

edit_article_rating(10,"wow")
    
