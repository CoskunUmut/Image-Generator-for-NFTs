import json
import os
import shutil

output_nft = "output_nft"
output_json = "output_nft_json"


class NFTjsonCreator:
    def __init__(self, NFTs) -> None:
        self.NFTs = NFTs
        self.json_data = {}
        self.remove_all_files_from_output_folder()
        for NFT in self.NFTs:
            self.fillData(
                f"This is NFT number {NFT.ID}",
                f"/{NFT.ID}.png",
                f"/{NFT.ID}.png",
                NFT.ID,
                NFT.moduleFeaturesDict)
            self.saveJsonData(NFT.ID)

    def fillData(self, description, external_url, image_path, name, moduleFeaturesDict):
        data = {}
        data['description'] = description
        data['external_url'] = external_url
        data['image'] = image_path
        data['name'] = name
        attributes = []
        for module, feature in moduleFeaturesDict.items():
            temp_dict = {}
            temp_dict["trait_type"] = module
            temp_dict["value"] = feature
            attributes.append(temp_dict)
        data['attributes'] = attributes

        self.json_data = data

    def remove_all_files_from_output_folder(self):
        try:
            shutil.rmtree(output_json)
        except:
            pass
        os.mkdir(output_json)

    def saveJsonData(self, ID):
        with open(str(ID)+'.json', 'w', encoding='utf-8') as f:
            json.dump(self.json_data, f, sort_keys=True, ensure_ascii=False)
        shutil.move(str(ID)+'.json', output_json+'/'+str(ID)+'.json')
