# Generated by Django 3.2.5 on 2022-10-27 10:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('automobile', '0003_alter_usedcars_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='discount',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='positioncategory',
            name='max_speed',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='positioncategory',
            name='seats_count',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='positioncategory',
            name='year',
            field=models.PositiveIntegerField(choices=[(2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024)], default=2022, verbose_name='year'),
        ),
        migrations.AlterField(
            model_name='usedcars',
            name='year',
            field=models.PositiveIntegerField(choices=[(2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024)], default=2022, verbose_name='year'),
        ),
        migrations.CreateModel(
            name='CarLikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likepost', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='likepost', to='automobile.car')),
                ('likeusers', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]