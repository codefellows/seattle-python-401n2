from faker import Faker

fake = Faker()
# print(dir(fake))

# fake_words = fake.words()
# print(fake_words)

# fake_sents = fake.sentences()
# print(fake_sents)

fake_paragraph = fake.paragraph()
# print(fake_paragraph)

fake_phone_number = fake.phone_number()
print(fake_phone_number)

fake_email = fake.email()
print(fake_email)

content = ''

for _ in range(100):
    content += fake.paragraph() + ' '
    content += fake.email() + ' '
    content += fake.word()
    content += fake.paragraph()
    content += fake.phone_number()

# print(content)
with open('content.txt', 'w+') as f:
    f.write(content)

import shutil

shutil.copy('content.txt', '../assets')
