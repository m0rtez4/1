
def my_callback(sender,**kwargs):
    print('request finished')


def create_new_user(sender,instance,created,**kwargs):
    if created :
        print('new user',instance)