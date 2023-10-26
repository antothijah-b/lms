from rest_framework import serializers
from . import models

# Serializer for Instructor
class IntructorSerailizer(serializers.ModelSerializer):
    class Meta:
        model = models.Instructor
        fields = ['id', 'firstName', 'lastName', 'email', 'password', 'dob', 'address', 'contactNumber', 'profilePicture', 'verificationStatus']

# Serializer for Student
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ['id', 'firstName', 'lastName', 'email', 'password', 'dob', 'address', 'contactNumber', 'profilePicture' ,'verificationStatus']

# Serializer for Category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['id', 'categoryName', 'description']

# Serializer for Course
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ['id', 'courseName', 'description', 'fk_category', 'fk_intructor', 'enrollmentCapacity', 'startDate', 'endDate']

# Serializer for Enrollments
class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Enrollments
        fields = ['id', 'fk_student', 'fk_course', 'enrollmentDate']

# Serializer for Syllabus
class SyllabusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Syllabus
        fields = ['id', 'syllabusTitle', 'fk_course', 'topic', 'chapters']

# Serializer for Content
class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Content
        fields = ['id', 'fk_syllabus', 'contentTitle', 'description', 'fk_intructor', 'uploadDate', 'totalViews']

# Serializer for Material
class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Material
        fields = ['id', 'materialTitle', 'description', 'fk_content', 'fileMaterial', 'uploadDate']

# Serializer for Faq
class FaqSerialzer(serializers.ModelSerializer):
    class Meta:
        model = models.Faq
        fields = ['id', 'questions', 'answer', 'fk_course', 'fk_student']

# Serializer for ClassSchedule
class ClassScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ClassSchedule
        fields = ['id', 'classTitle', 'description', 'fk_nstructor', 'fk_course', 'classDate', 'classTime', 'duration']

# Serializer for QuizQAndA
class QuizQAndASerializer(serializers.ModelSerializer):
    class Meta:
        model = models.QuizQAndA
        fields = ['id', 'quizQuestion', 'quizAnswer', 'optionA', 'optionB', 'optionC']

# Serailizer for Quizes
class QuizesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Quizes
        fields = ['id', 'fk_quizQAndAID', 'title', 'maxScore', 'userScore', 'fk_course', 'fk_instructor', 'time', 'startDate', 'endDate']


