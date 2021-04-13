from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def reverse(request):
    user_text = request.GET['usertext']
    words = user_text.split()
    word = len(words)
    reverse_text = user_text [::-1]
    return render(request, "reverse.html", {'usertext': user_text,
                                            "reversetext":reverse_text,
                                            'world': word })