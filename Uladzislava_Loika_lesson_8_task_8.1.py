import re

regex = re.compile(r'(?P<username>[A-Za-z0-9]+[.-_]+[A-Za-z0-9]+@(?P<domain>[A-Za-z0-9]+(\.[A-Za-z]{2,})))+')
# regex = re.compile(r'             ([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@           [A-Za-z0-9]+(\.[A-Z|a-z]{2,})+')
# RE_GET_PARSER = re.compile(r'(?<=[&?])(?P<key>[^&]+)=(?P<val>[^&]+)(?=&*)')

# def isValid(email):
#     if re.fullmatch(regex, email):
#       print("Valid email")
#     else:
#       print("Invalid email")
#
# isValid("name_surname@gmail.com")

def email_parse (email):
    RE_MAIL = re.compile(r'(?P<username>[A-Za-z0-9]+[.-_]*[A-Za-z0-9]+)@(?P<domain>[A-Za-z0-9]+(\.[A-Za-z]{2,}))+')

    try:
        result = RE_MAIL.match(email)
        dict_res = result.groupdict()
    except Exception:
        raise ValueError(f'Wrong e-mail format for: {email}')
    else:
        return dict_res


if __name__ == '__main__':
    print(email_parse('someo--ne@geekbrains.ru'))