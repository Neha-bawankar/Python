from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    age = Column(Integer)


# Create an engine and a session
engine = create_engine('sqlite:///example.db')
Session = sessionmaker(bind=engine)
session = Session()

# Create the users table if it does not exist
Base.metadata.create_all(engine)


def update_user(user_id, new_name, new_age):
    # Fetch the user record to be updated
    user = session.query(User).filter_by(id=user_id).first()

    if user:
        # Update the user record
        user.name = new_name
        user.age = new_age
        session.commit()
        print(f"User {user_id} updated successfully.")
    else:
        print(f"User {user_id} not found.")


# Example usage
update_user(1, "Updated Name", 30)