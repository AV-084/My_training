def sent_email(massage ,recipient, *, sender = 'university.help@gmail.com'):
    if '@' not in recipient:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif '@' not in sender:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif not any(i in recipient for i in ('.com', '.ru', '.net')):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif not any(i in sender for i in ('.com', '.ru', '.net')):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif recipient == sender:
        print(f'Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')

sent_email(massage='Это сообщение для проверки связи', recipient='vasyok1337@gmail.com', sender='university.help@gmail.com')
sent_email(massage='Вы видите это сообщение как лучший студент курса!', recipient='urban.fan@mail.ru', sender='urban.info@gmail.com')
sent_email(massage='Пожалуйста, исправьте задание', recipient='urban.student@mail.ru', sender='urban.teacher@mail.uk')
sent_email(massage='Напоминаю самому себе о вебинаре', recipient='urban.teacher@mail.ru', sender='urban.teacher@mail.ru')