# Generated by Django 4.0.8 on 2022-11-15 11:28

from django.db import migrations


class Migration(migrations.Migration):

	dependencies = [
		('dashboard', '0080_alter_pset_clubs_alter_pset_hours'),
	]

	operations = [
		migrations.SeparateDatabaseAndState(
			state_operations=[
				migrations.DeleteModel(name='ProblemSuggestion', ),
			],
			database_operations=[]
		)
	]
