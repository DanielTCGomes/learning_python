
import re


# def verification(a):
    
#     rule2 = re.compile(r"[a-zA-Z0-9]")
#     if re.match(rule2, a):
#         return True 
#     else:
#         return False
# print(verification("zzz"))

def check_character(string):
    rule = re.compile(r'[^a-zA-Z0-9]')
    string = rule.search(string)
    return not bool(string)

print(check_character("ABCDEFabcdef123450")) 
print(check_character("*&%@#!}{"))