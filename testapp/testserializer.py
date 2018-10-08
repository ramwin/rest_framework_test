#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-09-21 15:16:54


import json
import time
import sys

from django.core.management.base import OutputWrapper
from django.core.management.color import color_style
from django.test import TestCase
from django.utils import timezone
from .models import *
from . import serializers


out = OutputWrapper(sys.stdout)
style = color_style()


def head(text):
    out.write(style.SQL_TABLE(text))

def head1(text):
    out.write(style.MIGRATE_HEADING(text))

def list1(text):
    out.write(style.SQL_FIELD(text))

def list2(text):
    out.write(style.SQL_COLTYPE(text))

def info(text):
    out.write(style.HTTP_INFO(text))

class MySerializerTestCase(TestCase):

    def test_datetime(self):
        info("准备测试datetime field")
        data = {'time': timezone.now()}
        serializers.DateTimeModelSerializer(data=data).is_valid(raise_exception=True)
        info("可以直接使用datetime对象")

    def test_hidden(self):
        out.write(style.HTTP_INFO("准备测试hiddenfield"))
        s = serializers.TestHiddenField(data={"time1": "send"})
        s.is_valid(raise_exception=True)
        out.write(style.SUCCESS(s.validated_data))
        out.write(style.HTTP_INFO("测试完毕"))

    def test_many(self):
        print("准备测试多对多")
        a = serializers.ManySerializer(data={'texts': ['1','2','3']})
        a.is_valid(raise_exception=True)
        # a.save(texts=[])
        a.save()
        print("保存成功")
        BasicModel.objects.create(text='text')
        a.instance.texts.add(*BasicModel.objects.all())
        # print(serializers.ManyDetailSerializer(a.instance).data)

    def test_null(self):
        # print("不测试null")
        # return
        data_list = [
            {},
            {"can": ""},
            {"can": "can"}, # 有null为null，有blank为""
            {"can": "can", "can_null": None},
            {"can": "can", "can_null": ""},
            {"can": "can", "can_blank": None},
            {"can": "can", "can_default": ""},
        ]
        for data in data_list:
            serializer = serializers.TestNullSerializer(data=data)
            print("准备处理: %s" % data)
            if serializer.is_valid(raise_exception=False):
                serializer.save()
                out.write(style.SUCCESS(serializer.data))
            else:
                out.write(style.ERROR(serializer.errors))

    def test_serializer(self):
        return 
        print("准备测试")
        a = serializers.MySerializer(data={'field': 2})
        a.is_valid(raise_exception=True)
        a.save()

    def test_auto_now(self):
        out.write(style.HTTP_INFO("准备测试auto_now_add"))
        s = serializers.TestHiddenField(data={"text": "text", "time": "time"})
        s.is_valid(raise_exception=True)
        out.write(style.SUCCESS(s.validated_data))
        out.write(style.HTTP_INFO("测试完毕"))

    def test_many_filter(self):
        out.write(style.HTTP_INFO("准备测试嵌套的序列化类进行过滤"))
        text1 = BasicModel.objects.create(text='text1')
        text2 = BasicModel.objects.create(text='text2')
        mm = ManyModel.objects.create()
        mm.texts.add(text1, text2)
        out.write(style.MIGRATE_HEADING(json.dumps(serializers.ManyDetail2Serializer(mm).data, indent=4)))

    def test_many_true(self):
        print("准备测试嵌套的序列化类")
        a = serializers.ForeignKeySerializer(data={"text": [
            {"text":"text1"}, {"text": "text2"}
        ]})
        a.is_valid(raise_exception=True)
        a.save()
        print(a.data)
        print("嵌套的测试完毕")

    def test_method(self):
        return
        out.write(style.HTTP_INFO("准备测试method里面的数据"))
        data = {
            "text": 'text'
        }
        s = serializers.TestMethodSerializer(data=data)
        s.is_valid()
        s.save()
        out.write(style.HTTP_INFO(s.data))
        out.write(style.ERROR(s.errors))

    def test_validated_data(self):
        return
        out.write(style.HTTP_INFO("准备测试validated_data里面的数据"))
        text = BasicModel.objects.create(text='123')
        data = {
            "text": text.id
        }
        s = serializers.ForeignKey2Serializer(data=data)
        s.is_valid()
        out.write(style.HTTP_INFO(s.validated_data))
        out.write(style.ERROR(s.errors))

    def test_regex(self):
        return
        print("测试正则表达式的serializer")
        data_list = [
            {},
            {"avatar": ""},
            {"avatar": None},
            {"avatar": "tmp-group-123"},
        ]
        for data in data_list:
            serializer = serializers.TestRegexSerializer(data=data)
            print("准备处理: %s" % data)
            if serializer.is_valid(raise_exception=False):
                out.write(style.SUCCESS(serializer.data))
            else:
                out.write(style.ERROR(serializer.errors))

    def test_validation(self):
        out.write(style.HTTP_INFO("准备测试自己的validation"))
        data_list = [
            {"status": "0"},
            {"status": "1"},
            {"status": "2"},
        ]
        for data in data_list:
            serializer = serializers.TestValidateSerializer(data=data)
            print(serializer.is_valid())
        out.write(style.SUCCESS("测试自己的validation完毕"))

    def test_to_representation(self):
        out.write(style.HTTP_INFO("准备测试to_representation函数"))
        data = {"text": "text"}
        out.write(style.HTTP_INFO("准备测试to_representation函数"))
        out.write(style.HTTP_INFO("准备测试to_representation函数1"))
        serializer = serializers.TestToRepresentationSerializer(data=data)
        serializer.is_valid()
        print(serializer.data)
        out.write(style.HTTP_INFO("准备测试to_representation函数2"))
        serializer = serializers.TestToRepresentationSerializer(data=data)
        serializer.is_valid()
        serializer.save()
        print(serializer.data)
        out.write(style.HTTP_INFO("准备测试to_representation函数3"))
        serializers.TestToRepresentationSerializer(serializer.instance).data
        out.write(style.MIGRATE_HEADING("测试to_representation结束"))

    def test_property(self):
        out.write(style.HTTP_INFO("准备测试property的序列化"))
        out.write(style.HTTP_INFO("测试用pro"))
        data = {}
        serializer1 = serializers.TestPropertySerializer(data=data)
        serializer1.is_valid()
        serializer1.save()

    def test_source(self):
        head("准备测试source这个参数")
        list1("* 测试如果外键为None, 字段显示什么")
        basicmodel = BasicModel.objects.create(text='text')
        fkm = ForeignKeyModel2.objects.create()
        info(serializers.TestSourceSerializer(fkm).data)
        info("可以看到显示的是None")
        list1("* 测试如果save, 会发生什么, 他的数据竟然是 {'text': 'text'}, 不是简单的text")
        list2("    1. 如果instance的外键为None")
        testsource_ser = serializers.TestSourceSerializer(
            instance=fkm, data={"text": "text"})
        testsource_ser.is_valid(raise_exception=True)
        testsource_ser.save()
        list2("    2. 如果instance的外键不是None, 仍然是 {'text': 'text'}")
        fkm.text = basicmodel
        fkm.save()
        testsource_ser = serializers.TestSourceSerializer(
            instance=fkm, data={"text": "text"})
        testsource_ser.is_valid(raise_exception=True)
        testsource_ser.save()

    def test_extra(self):
        info("准备测试如果Meta.fields里面少了字段怎么办")
        info("会报错")
        return
        from rest_framework import serializers

        class ExtraSerializer(serializers.ModelSerializer):
            text = serializers.CharField()  # 不行，如果定义了，Meta里面必须有
            class Meta:
                model = BasicModel
                fields = ["id"]

        basic_model = BasicModel.objects.first()
        info(ExtraSerializer(basic_model).data)
