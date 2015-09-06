from django.shortcuts import render
from django.views.generic import View
from apps.httpreq.models import HttpReqStore


class Httpreq(View):
    @staticmethod
    def get(request):
        udata = {}

        for e in HttpReqStore.objects.all():
            ident = e.id
            htresponce = e.htresponce
            atime = e.atime
            udata['ident'] = ident
            udata['htresponce'] = htresponce
            udata['atime'] = atime

        if request.method == 'GET' or request.method == 'POST':
            HttpReqStore.objects.create(htresponce=request)

        title = str(HttpReqStore.objects.count()) + ' Requests total'
        udata['title'] = title

        return render(request, 'httpreq.html', udata)