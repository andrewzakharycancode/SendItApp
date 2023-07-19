from django.db import models

#all fields not added
class Email(models.Model):
    email_id = models.AutoField(primary_key=True)
    email_address = models.CharField(max_length=120, unique=True) 

#all fields not added    
class PhoneNumber(models.Model):
    phone_number_id = models.AutoField(primary_key=True)
    country_code = models.CharField(max_length=4)
    phone_number = models.CharField(max_length=20)

#all fields not added
class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    street_address = models.CharField(max_length=60)
    apartment_number = models.CharField(max_length=20, null=True)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=10)

#all fields not added
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    #Figure out the syntax for how to identify the foreign key below
    email_primary = models.ForeignKey(Email, on_delete=models.CASCADE)
    profile_picture = models.ImageField(null=True)
    phone_number = models.ForeignKey(PhoneNumber, on_delete=models.CASCADE)
    address_primary = models.ForeignKey(Address, related_name='user_address_primary', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Relationship(models.Model):
    relationship_id = models.AutoField(primary_key=True)
    relationship_type = models.CharField(max_length=100)

#all fields not added
class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    phone_number = models.ForeignKey(PhoneNumber, on_delete=models.CASCADE)
    email_primary = models.ForeignKey(Email, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, null=True)
    birthday = models.DateField(null=True)
    address_primary = models.ForeignKey(Address, related_name='contact_address_primary', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    contact_photo = models.ImageField(null=True)
    active = models.BooleanField(default=True)
    relationships = models.ManyToManyField(Relationship)

#all fields not added
class Message(models.Model):
    message_id = models.AutoField(primary_key=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    recipient = models.ManyToManyField(Contact, on_delete=models.CASCADE)
    message_text = models.CharField(max_length=1000)
    send_date = models.DateTimeField()
    recurring = models.BooleanField(default=False)
    attachment = models.FileField(null=True)
    frequency = models.CharField(max_length=50, null=True)

# Below is a sample model where the model has a characteristic similar to an enum, where there are options for that column, but only a finite number of options
# class Person(models.Model):
#     SHIRT_SIZES = [
#         ("S", "Small"),
#         ("M", "Medium"),
#         ("L", "Large"),
#     ]
#     name = models.CharField(max_length=60)
#     shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)

#many to many and one to one samples
# poll = models.ForeignKey(
#     Poll,
#     on_delete=models.CASCADE,
#     verbose_name="the related poll",
# )
# sites = models.ManyToManyField(Site, verbose_name="list of sites")
# place = models.OneToOneField(
#     Place,
#     on_delete=models.CASCADE,
#     verbose_name="related place",
# )

#A Note ON MANY TO MANY (there is more documentation on this if needed):
# It doesn’t matter which model has the ManyToManyField, but you should only put it in one of the models – not both.
# Generally, ManyToManyField instances should go in the object that’s going to be edited on a form. In the above example, toppings is in Pizza (rather than Topping having a pizzas ManyToManyField ) because it’s more natural to think about a pizza having toppings than a topping being on multiple pizzas. The way it’s set up above, the Pizza form would let users select the toppings.
