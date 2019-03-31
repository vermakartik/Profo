from CTest import models as ctest_models
def evaluate(response_set, test_id):
    # this function will actually evaluate the test sheet and provide the result
    test_obj = ctest_models.Test.objects.get(id = test_id)
    total_count = test_obj.question_set.all().count()
    question_items = response_set.items()
    corrects = 0
    for item in question_items:
        if item[0].startswith('question'):
            question_id = item[0].split("_")[1]
            response = item[1]
            question_obj = ctest_models.Question.objects.get(id = question_id)
            answer_id = question_obj.answer_set.all().filter(id = response)[0]
            print(answer_id)
            if answer_id.is_answer_correct == True:
                corrects += 1
    print(total_count, test_obj)
    return {"total_count": total_count, "correct": corrects}