# write your code here
person = {
        'name': "Munir",
        'age': 18,
        'hobbies': ["Reading", "Gaming", "Coding"]
}

print(person['name'])
print(person['age'])

person['age'] = 20
person['country'] = "Syria"
print(person)
print(len(person))

person['hobbies'].append("Football")

def check_hobbies(person):
    if len(person['hobbies']) > 3:
        print("WOW YOU ARE AMAZING!")

check_hobbies(person)        