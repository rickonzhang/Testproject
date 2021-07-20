from django.shortcuts import render

# Create your views here.
from django.views import View
from rest_framework.views import APIView, Response

from score.models import Score


class StudentView(APIView):
    def get(self, request):
        s_id = request.GET.get("s_id", None)
        if not s_id:
            return Response({'msg': '缺少必要参数', 'code': 40000, 'config': []})
        q1 = Score.objects.filter(s_id=s_id)
        for i in q1:
            data = {"s_id": i.s_id,
                    "name": i.name,
                    "score": i.score
                    }
        return Response({"data": data})
