from django.db import models

# Create your models here.

class PollModel(models.Model):
    poll_id = models.AutoField(primary_key = True)    
    question = models.TextField(max_length = 100)
    user_id = models.CharField(max_length = 10)        
    state_option_four = models.BooleanField(default = True, blank = True)
    option_one = models.CharField(max_length = 30)
    option_two = models.CharField(max_length = 30)
    option_three = models.CharField(max_length = 30)
    option_one_count = models.PositiveIntegerField(default = 0)
    option_two_count = models.PositiveIntegerField(default = 0)
    option_three_count = models.PositiveIntegerField(default = 0)
    option_four_nota_count = models.PositiveIntegerField(default = 0)


    def total(self):
        return self.option_one_count + self.option_two_count + self.option_three_count + self.option_four_nota_count


    class Meta:
        db_table = 'poll_table_temp'