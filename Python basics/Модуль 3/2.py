# def sqrt(a):
#     return a ** 0.5


# print(sqrt(16))  # 4

# def sqrt(a):
#     return a ** 0.5


# variable = sqrt(16)

def invite_to_event(username):
    message = (f"Dear {username}, we have the honour to invite you to our event")
    return message 
username = "Oleh"
invitation = invite_to_event(username)
print(invitation)

#мій варіант 1
def invite_to_event(username):
    return f'Dear {username}, we have the honour to invite you to our event'
print(invite_to_event('Solo'))

#мій варіант 2
def invite_to_event(username):
    return f'Dear {username}, we have the honour to invite you to our event'
username = "Solo"
print(invite_to_event(username))