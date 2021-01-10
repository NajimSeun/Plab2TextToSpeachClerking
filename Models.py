from peewee import *


db = SqliteDatabase("C:/p2t2s/db/p2t2s.db")


class BaseModel(Model):
    class Meta:
        database = db


class Topic(BaseModel):
    name = CharField(unique=True)
    num_time_accessed = IntegerField(default=0)


class PCase(BaseModel):
    question = TextField()
    topic = ForeignKeyField(Topic, backref= "cases")
    num_time_accessed = IntegerField(default=0)


class Condition(BaseModel):
    name = CharField(unique=False)
    topic  = ForeignKeyField(Topic, backref="conditions" )


class ClerkingQuestion(BaseModel):
    question = TextField()
    condition = ForeignKeyField(Condition, backref="clerking_questions")


def get_db():
    return db

class TopicToStudy:
    def __init__(self, topic=" ", case=" ", conditions_ques=None):
        self.topic =topic
        self.case = case
        self.conditions_ques = conditions_ques

    def get_topic(self):
        return self.topic

    def get_case(self):
        return self.case

    def get_conditions_ques(self):
        return self.conditions_ques


class ConditionQuestions:
    def __init__(self, condition, questions):
        self.condition = condition
        self.questions = questions

    def get_condition(self):
        return self.condition

    def get_questions(self):
        return self.questions
