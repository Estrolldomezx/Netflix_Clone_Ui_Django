from django.shortcuts import render
# Create your views here.
def hello(request): #create view
    return render(request, 'index.html', 
    {
        'starring':'Starring: Chris Hemsworth, Tom Hiddleston, Mark Ruffalo',
        'creator':'Directed by Taika Waititi',
        'background':'ttps://asset-a.grid.id/crop/0x0:0x0/x/photo/2020/09/18/47557070.jpeg',
    }) #reference templates that i made it

#def europe(request):
#   return render(request,'europe.html')
