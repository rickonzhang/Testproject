from django.shortcuts import render

# Create your views here.
from django.views import View
from rest_framework.views import APIView, Response

from score.models import Score
import json

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

    def post(self,request):
        # try:
        #     request_data = json.loads(request.body)
        # except Exception as e:
        #     return Response({"code": 40000, "msg": "请求格式错误"})
        s_id = request.POST.get('s_id')
        name = request.POST.get('name')
        score = request.POST.get('score')

        Score.objects.create(s_id=s_id,name=name,score=score)
        return Response({'msg': '添加成功', 'code': 20000})

    def delete(self, request):
        s_id = request.GET.get("s_id", None)
        if not s_id:
            return Response({'msg': '缺少必要参数', 'code': 40000})
        try:
            Score.objects.filter(s_id=s_id).delete()
        except Exception as e:
            return Response({'msg': '删除失败', 'code': 500})
        else:
            return Response({'msg': '删除成功', 'code': 20000})

    def put(self, request):
        s_id = request.POST.get('s_id')
        name = request.POST.get('name')
        score = request.POST.get('score')

        if not s_id:
            return Response({'msg': '缺少必要参数', 'code': 40000})
        try:
            Score.objects.filter(s_id=s_id).update(name=name,score=score)
        except Exception as e:
            return Response({'msg': '更改失败', 'code': 500})
        else:
            return Response({'msg': '更改成功', 'code': 20000})