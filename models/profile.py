import json

class UserProfile:
    def __init__(self, profile_file='profiles.json'):
        self.profile_file = profile_file
        self.profiles = self.load_profiles()

    def load_profiles(self):
        try:
            with open(self.profile_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_profiles(self):
        with open(self.profile_file, 'w') as file:
            json.dump(self.profiles, file, indent=4)

    def add_profile(self, name, settings):
        self.profiles[name] = settings
        self.save_profiles()

    def get_profile(self, name):
        return self.profiles.get(name, None)
