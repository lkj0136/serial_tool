from models.profile import UserProfile

class ProfileController:
    def __init__(self):
        self.user_profile = UserProfile()

    def save_profile(self, name, settings):
        self.user_profile.add_profile(name, settings)

    def load_profile(self, name):
        return self.user_profile.get_profile(name)
