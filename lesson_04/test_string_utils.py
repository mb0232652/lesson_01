
from string_utils import StringUtils 
import pytest

def test_capitaleze_positive_смешанный_регистр():

    string_utils = StringUtils()
    assert string_utils.capitalize("skyPro") == "SkyPro"

def test_capitaleze_positive_все_заглавными():

    string_utils = StringUtils()
    assert string_utils.capitalize("SKYPRO") == "SKYPRO"   

def test_capitaleze_positive_обычный_текст():

    string_utils = StringUtils()
    assert string_utils.capitalize("hello") == "Hello"  

def test_capitaleze_positive_цифры_текст():

    string_utils = StringUtils()
    assert string_utils.capitalize("123abc") == "123Abc" 


def test_capitaleze_positive_кириллица():

    string_utils = StringUtils()
    assert string_utils.capitalize("привет") == "Привет" 


def test_trim_positive_Принимает_на_вход_текст_удаляет_пробелы_в_начале_если_есть():

    string_utils = StringUtils()
    assert string_utils.trim(" Привет") == "Привет" 

def test_trim_positive_Принимает_на_вход_текст_удаляет_пробелы_в_начале_если_есть_в_колличестве_10():

    string_utils = StringUtils()
    assert string_utils.trim("          Привет") == "Привет"  

def test_trim_negative_строка_пробелом_пустая():

    string_utils = StringUtils()
    assert string_utils.trim(" ") == ""   

         
def test_contains_positive_есть_искомый_символ_S():

    string_utils = StringUtils()
    assert string_utils.contains("Sport", "S") == True  


def test_contains_positive_нет_искомого_символ_S():

    string_utils = StringUtils()
    assert string_utils.contains("Port", "S") == False  

def test_contains_positive_есть_искомый_символ_s_строчной():

    string_utils = StringUtils()
    assert string_utils.contains("skyPro", "s") == True           

def test_contains_negative_пустая_строка():

    string_utils = StringUtils()
    assert string_utils.contains("", "S") == False 

def test_contains_negative_NONE():

    string_utils = StringUtils()
    with pytest.raises(TypeError):
         string_utils.contains(None, "S") == False 


def test_delete_symbo_positive_удаляет_заявленный_символ_k():

    string_utils = StringUtils()
    assert string_utils.delete_symbol("sok", "k") == "so"  

def test_delete_symbo_positive_удаляет_заявленный_символ_Pro():

    string_utils = StringUtils()
    assert string_utils.delete_symbol("Pro", "Pro") == ""          

