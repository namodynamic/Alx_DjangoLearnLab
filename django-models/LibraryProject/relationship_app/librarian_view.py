from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarians'


@user_passes_test(is_librarian)
def librarian_dashboard(request):
    return render(request, 'librarian.html')