import re


def email_parse(email_address):
    re_name = re.compile(r'\w+@\w+(\.ru|\.com)')
    if re_name.match(email_address):
        return {'username': re.findall(r'^\w+@', email_address)[0][:-1],
                'domain': re.findall(r'@\w+\.\w+', email_address)[0][1:]}

    elif re_name.match(email_address) == None:
        raise ValueError('Недопустимый формат email-адреса')


print(email_parse('some_1one@geekbrains.com'))
