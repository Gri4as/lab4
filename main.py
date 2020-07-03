import db, security, notes

current_user = ""
super_key = 

while current_user == "":
    db.filling_data()
    menu = input('1)Регистрация\n2)Авторизация\n3)Уничтожить аккаунт\n')
    if menu == '1':
        print(db.log_pass)
        login = input('Логин: ')
        if login in db.log_pass.keys():
            print('Ошибка, логин уже в базе!')
        else:
            db.add_account(login,input('Пароль: '))
            current_user = login
    elif menu == '2':
        login, password = input('Login: '), input('Password: ')
        try:
            db.authorization(login, password)
            current_user = login
            print('Оформлен вход')
        except:
            print('Ошибка входа!')
    elif menu == '3':
        print(db.log_pass)
        login, password = input('Login: '), input('Password: ')
        try:
            db.delete_account(login, password)
            print('Танк уничтожен')
        except Exception as e:
            print('Ошибка, танк не обнаружен', e)
        print(db.log_pass)
