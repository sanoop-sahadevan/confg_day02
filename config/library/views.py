from django.shortcuts import render

# Create your views here.
def Home_page(request):
    
    return render(request,"home.html")

def Books_page(request):
    list=[
        "florida",
        "helen",
        "sweets",
        "wednesday",
        "stranger"
    ]
    context={
        "context":list
    }
    return render(request,"Books.html",context)



def Book_detail(request,id):
     h= f"THis is book {id}'s detail page"
     context={
        "content":h
     }
     return render(request,"Book_detail.html",context,)
   

  