

class NFT:
    def __init__(self, image_path, feature_paths) -> None:
        self.image_path = image_path
        self.features_path = self.create_features_path_list(feature_paths)
        self.rarity = 0

    def create_features_path_list(self, feature_paths):
        for i in range(len(feature_paths)):
            last_underline_index = feature_paths[i][:feature_paths[i].rfind("/")].rfind("/")
            feature_name = feature_paths[i][last_underline_index+1:]
            feature_paths[i] = feature_name
        return feature_paths
