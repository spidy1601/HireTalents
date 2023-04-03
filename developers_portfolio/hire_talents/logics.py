from djf_surveys.models import Answer
from .models import DeveloperImage

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