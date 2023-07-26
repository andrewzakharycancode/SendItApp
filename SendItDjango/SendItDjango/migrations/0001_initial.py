# Generated by Django 4.2.2 on 2023-07-26 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Address",
            fields=[
                ("address_id", models.AutoField(primary_key=True, serialize=False)),
                ("street_address", models.CharField(max_length=60)),
                ("apartment_number", models.CharField(max_length=20, null=True)),
                ("city", models.CharField(max_length=30)),
                ("state", models.CharField(max_length=30)),
                ("zip_code", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="Contact",
            fields=[
                ("contact_id", models.AutoField(primary_key=True, serialize=False)),
                ("first_name", models.CharField(max_length=30)),
                ("last_name", models.CharField(max_length=30, null=True)),
                ("birthday", models.DateField(null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("contact_photo", models.ImageField(null=True, upload_to="")),
                ("active", models.BooleanField(default=True)),
                (
                    "address_primary",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="contact_address_primary",
                        to="SendItDjango.address",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Email",
            fields=[
                ("email_id", models.AutoField(primary_key=True, serialize=False)),
                ("email_address", models.CharField(max_length=120, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="PhoneNumber",
            fields=[
                (
                    "phone_number_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("country_code", models.CharField(max_length=4)),
                ("phone_number", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Relationship",
            fields=[
                (
                    "relationship_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("relationship_type", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                ("user_id", models.AutoField(primary_key=True, serialize=False)),
                ("first_name", models.CharField(max_length=30)),
                ("last_name", models.CharField(max_length=30)),
                ("profile_picture", models.ImageField(null=True, upload_to="")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "address_primary",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="user_address_primary",
                        to="SendItDjango.address",
                    ),
                ),
                (
                    "email_primary",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="SendItDjango.email",
                    ),
                ),
                (
                    "phone_number",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="SendItDjango.phonenumber",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Message",
            fields=[
                ("message_id", models.AutoField(primary_key=True, serialize=False)),
                ("message_text", models.CharField(max_length=1000)),
                ("send_date", models.DateTimeField()),
                ("recurring", models.BooleanField(default=False)),
                ("attachment", models.FileField(null=True, upload_to="")),
                ("frequency", models.CharField(max_length=50, null=True)),
                ("recipient", models.ManyToManyField(to="SendItDjango.contact")),
                (
                    "sender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="SendItDjango.user",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="contact",
            name="email_primary",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="SendItDjango.email",
            ),
        ),
        migrations.AddField(
            model_name="contact",
            name="phone_number",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="SendItDjango.phonenumber",
            ),
        ),
        migrations.AddField(
            model_name="contact",
            name="relationships",
            field=models.ManyToManyField(to="SendItDjango.relationship"),
        ),
        migrations.AddField(
            model_name="contact",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="SendItDjango.user"
            ),
        ),
    ]