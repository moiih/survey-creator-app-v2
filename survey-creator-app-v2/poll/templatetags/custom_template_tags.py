from django import template
from poll.views import pass_to_ttags
# from django.utils.html import mark_safe
# from django.db import connection, Error

#  Registering New Django Template Tags And Functions Here.

register = template.Library()

inc = 0


@register.filter
def chk_ques_mark(string_value):

    chk = 0
    if string_value[len(string_value)-1:] != '?':  

        string_value = string_value.split(' ')
        question_words = ['what', 'which', 'where', 'when', 'who', 'whom', 'whose', 'how', 'do', 'does', 'did', 'is', 'are', 'was', 'were', 'has', 'have', 'had']

        for s in string_value:
            if question_words.count( s.lower() ) > 0:
                chk = 1
                break

    return chk


@register.filter
def add_ques_mark(string_value):

    chk = 0
    if string_value[len(string_value)-1:] != '?':

        string = string_value.split(' ')
        question_words = ['what', 'which', 'where', 'when', 'who', 'whom', 'whose', 'how', 'do', 'does', 'did', 'is', 'are', 'was', 'were', 'has', 'have', 'had']

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
def increment(num):
    global inc
    inc += 1
    return ''


@register.filter
def count(num): 
    global inc   
    if inc > 1:
        inc = 0
        return 1
    else:
        inc = 0
        return 0


@register.filter
def split_string(string_value):

    string_value = string_value.split(' ')
    
    return string_value


@register.filter
def highlight_search(keyword):

    search = pass_to_ttags()
    
    if keyword.lower() == search.lower():
        return 1
    else:
        return 0

    # keyword = pass_to_ttags()
    # keyword = list( keyword )

    # string_value = list(string_value)

    # if string_value.count( keyword.upper() ) > 0 or string_value.count( keyword.lower() ) > 0:
    #     return 1
    # else:
    #     return 0


# @register.filter
# def remove_last_space(word):

#     word = word[:len(word)-1]

#     return word