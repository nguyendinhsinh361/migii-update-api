import numpy as np


def get_group_ids_of_question_test(data):
    all_ids = []
    for activity in data:
        for content in activity['content']:
            all_ids.extend([question['id']
                           for question in content['Questions']])
    return np.array(all_ids).tolist()


def find_object_by_id(data, target_id):

    for item in data:
        for content_item in item['content']:
            for question in content_item['Questions']:
                if question['id'] == target_id:
                    return question
    return None


def update_value(data, target_id, general_update, content_update):

    for item in data:
        for content_item in item['content']:
            for question in content_item['Questions']:
                if question['id'] == target_id:
                    question["general"] = general_update
                    question["content"] = content_update
                    return data
    return None


def are_values_equal(obj1, obj2):
    if (not obj1 and not obj2):
        return True
    values1 = [str(val) for val in obj1.values() if val]
    values2 = [str(val) for val in obj2.values() if val]
    return values1 == values2


def are_values_equal_content(obj1, obj2):
    check = False
    if (not obj1 and not obj2):
        return True
    for tmp1, tmp2 in zip(obj1, obj2):
        values1 = [str(val) for val in tmp1.values() if val]
        values2 = [str(val) for val in tmp2.values() if val]
        check = values1 == values2
    return check
