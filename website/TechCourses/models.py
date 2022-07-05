from django.db import models

class Allcourses(models.Model):
    coursename = models.CharField(max_length= 200)
    instructorname = models.CharField(max_length= 200)
    def __str__(self):
        return '{} {}'.format(self.coursename, self.instructorname)

class details(models.Model):
    course = models.ForeignKey(Allcourses, on_delete=models.CASCADE)
    sp = models.CharField(max_length=500)
    il = models.CharField(max_length=500)
    def __str__(self):
       # return '{} {}'.format(self.sp, self.il)
         return str(self.pk)
