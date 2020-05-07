from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import requests
import json
from myapi.serializers import *
from myapi.models import *





class CategoryViews(APIView):
	def get(self, request):
		response = {}
		pk =  request.GET.get('id')
		if pk:
			Category_qs = Category.objects.filter(id=pk)
		else:
			Category_qs = Category.objects.all()
		for data in Category_qs:
			response[data.id] = {
				"id":data.id,
				"CategoryName":data.categoryName,
				"created_at":data.created_at,
				"status":data.status
				}
		return Response(response.values(),status=status.HTTP_200_OK)

class IPCViews(APIView):
	def get(self, request):
		response = {}
		pk = request.GET.get('id')
		if pk:
			Ipc_qs = IPC.objects.filter(id=pk)
		else:
			print("hello world")
			Ipc_qs = IPC.objects.all()
		for data in Ipc_qs:
			response[data.id] = {
				"id": data.id,
				"IPC_NUMBER":data.IPC_NUMBER,
				"DESCRIPTION":data.DESCRIPTION,
				"Image":data.IMAGE.url,
				"STATUS":data.STATUS,
				"CREATED_AT":data.CREATED_AT
			}
		return Response(response.values(),status=status.HTTP_200_OK)