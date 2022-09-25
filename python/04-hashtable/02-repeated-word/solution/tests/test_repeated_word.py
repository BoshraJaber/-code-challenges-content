from unittest import async_case
from repeated_word.repeated_word import first_repeated_word


def test_first_repeated_word():
    string = "ASAC is a department at LTUC. ASAC teaches programming in LTUC."
    actual = first_repeated_word(string)
    excepted = "asac"
    assert actual == excepted
    
    
def test_first_repeated_word_no_repetition():
    string = "I am learning programming at ASAC"
    actual = first_repeated_word(string)
    excepted =  "No repetition"
    assert actual == excepted   
    
    
def test_first_repeated_word_empty():
    string = " "
    actual = first_repeated_word(string)
    excepted =  "No repetition"
    assert actual == excepted   
    
    
