from os import walk
from image_feature import ImageFeature


class ImageModule:
    def __init__(self, module_path) -> None:
        self.module_path = module_path
        self.feature_paths = []
        self.images_feature = []
        self.maxImages = 0
        self.currentImageIndex = 0
        self.create_images_path()
        self.maxOccurance = 0
        self.moduleType = ""
        self.get_module_type()

    def get_module_type(self):
        startIndexModuleType = self.module_path.rfind("/")
        self.moduleType = self.module_path[startIndexModuleType+3:]

    def create_images_path(self):
        self.feature_paths = next(walk(self.module_path), (None, None, []))[2]
        for i in range(len(self.feature_paths)):
            image_feature_path = str(self.module_path) + "/" + str(self.feature_paths[i])
            image_feature = ImageFeature(image_feature_path)
            self.images_feature.append(image_feature)
        self.maxImages = len(self.feature_paths)

    def calculate_max_probability(self, maxNFT):
        self.maxOccurance = float(maxNFT / len(self.feature_paths))

    def set_next_image_index(self):
        self.currentImageIndex = self.currentImageIndex + 1
        if self.currentImageIndex == self.maxImages:
            self.currentImageIndex = 0
        return self.currentImageIndex

    def get_feature_path(self):
        if self.images_feature[self.currentImageIndex].calculate_if_feature_is_skipped():
            return "Skip!"
        return self.images_feature[self.currentImageIndex].get_path()
