from django.shortcuts import render
from django.views.generic import View
from apps.mainp.models import MainPage
from django.http import HttpRequest
from apps.httpreq.models import HttpReqStore


class Index(View):
    @staticmethod
    def get(request):
        udata = dict()
        for e in MainPage.objects.all():
            title = e.title
            name = e.name
            lastname = e.lastname
            bdate = e.bdate
            cemail = e.cemail
            cjabber = e.cjabber
            cskype = e.cskype
            bio = e.bio
            ocontacts = e.ocontacts
            udata['title'] = title
            udata['name'] = name
            udata['lastname'] = lastname
            udata['bdate'] = bdate
            udata['cemail'] = cemail
            udata['cjabber'] = cjabber
            udata['cskype'] = cskype
            udata['bio'] = bio
            udata['ocontacts'] = ocontacts
        if request.method == 'GET' or request.method == 'POST':
            HttpReqStore.objects.create(htresponce=request)

        return render(request, 'base.html', udata)



