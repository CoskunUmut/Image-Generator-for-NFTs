import shutil
import os
from os import walk
from image_module import ImageModule
from PIL import Image
from excel_creator import ExcelCreator
from nft_json_creator import NFTjsonCreator
from nft import NFT
# from tkinter import Tk     # from tkinter import Tk for Python 3.x
# from tkinter.filedialog import askopenfilename

# SET YOUR IMAGES PATH ##
image_modules_path = "C:/Users/Umut/OneDrive/Desktop/NFT/NFT_Dummy_Bilder"
output_folder = "output_nft"
# Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
# image_modules_path = askopenfilename()


class NFT_Generator:
    def __init__(self) -> None:
        self.nftCounter = 0
        self.nftCreatedCounter = 0
        self.maxNFT = 1
        self.finished = False
        self.image_modules_path = image_modules_path
        self.modules_dir = []
        self.image_modules = []
        self.currentModuleIterating = 0
        self.NFTs = []
        self.remove_all_files_from_output_folder()
        self.search_for_modules()
        self.create_image_modules()
        self.calculate_max_NFT()
        self.generate_NFTs()
        self.createExcel()
        self.createJson()

    def remove_all_files_from_output_folder(self):
        try:
            shutil.rmtree(output_folder)
        except:
            pass
        os.mkdir(output_folder)

    def search_for_modules(self):
        self.modules_dir = next(
            walk(self.image_modules_path), (None, [], None))[1]

    def create_image_modules(self):
        for module_dir in self.modules_dir:
            module_path = self.image_modules_path + "/" + module_dir
            image_module = ImageModule(module_path)
            self.image_modules.append(image_module)
            self.currentModuleIterating = len(self.image_modules) - 1

    def create_image(self, images_path):
        composited_image = Image.open(images_path[0])
        for i in range(1, len(images_path)):
            next_image = Image.open(images_path[i])
            composited_image = Image.alpha_composite(
                composited_image, next_image)
        return composited_image

    def calculate_max_NFT(self):
        for image_modul in self.image_modules:
            self.maxNFT = self.maxNFT * image_modul.maxImages
        for image_modul in self.image_modules:
            image_modul.calculate_max_probability(self.maxNFT)

    def get_features_path_list(self):
        features_path = []
        for image_module in self.image_modules:
            feature_path = image_module.get_feature_path()
            if feature_path == "Skip!":
                return feature_path
            features_path.append(feature_path)
        return features_path

    def set_new_module_iterating(self):
        image_index = self.image_modules[self.currentModuleIterating].set_next_image_index()
        shift = 0
        while image_index == 0:
            self.currentModuleIterating = self.currentModuleIterating - 1
            shift = shift + 1
            image_index = self.image_modules[self.currentModuleIterating].set_next_image_index()
        self.currentModuleIterating = self.currentModuleIterating + shift

    def check_end_condition(self):
        if self.nftCounter == self.maxNFT:
            self.finished = True

    def safe_NFT(self, image, features_path):
        image.save(output_folder+"/" + str(self.nftCreatedCounter) + ".png")
        nft = NFT(output_folder+"/" + str(self.nftCreatedCounter) + ".png", features_path, self.nftCreatedCounter)
        self.NFTs.append(nft)
        self.nftCreatedCounter = self.nftCreatedCounter + 1
        self.nftCounter = self.nftCounter + 1
        # print(f"NFT number {self.nftCreatedCounter} created! KA-CHING!")
        self.check_end_condition()

    def generate_NFTs(self):
        while not self.finished:
            features_path = self.get_features_path_list()
            if features_path == "Skip!":
                self.nftCounter = self.nftCounter + 1
                self.check_end_condition()
                self.set_new_module_iterating()
                continue
            NFT_image = self.create_image(features_path)
            self.safe_NFT(NFT_image, features_path)
            self.set_new_module_iterating()

    def createExcel(self):
        ExcelCreator(self.image_modules, self.maxNFT, self.NFTs)

    def createJson(self):
        NFTjsonCreator(self.NFTs)


nft_generator = NFT_Generator()
