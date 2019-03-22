#!/usr/bin/env python
# coding:utf-8
# author: sinlyon date 2019/3/21 0021
import time

from django.http import HttpResponse
from HelloWorld.Models import models
from . import view
from django.shortcuts import render


def add_user(user):
    user.save()
    return "添加用户成功！"


def get_user(user):
    user = models.User.objects.get(user_id=user.user_id)
    response = """<h2> 姓名: %s </h2>
        <h2> 年龄: %d </h2>
        <h2> 生日: %s </h2>
        <h2> 地址: %s </h2>""" % (user.user_name, user.user_age, user.user_birthday, user.user_addr)
    return response


def get_users():
    # 获取前3条数据，与limit 3
    # users = models.User.objects.all()[0:3]
    users = models.User.objects.all()
    # 根据user_id排序
    # users = models.User.objects.all().order_by("user_id")[0:3]
    # response = ""
    # for user in users:
    #     temp = """<h2> 姓名: %s</h2>
    #     <h2> 年龄: %d</h2>
    #     <h2> 生日: %s</h2>
    #     <h2> 地址: %s</h2>
    #     """ % (user.user_name, user.user_age, user.user_birthday, user.user_addr)
    #     response += temp
    return users


def mod_user(user):
    old_user = models.User.objects.get(user_id=user.user_id)
    old_user.user_name = user.user_name
    old_user.user_age = user.user_age
    old_user.save()
    response = """新用户信息：<br>
    <h2> 姓名: %s</h2>
    <h2> 年龄: %d</h2>
    <h2> 生日: %s</h2>
    <h2> 地址: %s</h2> 
    """ % (old_user.user_name, old_user.user_age, old_user.user_birthday, old_user.user_addr)
    return response


def del_user(user):
    try:
        user = models.User.objects.get(user_id=user.user_id)
    except Exception:
        response = "<h2>用户不存在</h2>"
    if not user:
        user.delete()
        response = """删除用户信息：<br>
        <h2> 姓名: %s</h2>
        <h2> 年龄: %d</h2>
        <h2> 生日: %s</h2>
        <h2> 地址: %s</h2> 
        """ % (user.user_name, user.user_age, user.user_birthday, user.user_addr)
    return response


def users(request):
    # action = {"GET": get_user, "POST": add_user, "PUT": mod_user, "DELETE": del_user}
    # user = models.User()
    # user.user_name = "sinlyon"
    # user.user_age = 18
    # user.user_birthday = time.strftime("%Y-%m-%d %H:%M:%S")
    # user.user_addr = "广东省深圳市"
    # 添加用户
    # add_user(user)

    # 获取单个用户 user_id==1
    # user = models.User()
    # user.user_id = 1
    # response = action[request.method](user)

    # 用户列表
    users = get_users()
    for user in users:
        print(user.user_id)

    # 修改id==2的用户
    # user = models.User()
    # user.user_id = 2
    # user.user_name = "xingliang"
    # user.user_age = 20
    # response = mod_user(user)

    # 删除id==9的用户
    # user = models.User()
    # user.user_id = 9
    # response = del_user(user)
    # return HttpResponse(response)
    # context = {"users": response}
    user_list = {"users": users}
    return HttpResponse
    return render(request, "users.html", user_list)
