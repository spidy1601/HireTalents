from operator import methodcaller
from djf_surveys.models import Answer,Question
from .models import DeveloperImage
from django.db.models.functions import Lower

def get_dev_details(nums=[22]):
    '''[[photo(url of the image),answers(queryset)],[img,ans]]'''
    all_dev_details = []
    for num in nums:
        one_dev_details = []
        answers = Answer.objects.filter(user_answer_id=num)
        photo = DeveloperImage.objects.filter(answer_id=num) 
        one_dev_details.append(photo)
        one_dev_details.append(answers)
        all_dev_details.append(one_dev_details)
    return all_dev_details 

#cc= get_dev_details()
#cc[0][1][0].value 
#cc[which user][which type of detail(image or answers)][(0,0..list)]


def search_dev(client_skills=['PyThOn','javascript','reactjs']):
    cleaned_skills = list(map(str.lower,client_skills))
    all_skills = Answer.objects.filter(question_id=19).values_list(Lower('value'),flat=True)

    # convert all the skills in dev_skills to lowercase
    dev_skills = list(map(methodcaller('split',','),all_skills))

    # iterate through dev_skills and check if all skills in skills are present in each sublist
    selected_dev_id = [all_skills[i].user_answer_id for i, skill_set in enumerate(dev_skills) if all(skill in skill_set for skill in cleaned_skills)]

    return selected_dev_id