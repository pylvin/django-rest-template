from django.utils.translation import ugettext_lazy as _


def get_current_user(user):
    from apps.account.models import Student, Teacher
    current = None
    if user.user_type == 'student':
        current = Student.objects.filter(id=user.id).last()
    elif user.user_type == 'teacher':
        current = Teacher.objects.filter(id=user.id).last()
    return current
