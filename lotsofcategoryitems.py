from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, CategoryItem, User

engine = create_engine('sqlite:///catalogitem1.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
User1 = User(
    name="Robo Barista",
    email="tinnyTim@udacity.com",
    picture='''https://pbs.twimg.com/profile_images/
    2671170543/18debd694829ed78203a5a36dd364160_400x400.png'''
    )

session.add(User1)
session.commit()

# Category for Soccer
category1 = Category(user_id=1, name="Soccer")
session.add(category1)
session.commit()

# adding Soccer item 1:soccer ball
categoryItem1 = CategoryItem(
    user_id=1,
    title="Soccer Ball",
    description="soccer ball",
    category=category1,
    image=""
    )

session.add(categoryItem1)
session.commit()

# adding Soccer item 2: gloves
categoryItem2 = CategoryItem(
    user_id=1,
    title="Goal Keeper Gloves",
    description="the goal keeper gloves with super cushion",
    category=category1,
    image=""
    )

session.add(categoryItem2)
session.commit()


# basketball Category
category2 = Category(user_id=1, name="Basketball")
session.add(category2)
session.commit()

# adding Basket item 1: ball
categoryItem1 = CategoryItem(
                    user_id=1,
                    title="Basket Ball",
                    description="basket ball training",
                    category=category2, image=""
                )

session.add(categoryItem1)
session.commit()

# adding basket item 2: the hop
categoryItem2 = CategoryItem(
                        user_id=1,
                        title="Basket Hop",
                        description="el aro0",
                        category=category2, image=""
                    )

session.add(categoryItem2)
session.commit()

print "added category items!"
