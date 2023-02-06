from authentication.models import  User
from django.contrib.auth.models import Group

def main():
    print('creating admin user')
    admin = User.objects.create(
        is_superuser=True,
        username='admin',
        first_name='Jon',
        last_name='Doe',
        rut='12345678',
        email='admin@example.com',
        is_staff=True,
        # branch= ,
        # company= ,
    )
    admin.set_password('12345678')
    admin.save()
    admin.groups.add(Group.objects.get(name='admin'))

main()
exit()
