from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL

# Create your models here.

class QuizModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # state_image = models.BooleanField(default=False)
    # state_mcq = models.BooleanField(default=False)
    # state_text_response = models.BooleanField(default=False)
    # state_option_nota = models.BooleanField(default=False)    
    poller = models.CharField(max_length=150, null=True)
    quiz_title = models.CharField(max_length=100, null=True)
    question = models.CharField(max_length=250, null=True)
    image = models.ImageField(upload_to='quiz_images', blank=True, null = True)  ## To make ("ImageField / FileField") 'Optional' then add [ blank=True, null=True ] in "models.py" and use ["request.FILES.get('image_field_name')"] while manually catching and saving the value of "image_field_name" from HTML Form in "views.py".
    text_response = models.CharField(max_length=300, null=True)  ## It will now be used for storing "pseudo_correct_answer" for each response for each question.
    option_one = models.CharField(max_length = 30, null=True)
    option_two = models.CharField(max_length = 30, null=True)
    option_three = models.CharField(max_length = 30, null=True)
    option_four = models.CharField(max_length = 30, null=True)
    option_five = models.CharField(max_length = 30, null=True)
    option_six = models.CharField(max_length = 30, null=True)
    option_one_count = models.PositiveIntegerField(default = 0)
    option_two_count = models.PositiveIntegerField(default = 0)
    option_three_count = models.PositiveIntegerField(default = 0)
    option_four_count = models.PositiveIntegerField(default = 0)
    option_five_count = models.PositiveIntegerField(default = 0)
    option_six_count = models.PositiveIntegerField(default = 0)
    correct_option = models.CharField(max_length = 300, null=True)    
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)


    def quiz_mcq_total(self):
        return self.option_one_count + self.option_two_count + self.option_three_count + self.option_four_count + self.option_five_count + self.option_six_count


    class Meta:
        db_table = 'quiz_table_temp'