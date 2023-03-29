from djf_surveys.models import Answer
from .models import DeveloperImage

def get_dev_details(num=17):
    answers = Answer.objects.filter(user_answer_id=num)
    photo = DeveloperImage.objects.filter(answer_id_id=num) 
    print(answers[0].value,"****",photo[0].developer_image)

# get_dev_details()