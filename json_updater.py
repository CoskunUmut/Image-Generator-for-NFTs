import json
import os
import shutil
import os
import os.path

output_nft = "output_nft"
output_json = "output_nft_json"


CID = "ipfs://QmfXmvBAnzatLsh7DdXM7PS67pwWpRuVANpVhiat2wCmiC"


class NFTjsonCreator:
    def __init__(self) -> None:
        pass

    def update_image_url(self):
        path, dirs, files = next(os.walk(output_json))
        file_count = len(files)
        for i in range(file_count):
            a_file = open(f'output_nft_json/{i}.json', "r")
            json_object = json.load(a_file)
            json_object["image"] = CID+json_object["image"]
            print(json_object["image"])
            a_file = open(f'output_nft_json/{i}.json', "w")
            json.dump(json_object, a_file)
            a_file.close()


nftJsonCreator = NFTjsonCreator()
nftJsonCreator.update_image_url()
