from django.db import models

# Intructor models here.
class Instructor(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    dob = models.DateField(null=False)
    address = models.CharField(max_length=100)
    contactNumber = models.CharField(max_length=10)
    profilePicture = models.ImageField(null=True, blank=True, upload_to="images/", default=1)
    verificationStatus = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Instructor"
    
    def __str__(self):
        return self.firstName + ' ' + self.lastName

# Student models here.
class Student(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    dob = models.DateField(null=False)
    address = models.CharField(max_length=100)
    contactNumber = models.CharField(max_length=10)
    profilePicture = models.ImageField(null=True, blank=True, upload_to="images/", default=1)
    verificationStatus = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Student"

    def __str__(self):
        return self.firstName + ' ' + self.lastName
    


# Category models here.
class Category(models.Model):
    categoryName = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.categoryName

# Course models here.
class Course(models.Model):
    courseName = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    fk_category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="category")
    fk_intructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, verbose_name="Intructor")
    enrollmentCapacity = models.IntegerField()
    startDate = models.DateField(null=False)
    endDate = models.DateField(null=False)
    # progressStatus = 
    class Meta:
        verbose_name_plural = "Course"
    
    def __str__(self):
        return self.courseName


# Enrollments models here.
class Enrollments(models.Model):
    fk_student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Student")
    fk_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Course")
    enrollmentDate = models.DateField(null=False)
    class Meta:
        verbose_name_plural = "Enrollment"


# Syllabus models here.
class Syllabus(models.Model):
    syllabusTitle = models.CharField(max_length=100)
    fk_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Course")
    topic = models.TextField()
    chapters = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Syllabus"
    
    def __str__(self):
        return self.syllabusTitle

# Content Model here.
class Content(models.Model):
    fk_syllabus = models.ForeignKey(Syllabus, on_delete=models.CASCADE, verbose_name="Sallabus")
    contentTitle = models.CharField(max_length=150)
    description = models.TextField()
    fk_intructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, verbose_name="Instructor")
    uploadDate = models.DateField(null=False)
    totalViews = models.IntegerField()
    class Meta:
        verbose_name_plural = "Content"

    def __str__(self):
        return self.contentTitle

# Material Model here.
class Material(models.Model):
    materialTitle = models.CharField(max_length=100)
    description = models.TextField()
    fk_content = models.ForeignKey(Content, on_delete=models.CASCADE, verbose_name="content")
    uploadDate = models.DateField(null=False)
    fileMaterial = models.FileField(null=True, blank=True, upload_to="video%y", default=1)
    class Meta:
        verbose_name_plural = "Material"
    
    def __str__(self):
        return self.materialTitle

# FAQ Model here.
class Faq(models.Model):
    questions = models.TextField()
    answer = models.TextField()
    fk_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Course")
    fk_student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Student")
    class Meta:
        verbose_name_plural = "Faq"

# ClassSchedule Model here
class ClassSchedule(models.Model):
    classTitle = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    fk_nstructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, verbose_name="Instructor")
    fk_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Course")
    classDate = models.DateField()
    classTime = models.TimeField()
    duration = models.DurationField()
    class Meta:
        verbose_name_plural = "Class Schedule"

# QuizQAndA Model here.
class QuizQAndA(models.Model):
    quizQuestion = models.CharField(max_length=200)
    quizAnswer = models.CharField(max_length=200)
    optionA = models.CharField(max_length=200)
    optionB = models.CharField(max_length=200)
    optionC = models.CharField(max_length=200)
    class Meta:
        verbose_name_plural = "QuizQandA"

    def __str__(self):
        return self.quizAnswer

# Quizes Model here.
class Quizes(models.Model):
    fk_quizQAndAID = models.ForeignKey(QuizQAndA, on_delete=models.CASCADE, verbose_name="Answer")
    title = models.CharField(max_length=100)
    maxScore = models.IntegerField()
    userScore = models.IntegerField()
    fk_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Coure")
    fk_instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, verbose_name="Intructor")
    time = models.TimeField()
    startDate = models.DateField()
    endDate = models.DateField()
    class Meta:
        verbose_name_plural = "Quizes"
