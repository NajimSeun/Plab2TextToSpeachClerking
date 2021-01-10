from Models import *
from peewee import DoesNotExist


class AppController:

    @staticmethod
    def add_topic(topic, cases, conditions_ques_list):

        questions_list = []
        with get_db().atomic():
            topic = Topic.create(name=topic)
            cases_ins_list = [PCase(question=case, topic=topic) for case in cases]
            PCase.bulk_create(cases_ins_list)
            for condition, questions in conditions_ques_list.items():

                condition_inst = Condition.create(name=condition, topic = topic)
                for question in questions:
                    questions_list.append(ClerkingQuestion(question = question , condition = condition_inst))

            ClerkingQuestion.bulk_create(questions_list)

    @staticmethod
    def get_topic_to_study():
        conditions_ques_list = []
        try:
            with get_db().atomic():
                topic = Topic.select().order_by(Topic.num_time_accessed).get()
                topic.num_time_accessed += 1
                topic.save()
                case = PCase.select().join(Topic).where(Topic.id == topic.id).order_by(PCase.num_time_accessed).get()
                case.num_time_accessed += 1
                case.save()
                conditions = Condition.select().join(Topic).where(Topic.id == topic.id)
                for condition in conditions:
                    clerking_questions = ClerkingQuestion.select().where(ClerkingQuestion.condition_id == condition.id)
                    quest_list = [cq.question for cq in clerking_questions]
                    conditions_ques_list.append(ConditionQuestions(condition.name.strip(), quest_list))
                return TopicToStudy(topic.name.strip(), case.question.strip(), conditions_ques_list)
        except DoesNotExist as dne:

            return TopicToStudy()


