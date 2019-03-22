#!/usr/bin/env python
# coding:utf-8
# author: sinlyon date 2019/3/22 0022
from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from os import linesep

from django.views.decorators.csrf import csrf_exempt


def get_form(request):
    return render_to_response("search_get.html")


def post_form(request):
    return render_to_response("search_post.html")


def search_get(request):
    request.encoding = "utf-8"
    message = ""
    if request.GET["user_id"]:
        message = "用户ID：" + request.GET["user_id"] + linesep
        message += "用户名：" + request.GET["user_name"]

    else:
        message = "你提交了空表单"
    # print(message)
    return HttpResponse(message)


@csrf_exempt
def search_post(request):
    request.encoding = "utf-8"
    ctx = {}
    if request.POST:
        ctx["user_id"] = request.POST["user_id"]
        ctx["user_name"] = request.POST["user_name"]
    response = """<h2>用户ID: %s</h2>
    <h2>用户名: %s</h2>""" % (ctx["user_id"], ctx["user_name"])
    return HttpResponse(response)
