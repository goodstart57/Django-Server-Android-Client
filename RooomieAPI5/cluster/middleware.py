from django.db.models.query import QuerySet
from django.http import JsonResponse

from .views import tm


def json_response(qs):
    mylist = []
    if tm.compType("getMemInfo"):
        print("send five member information")
        for instance in qs:
            mylist.append({
                'STUD_ID': instance.STUD_ID,
                'ID':       instance.ID,
                'PWD':      instance.PWD,
                'NAME':     instance.NAME,
                'GENDER':   instance.GENDER,
                'PHONE':    instance.PHONE,
                'EMAIL':    instance.EMAIL,
                'MAJOR':    instance.MAJOR
            })

    elif tm.compType("listAllUserIDs"):
        print("send five member information")
        for instance in qs:
            mylist.append({
                'ID': instance.ID
            })

    return JsonResponse(mylist, safe=False)


class JsonResponseMiddleware(object):
    def process_response(self, request, response):
        if isinstance(response, QuerySet):
            return json_response(response)
        return response
