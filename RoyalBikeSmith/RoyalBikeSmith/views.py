from django.shortcuts import render

# Render home page
def homePage(request):
    homePageName={'homePageName':'Royal Bike Smith'}
    return render(request, 'index.html', homePageName)