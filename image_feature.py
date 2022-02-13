import random
# random.seed(1000)

# Make this higher if not enough NFTs are created!
global_likelihood_adjuster = 0.0


class ImageFeature:
    def __init__(self, feature_path) -> None:
        self.feature_path = feature_path
        self.likelihood = 100
        self.feature_actually_used = 0
        self.feature_name = ""
        self.get_feature_name()
        self.get_likelihood()

    def get_path(self):
        return self.feature_path

    def get_feature_name(self):
        # finds second "/" from BEHIND
        last_underline_index = self.feature_path[:self.feature_path.rfind("/")].rfind("/")
        self.feature_name = self.feature_path[last_underline_index+1:]

    def get_likelihood(self):
        last_underline_index = self.feature_path.rfind("_")
        likelihood_substring = self.feature_path[last_underline_index+1:len(self.feature_path)]
        dot_index = likelihood_substring.rfind(".")
        if dot_index > 6:  # probably not found _xx.png
            return
        try:
            self.likelihood = float(likelihood_substring[0:dot_index])
        except:
            self.likelihood = 100

    def calculate_if_feature_is_skipped(self):
        result = True
        random_check_number = random.uniform(0, 100)
        if self.likelihood >= random_check_number * (1.0-global_likelihood_adjuster):
            result = False
            self.feature_actually_used = self.feature_actually_used + 1
        return result
