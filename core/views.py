from django.shortcuts import redirect, render, reverse


def index(request):
    if request.user.is_authenticated:
        return redirect(reverse("posts:list"))
    else:
        return render(request, "home.html")
