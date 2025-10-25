# Generated manually

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('зачет', 'Зачет'), ('незачет', 'Незачет')], max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(blank=True, max_length=50, null=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_site.group')),
            ],
        ),
        migrations.CreateModel(
            name='StudentDisciplineMark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discipline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_site.discipline')),
                ('mark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_site.mark')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_site.student')),
            ],
        ),
        migrations.AddConstraint(
            model_name='studentdisciplinemark',
            constraint=models.UniqueConstraint(fields=('student', 'discipline'), name='unique_student_discipline'),
        ),
    ]

