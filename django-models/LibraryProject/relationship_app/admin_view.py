from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test


@user_passes_test(lambda user: user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin')
def admin_view(request):
    return render(request, 'relationship_app/admin_dashboard.html')