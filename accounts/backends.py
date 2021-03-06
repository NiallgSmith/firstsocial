from models import User
import datetime
import arrow


class EmailAuth(object):
    def authenticate(self, email=None, password=None):

        try:
            user = User.objects.get(email=email)
            if (user.check_password(password)) and (user.subscription_end > arrow.now()):
                return user

        except User.DoesNotExist:
            return None



    def get_user(self, user_id):
        """ retrieve an instance of a user"""
        try:
            user = User.objects.get(pk=user_id)
            if user.is_active:
                return user
            return None
        except User.DoesNotExist:
            return None
