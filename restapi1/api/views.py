from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def emp_view(request):
    emp={
        'eno':100,
        'ename':"sam",
        'esal':20000,
        'eadd':"hyd"

    }
    res="<h1>employee no is:{}<br>Employye name is:{}<br>Employee salary is:{}<br>Employee address is:{}</h1>".format(emp['eno'],emp['ename'],emp['esal'],emp['eadd'])

    return HttpResponse(res)

import json
def emp_jsonview(request):
    emp={
        'eno':100,
        'ename':"sam",
        'esal':20000,
        'eadd':"hyd"

    }
    json_res=json.dumps(emp)
    return HttpResponse(json_res,content_type="aplication/json")