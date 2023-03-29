from djf_surveys.models import Answer
from .models import DeveloperImage

def get_dev_details(num=17):
    '''[answers(queryset),photo(url of the image)]'''
    dev_details = []
    answers = Answer.objects.filter(user_answer_id=num)
    photo = DeveloperImage.objects.filter(answer_id_id=num) 
    dev_details.append(answers)
    dev_details.append(photo)
    return dev_details 

# get_dev_details()