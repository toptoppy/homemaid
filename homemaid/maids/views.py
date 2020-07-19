from django.http import HttpResponse
from django.views import View

from .models import Maid

class MaidListView(View):
    def get(self, request):
        maids = Maid.objects.all()
        html = ''

        for maid in maids:
            html += f'<li>{maid.name}</li>'
        
        return HttpResponse(html)
    

def maid_another_list_view(request):
    return HttpResponse()
