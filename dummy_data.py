import os , django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()



from faker import Faker
import random
from fruit.models import Fruit





def seed_fruit(n):
    fake = Faker()
    images = ['fruite1.jpg','fruite2.jpg','fruite3.jpg','fruite4.jpg','fruite5.jpg','fruite6.jpg','vegatables1.jpg','vegatables2.jpg',]
    

    for x in range(n):
        Fruit.objects.create(
            name = fake.name() , 
            price = round(random.uniform(20.99,99.99),2) , 
            subtitle=fake.text(max_nb_chars=30) , 
            image = f'fruit/{images[random.randint(0,7)]}',
            
        )
    print(f'{n} Product Was Created Successfuly ...')




seed_fruit(300)