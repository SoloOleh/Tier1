# with open('raw_data.bin', 'wb') as fh:
#     fh.write(b'Hello world!')

def save_credentials_users(path, users_info):
    with open(path, 'wb') as file:
        for username, password in users_info.items():
            # Формуємо рядок у форматі "username:password\n"
            line = f"{username}:{password}\n"
            # Конвертуємо рядок у байти
            file.write(line.encode())

# Приклад використання функції
users_info = {'andry':'uyro18890D', 'steve':'oppjM13LL9e'}
save_credentials_users('user_credentials.bin', users_info)
