import shutil

from faker import Faker

fake = Faker('en_US')

contents = ""

existing = ""

###########################
# explains what range is doing under the hood
###########################

# range_gen = range(100)

# print(type(range_gen))

# iterator = iter(range_gen)

# print(type(iterator))

# while True:

#     try:
#         i = next(iterator)
#     except StopIteration:
#         break

###########################

for i in range(100):

    email = fake.email()
    phone_number = fake.phone_number()

    contents += fake.paragraph()
    contents += " " + email + " "
    contents += fake.paragraph()
    contents += fake.ssn()
    contents += fake.sentence()
    contents += phone_number
    contents += fake.paragraph()

    if i % 7 == 0: # every now and then throw in a duplicate email
        contents += " " + email + " "
        contents + fake.sentence()

    if i % 9 == 0: # every now and then throw in a duplicate phone number
        contents += phone_number
        contents += fake.paragraph()


    if i % 5 == 0: # keep track of some "existing contacts" for the stretch goal
        existing += email + "\n"
        existing += phone_number + "\n"


    contents += "\n"

with open("potential-contacts.txt", "w+") as f:
    f.write(contents)

shutil.copy('potential-contacts.txt', '../../lab/assets/potential-contacts.txt')

# for stretch goal
with open("existing-contacts.txt", "w+") as f:
    f.write(existing)

shutil.copy('existing-contacts.txt', '../../lab/assets/existing-contacts.txt')




