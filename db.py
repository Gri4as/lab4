import security

database_data = ''
log_pass = {}


def filling_data():
    with open('bin/base.dat', 'r', encoding='utf-8') as database:
        database_data = database.read().split('\n')
    if database_data == ['']:
        pass
    else:
        for x in database_data:
            log_pass[x.split(':')[0]] = x.split(':')[1]


def add_account(login, password):
    log_pass[login] = security.road_to_hash(password)
    with open('bin/base.dat', 'a', encoding='utf-8') as new_account:
        if len(log_pass) > 1:
            new_account.write('\n')
        new_account.write(login + ':' + security.road_to_hash(password))


def authorization(login, password):
    if log_pass[login] == security.road_to_hash(password):
        pass
    else:
        raise Exception('Ошибка входа')


def delete_account(login, password):
    if log_pass[login] == security.road_to_hash(password):
        del log_pass[login]
        with open('bin/base.dat', 'w', encoding='utf-8') as write_dat:
            if len(log_pass) == 0:
                return
            elif len(log_pass) == 1:
                write_dat.write(list(log_pass.keys())[0]+ ':' + log_pass[list(log_pass.keys())[0]])
            else:
                for x in log_pass:
                    write_dat.write(x + ':' + log_pass[x])
                    if x != list(log_pass.keys())[-1]:
                        write_dat.write('\n')
    else:
        raise Exception("Похоже здесь ошибка")