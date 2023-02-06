from django.contrib.auth.models import Group
from core.custom_permissions import GROUPS


def main():
    for group in GROUPS:
        print('Getting or creating user group: {}'.format(group))
        Group.objects.get_or_create(name=group)

main()
exit()
