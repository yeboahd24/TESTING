class Image:
    def __init__(self):
        self.url = 'https://cdn.discordapp.com/attachments/639087150109879296/640109812098135040/image0.png'

def check_image_url(image_url):
    if image_url and hasattr(image_url, 'url'):
        return image.url
    else:
        return None


image = Image()
#print(check_image_url(image_url=image))

from django.contrib.auth.backends import  BaseBackend

# Custom BaseBackend with email as username and password
class EmailBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


