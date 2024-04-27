students = [
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    },
]

def save_applicant_data(source, output):
    with open(output, 'w') as file:
        for student in source:
            file.write(f'{student ["name"]},{student ["specialty"]},{student ["math"]},{student ["lang"]},{student ["eng"]}\n')
# save_applicant_data (students,'path')
save_applicant_data (students,'/Users/solo/Desktop/IT/Repository/Tier1/Модуль 6/test.txt')



