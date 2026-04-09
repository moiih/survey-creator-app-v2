from django import template
# from quiz.views import chart_stats_ctags
from quiz.views import chart_stats_ctags_1, chart_stats_ctags_2


#  Registering New Django Template Tags And Functions Here.

register = template.Library()


@register.filter
def add_ques_mark(string_value):

    chk = 0
    if string_value[len(string_value)-1:] != '?':

        string = string_value.split(' ')
        question_words = ['what', 'which', 'where', 'when', 'who', 'whom', 'whose', 'how', 'do', 'does', 'did']

        for s in string:
            if question_words.count( s.lower() ) > 0:
                chk = 1
                break

    if chk == 1:
        return string_value + ' ?'
    else:
        if string_value[len(string_value)-1 : len(string_value)] == '?':
            return string_value[:len(string_value)-1] + ' ?'
        else:
            return string_value



@register.filter
def upper_first_letter(string_value):

    string_value = str(string_value)

    if string_value[:1].islower():
        temp1 = string_value[1:]
        temp2 = string_value[:1].upper()

        # print('\nFirst Letter Question :', temp2+temp1, end='\n\n\n')
        return temp2 + temp1
    
    else:
        return string_value


@register.filter
def get_right_ans(objects_value):
    # print(objects_value)
    # print(objects_value[0].poller)
    # stats = []
    right = 0
    # wrong = 0    
    for record in objects_value:
        if record.correct_option == record.text_response:
            right += 1        
    # stats.append(right)
    # stats.append(wrong)
                    
    return right



@register.filter
def get_wrong_ans(objects_value):    
    wrong = 0    
    for record in objects_value:
        if record.correct_option != record.text_response:
            wrong += 1            
                    
    return wrong




@register.filter
def get_wrong_ans_beta(value):
    # print(value)
    # dataArray = chart_stats_ctags()
    # poll_data = dataArray[1]
    # end = (int(value) * dataArray[0]) - 1      
    # start = (end+1) - dataArray[0]
    # print('\nStart =', start)
    # print('\nEnd =', end)    
    
    # # t_right = 0
    # t_wrong = 0
    # for i in range(start, end+1):
    #     if dataArray[1]:
    #         print('~~~~ t_Text_Response =', poll_data[i].text_response)        
    #         if poll_data[i].text_response != 'NULL':
    #             if  poll_data[i].correct_option != poll_data[i].text_response:
    #                 t_wrong += 1
    #                 # t_right += 1
    #             # else:
    #             #     t_wrong += 1
                                    

    # # print('----- t_right =', t_right)
    # print('----- t_wrong =', t_wrong)    
    # return t_wrong


    
    data_length = chart_stats_ctags_1()
    poll_data = chart_stats_ctags_2()
    end = (int(value) * data_length) - 1      
    start = (end+1) - data_length
    print('\nStart =', start)
    print('\nEnd =', end)    
    
    # t_right = 0
    t_wrong = 0
    for i in range(start, end+1):
        if poll_data:
            print('~~~~ t_Text_Response =', poll_data[i].text_response)        
            if poll_data[i].text_response != 'NULL':
                if  poll_data[i].correct_option != poll_data[i].text_response:
                    t_wrong += 1
                    # t_right += 1
                # else:
                #     t_wrong += 1
                                    

    # print('----- t_right =', t_right)
    print('----- t_wrong =', t_wrong)    
    
    return t_wrong





@register.filter
def get_right_ans_beta(value):
    # print(value)
    # dataArray = chart_stats_ctags()
    # poll_data = dataArray[1]
    # end = (int(value) * dataArray[0]) - 1
    # start = (end+1) - dataArray[0]
    # print('\nStart =', start)
    # print('\nEnd =', end)    

    # global myCtag
    # t_right = 0    
    # for i in range(start, end+1):
    #     if dataArray[1]:
    #         print('~~~~ t_Text_Response =', poll_data[i].text_response)
    #         if poll_data[i].text_response != 'NULL':
    #             if poll_data[i].correct_option == poll_data[i].text_response:
    #                 t_right += 1      


    # print('----- t_right =', t_right)
    
    # return t_right






    data_length = chart_stats_ctags_1()
    poll_data = chart_stats_ctags_2()
    end = (int(value) * data_length) - 1      
    start = (end+1) - data_length
    print('\nStart =', start)
    print('\nEnd =', end)    
    
    t_right = 0
    # t_wrong = 0
    for i in range(start, end+1):
        if poll_data:
            print('~~~~ t_Text_Response =', poll_data[i].text_response)        
            if poll_data[i].text_response != 'NULL':
                if  poll_data[i].correct_option == poll_data[i].text_response:                    
                    t_right += 1                
                                    

    print('----- t_right =', t_right)
    # print('----- t_wrong =', t_wrong)    
    
    return t_right