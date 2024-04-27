def get_credentials_users(path):
    with open(path, 'rb') as file:
        content = file.read().decode('utf-8')
    return content.splitlines()
