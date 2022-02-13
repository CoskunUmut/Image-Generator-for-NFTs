

class NFT:
    def __init__(self, image_path, feature_paths, ID) -> None:
        self.ID = ID
        self.image_path = image_path
        self.features_path = self.create_features_path_list(feature_paths)
        self.moduleFeaturesDict = self.extract_all_moduleFeatureTypes(feature_paths)
        self.rarity = 0

    def extract_all_moduleFeatureTypes(self, feature_paths):
        moduleFeaturesDict = dict()
        for feature_path in feature_paths:
            feature_path = self.filter_module_and_feature(feature_path)
            slashIndex = feature_path.find("/")
            module = feature_path[:slashIndex]
            feature = feature_path[slashIndex+1:]
            probabilitySignIndex = feature.rfind("_")
            if probabilitySignIndex is not -1:
                feature = feature[:probabilitySignIndex]
            moduleFeaturesDict[module] = feature
        return moduleFeaturesDict

    def filter_module_and_feature(self, feature_path):
        indexStartModule = feature_path.find("-")
        indexEndModule = feature_path.rfind(".")
        return feature_path[indexStartModule+1:indexEndModule]

    def create_features_path_list(self, feature_paths):
        for i in range(len(feature_paths)):
            last_underline_index = feature_paths[i][:feature_paths[i].rfind("/")].rfind("/")
            feature_name = feature_paths[i][last_underline_index+1:]
            feature_paths[i] = feature_name
        return feature_paths
