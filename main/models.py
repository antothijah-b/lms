from django.db import models

# Intructor models here.
class Instructor(models.Model):
    instructorID = models.BigAutoField(primary_key=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    dob = models.DateField(null=False)
    address = models.CharField(max_length=100)
    contactNumber = models.CharField(max_length=10)
    # profilePicture = models.ImageField(null=True, blank=True, upload_to="images/")
    verificationStatus = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Instructor"

# Student models here.
class Student(models.Model):
    studentID = models.BigAutoField(primary_key=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    dob = models.DateField(null=False)
    address = models.CharField(max_length=100)
    contactNumber = models.CharField(max_length=10)
    # profilePicture = models.ImageField(null=True, blank=True, upload_to="images/")
    verificationStatus = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Student"

# Enrollments models here.
class Enrollments(models.Model):
    enrollmentID = models.BigAutoField(primary_key=True)
    studentID = models.ForeignKey(Student, on_delete=models.CASCADE)
    # courseID = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollmentDate = models.DateField(null=False)
    class Meta:
        verbose_name_plural = "Enrollment"

# Category models here.
class Category(models.Model):
    categoryID = models.BigAutoField(primary_key=True)
    # courseID = models.ForeignKey(Course, )
    categoryName = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    class Meta:
        verbose_name_plural = "Categories"

# Course models here.
class Course(models.Model):
    courseID = models.BigAutoField(primary_key=True)
    courseName = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    categoryID = models.ForeignKey(Category, on_delete=models.CASCADE)
    intructorID = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    enrollmentCapacity = models.IntegerField()
    startDate = models.DateField(null=False)
    endDate = models.DateField(null=False)
    # progressStatus = 
    class Meta:
        verbose_name_plural = "Course"

# Syllabus models here.
class Syllabus(models.Model):
    syllabusID = models.BigAutoField(primary_key=True)
    syllabusTitle = models.CharField(max_length=100)
    courseID = models.ForeignKey(Course, on_delete=models.CASCADE)
    topic = models.TextField()
    chapters = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Syllabus"

# Content Model here.
class Content(models.Model):
    contentID = models.BigAutoField(primary_key=True)
    syllabusID = models.ForeignKey(Syllabus, on_delete=models.CASCADE)
    contentTitle = models.CharField(max_length=150)
    description = models.TextField()
    intructorID = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    uploadDate = models.DateField(null=False)
    totalViews = models.IntegerField()
    class Meta:
        verbose_name_plural = "Content"

# Material Model here.
class Material(models.Model):
    materialID = models.BigAutoField(primary_key=True)
    materialTitle = models.CharField(max_length=100)
    description = models.TextField()
    contentID = models.ForeignKey(Content, on_delete=models.CASCADE)
    uploadDate = models.DateField(null=False)
    # fileLocation = models.CharField(max_length=200)
    class Meta:
        verbose_name_plural = "Material"

# FAQ Model here.
class Faq(models.Model):
    faqID = models.BigAutoField(primary_key=True)
    questions = models.TextField()
    answer = models.TextField()
    courseID = models.ForeignKey(Course, on_delete=models.CASCADE)
    studentID = models.ForeignKey(Student, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Faq"

# ClassSchedule Model here
class ClassSchedule(models.Model):
    classID = models.BigAutoField(primary_key=True)
    classTitle = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    instructorID = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    courseID = models.ForeignKey(Course, on_delete=models.CASCADE)
    classDate = models.DateField()
    classTime = models.TimeField()
    duration = models.DurationField()
    class Meta:
        verbose_name_plural = "Class Schedule"

# QuizQAndA Model here.
class QuizQAndA(models.Model):
    quizQAndAID = models.BigAutoField(primary_key=True)
    quizQuestion = models.CharField(max_length=200)
    quizAnswer = models.CharField(max_length=200)
    optionA = models.CharField(max_length=200)
    optionB = models.CharField(max_length=200)
    optionC = models.CharField(max_length=200)
    class Meta:
        verbose_name_plural = "QuizQandA"

# Quizes Model here.
class Quizes(models.Model):
    quizID = models.BigAutoField(primary_key=True)
    quizQAndAID = models.ForeignKey(QuizQAndA, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    maxScore = models.IntegerField()
    userScore = models.IntegerField()
    courseID = models.ForeignKey(Course, on_delete=models.CASCADE)
    instructorID = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    time = models.TimeField()
    startDate = models.DateField()
    endDate = models.DateField()
    class Meta:
        verbose_name_plural = "Quizes"
