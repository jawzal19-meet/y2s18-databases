from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
    __tablename__ = 'Knowledge'
    knowledge_id= Column(Integer, primary_key=True)
    topic = Column(String)
    title = Column(String)
    rating = Column(Integer)

	# Create a table with 4 columns
	# The first column will be the primary key
	# The second column should be a string representing
	# the name of the Wiki article that you're referencing
	# The third column will be a string representing the 
	# topic of the article. The last column will be
	# an integer, representing your rating of the article.

#    def __repr__(self):
#     	if slef.rating<7:
#      return ("If you want to learn about " +self.topic + ", you should look at the Wikipedia article called +self.title+  We gave this article a rating of +self.rating")
#         else:
#         	return ("Unfortunately, this article does not have a better rating. Maybe, this is an article that should replaced soon!.")
def __repr__(self):
       return ("knowledge_id: {}\n"
       		   "topic: {}\n"
               "title: {} \n"
               "rating: {}").format(
                    self.knowledge_id, self.topic, self.title, self.rating)

Knowledge1 = Knowledge(knowledge_id = 1, topic="weather", title="rainbow", rating=9 )
#print(Knowledge1)

