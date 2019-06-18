import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
django.setup()

#Fake JavaScript

import  random
from appTwo.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        fake_lastName = fakegen.last_name()
        fake_firstName = fakegen.first_name()
        fake_email = fakegen.email()
        User.objects.get_or_create(lastName=fake_lastName,firstName=fake_firstName, email=fake_email)[0]

if __name__ == '__main__':
    print('populating script!!!')
    populate(20)
    print('populating complete')
