#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2018-05-21 17:07:05

import ipdb
import sys
import datetime
from datetime import timedelta
import pytz

from django.core.management.base import OutputWrapper
from django.core.management.color import color_style

from django.test import TestCase
from testapp import models
from testapp.models import DateTimeModel, Student, Teacher
from testapp import models, head, head1, list1, list2, info
from django.utils import timezone


out = OutputWrapper(sys.stdout)
style = color_style()


head("# 准备测试Field")


class FieldTestCase(TestCase):

    def setUp(self):
        pass

    def test_onetoone_field(self):
        head1("\n## 测试OneToOneField")
        text = models.BasicModel.objects.create(text="text")
        onetoone = models.TestOneToOneField.objects.create(text=text)
        text.delete()
        # CASCADE null=False|True, 此时可以用text.testonetoonefield 但是调用 text.testonetoonefield.refresh_from_db 就会报错
        out.write(style.HTTP_INFO("text已经删除"))
        out.write(style.HTTP_INFO(models.TestOneToOneField.objects.all()))

    def test_manytomany_field(self):
        head1("\n## 测试ManyToManyField")
        list1("* 如果symmetrical=True默认")
        student = Student.objects.create(name="George")
        student2 = Student.objects.create(name="Li Lei")
        student3 = Student.objects.create(name="Han Mei")
        student2.friends.add(student)
        student2.friends.add(student3)
        student3.friends.add(student2)
        print("student2的好友有:", end=" ")
        print(student2.friends.all())
        print("认为我是好友的有(只能是一样的):", end=" ")
        # print(student2.student_set.all()) 这个会报错
        print(student2.friends.all())
        list1("* 如果symmetrical=False")
        teacher = Teacher.objects.create(name="王主任")
        teacher2 = Teacher.objects.create(name="小李主任")
        teacher3 = Teacher.objects.create(name="小红主任")
        teacher2.teachers.add(teacher)
        teacher2.teachers.add(teacher3)
        teacher3.teachers.add(teacher)
        print("给teacher3指导过的有:", end=" ")
        print(teacher3.teachers.all())
        print("teacher3指导过的人有:", end=" ")
        # import ipdb
        # ipdb.set_trace()
        print(teacher3.teacher_set.all())
        list1("* 检查是否存在")
        new_student = Student.objects.create(name="New Student")
        print("现在new_student的friends里面有没有George", student in new_student.friends.all())
        result = new_student.friends.add(student)
        print("add以后现在new_student的friends里面有没有George", student in new_student.friends.all())
        print("但是add的return: ", result)
        head1("ManyToManyField测试完毕")

    def test_datetime_field(self):
        head1("\n## 测试和时间有关的Field")
        list1("* 测试DurationField")
        datetime_obj = models.DateTimeModel.objects.create(
            time=timezone.now())
        info(isinstance(datetime_obj.duration, timedelta))
