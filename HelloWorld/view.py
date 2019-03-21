#!/usr/bin/env python
# coding:utf-8
# author: sinlyon date 2019/3/21 0021
# from django.http import HttpResponse
import time

from django.shortcuts import render


def hello(request):
    context = {}
    context['hello'] = 'Hello World. '
    context['str1'] = "abcdef"
    context['users'] = ["sinlyon", "amanbo"]
    context["date"] = time.time()
    return render(request, 'hello.html', context)
