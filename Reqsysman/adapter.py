from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

class LocalhostSocialAccountAdapter(DefaultSocialAccountAdapter):
    def is_open_for_signup(self, request, sociallogin):
        return False
