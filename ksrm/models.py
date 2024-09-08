from django.db import models

# Create your models here.
# class Student(models.Model):
# 	branchopts=[
# 				('CSE','CSE'),
# 				# ('EEE','EEE'),
# 				# ('ECE','ECE'),
# 				# ('MECH','MECH'),
# 				# ('CIVIL','CIVIL'),
# 				]


# 	name=models.CharField(max_length=20)
# 	rollno=models.CharField(max_length=20)
# 	subject=models.CharField(max_length=20)
# 	no_of_copies=models.CharField(max_length=10)
# 	branch=models.CharField(max_length=10,choices=branchopts)
# 	def __str__(self):
# 		return self.name




class Student1(models.Model):
	branchopts=[
				('CSE','CSE'),
				('EEE','EEE'),
				 ('ECE','ECE'),
				 ('MECH','MECH'),
				 ('CIVIL','CIVIL'),
				]


	name=models.CharField(max_length=20)
	rollno=models.CharField(max_length=20)
	subject=models.CharField(max_length=20)
	no_of_copies=models.CharField(max_length=10)
	branch=models.CharField(max_length=10,choices=branchopts)
	
	def __str__(self):
		return self.name
	

class Professor(models.Model):
	department_opt = [
		('CSE','CSE'),
		('EEE','EEE'),
		('ECE','ECE'),
		('MECH','MECH'),
		('CIVIL','CIVIL'),
	]
	name = models.CharField(max_length=20)
	employee_id = models.CharField(max_length=20)
	designation = models.CharField(max_length=20)
	subject=models.CharField(max_length=20)
	no_of_copies=models.CharField(max_length=10)
	department = models.CharField(max_length=20,choices=department_opt)


	def __str__(self) -> str:
		return self.name



