from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 
from .models import *


class Experiences(APIView):
    def get(self, request):
        experiences = ExperienceItem.objects.all().order_by('year').reverse()
        return Response([{
            'year': experience.year,
            'title': experience.title,
            'organisation': experience.organisation,
            'duration': experience.duration,
            'details': experience.details
        } for experience in experiences])
        
        
class Portfolio(APIView):
    def get(self, request):
        portfolio = PortfolioItem.objects.all()
        return Response([{
            'title': item.title,
            'imgUrl': item.imgUrl,
            'stack': [stack.name for stack in item.stack.all()]
        } for item in portfolio])   