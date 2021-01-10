from Models import *

if __name__ == "__main__":

    db = get_db()
    with db:
        db.create_tables([Topic, PCase, Condition, ClerkingQuestion])