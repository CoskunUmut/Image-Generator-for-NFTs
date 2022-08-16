# Image Generator for NFTs
 
 ## Description
 This is an image generator that combinatorially creates images from a set of image features.
 The tool is intended to create typical  Non-Fungible Token (NFT) images. Therefore alongside the generated images,
 meta data is also created for uploading it to e.g. OpenSea is created. 
 
 Additionally, a script "json_updater.py" can be used to update the IPFS CID in the image meta data.
 
 ## Usage - Generate Images
 1) Make a folder for every image feature:
 
 ![grafik](https://user-images.githubusercontent.com/98838105/184851368-186d42fd-7a77-480e-ace2-ce92cfff2089.png)
 
**Note**: Most rear features need to be at the very top. That is why I used "0_" for the background folder.

2) Put any number of images within these folders:

![grafik](https://user-images.githubusercontent.com/98838105/184852667-c0a148ac-d0bf-47c5-b64c-263e349523ad.png)

**Note**: The images have to following naming convention: [Name]_[Probability]. So an image called RedEyes_40.png will appear with a probability of 40%. Default is 100%.

3) Execute the main script.

## Outputs

The images are output in the /output_nft folder. 
Along with it an output_nft_json is created that contains meta data for each image.

![grafik](https://user-images.githubusercontent.com/98838105/184854309-8de776c8-62bb-4266-bb54-dbd3a4213dea.png)



## Usage - IPFS and CID:

1) Archieve the output images and put it on IPFS to get the CID of the archieve.
2) Put the CID value into the variable CID in "json_updater.py"
3) While the .json data is still in the /output_nft_json folder, execute the "json_updater.py" script

