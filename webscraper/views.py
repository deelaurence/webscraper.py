from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer 
from .models import JobListing
from .serializers import JobListingSerializer
from rest_framework.response import Response
from .scraper import scrape_website
from rest_framework.views import APIView
from .regex import clean_deverence



class JobListingViewSet(APIView):
    renderer_classes = [JSONRenderer]  # Specify JSONRenderer for the response

    def get(self, request):
        # Replace 'https://example.com' with the URL you want to scrape
        website_url = request.GET.get('url', '')  # 'url' is the query parameter name

        if not website_url:
            return Response({'message': 'Website URL is required'}, status=400)

        scraped_data = scrape_website(website_url)
        scraped_data=clean_deverence(scraped_data)
        if scraped_data:
            scraped_data_obj = JobListing(title='Examples Title', description=scraped_data)
            scraped_data_obj.save()
            serializer = JobListingSerializer(scraped_data_obj)
            return Response(serializer.data)
        else:
            return Response({'message': 'Failed to scrape data from the website'}, status=400)