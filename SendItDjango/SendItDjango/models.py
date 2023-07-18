from django.db import models

#all fields not added
class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    #Figure out the syntax for how to identify the foreign key below
    email_primary_id = models.ForeignKey(Email, on_delete=models.CASCADE)

#all fields not added
class Email(models.Model):
    email_address = models.CharField(max_length=120)

#all fields not added    
class PhoneNumber(models.Model):
    country_code = models.CharField(max_length=4)

#all fields not added    
class Contact(models.Model):
    first_name = models.CharField(max_length=30)

#all fields not added
class Address(models.Model):
    street_address = models.CharField(max_length=60)
    
#all fields not added
class Message(models.Model):
    message_text = models.CharField(max_length=500)

#99% sure we actually don't need the joiner tables. Django has built in many to many functionality, see notes at bottom of fil
class MessageRecipient(models.Model):
    placeholder = models.CharField(max_length=50) #this is a placeholder, all items here are foreign keys / this is a joiner table

class Relationship(models.Model):
    relationship_type = models.CharField(max_length=100)

#99% sure we actually don't need the joiner tables. Django has built in many to many functionality, see notes at bottom of fil
class ContactRelationship(models.Model):
    placeholder2 = models.CharField(max_length=50) #this is a placeholder, all items here are foreign keys / this is a joiner table
    
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
