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

class MessageRecipient(models.Model):
    placeholder = models.CharField(max_length=50) #this is a placeholder, all items here are foreign keys / this is a joiner table

class Relationship(models.Model):
    relationship_type = models.CharField(max_length=100)

class ContactRelationship(models.Model):
    placeholder2 = models.CharField(max_length=50) #this is a placeholder, all items here are foreign keys / this is a joiner table