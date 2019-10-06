from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image, Location, Category


# Create your views here.

def welcome(request):
    images = Image.get_all_images()
    locations = Location.get_all_locations()
    
    return render(request, 'welcome.html', {'images': images, 'locations': locations})


def search_results(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"
        
        return render(request,'search.html',{"message":message, "images":searched_images, "category":search_term})
    
    else:
        message = "You haven't searched for any category"
        
        return render(request, 'search.html', {"message":message})
    
    
def location(request,location):
    selected_location = Location.objects.get(id = location)
    images = Image.objects.filter(location = selected_location.id)
    
    return render(request, 'location.html', {"location":selected_location,"images":images})
