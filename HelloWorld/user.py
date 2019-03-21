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
    return models.User.objects.filter(user_name="sinlyon")


def get_users(user):
    return user.objects.all()


def mod_user(user):
    pass


def del_user(user):
    pass


def user(request):
    action = {"GET": get_user, "POST": add_user, "PUT": mod_user, "DELETE": del_user}
    # user = models.User()
    # user.user_name = "sinlyon"
    # user.user_age = 18
    # user.user_birthday = time.strftime("%Y-%m-%d %H:%M:%S")
    # user.user_addr = "广东省深圳市"
    # add_user(user)
    result = action[request.method](None)
    # return HttpResponse(result)
    return render(request, "users.html", result)