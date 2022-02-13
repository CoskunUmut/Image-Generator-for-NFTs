
import xlsxwriter
import math
column_size = 40


class ExcelCreator:
    def __init__(self, images_module, maxNFT, NFTs) -> None:
        self.images_module = images_module
        self.NFTs = NFTs
        self.maxNFT = maxNFT
        self.features_dict = dict()
        self.create_occurrences_table()
        self.create_NFT_table()

        # self.create_NFT_rarity_list()

    def set_column_size(self, worksheet):
        worksheet.set_column(0, 100, column_size)

    def set_bold(self, workbook, worksheet):
        cell_format = workbook.add_format({'bold': True, 'align': 'left'})
        cell_format.set_bold()
        worksheet.set_column('A1:ZZ1', None, cell_format)

    def create_occurrences_table(self):
        workbook = xlsxwriter.Workbook('FeatureOccurencesList.xlsx')
        worksheet = workbook.add_worksheet()
        self.set_bold(workbook, worksheet)
        self.set_column_size(worksheet)
        worksheet.write(0, 0, "Feature Name")
        worksheet.write(0, 1, "Occurences [No.]")
        worksheet.write(0, 2, "Occurences [ % ]")

        row = 0
        for image_module in self.images_module:
            for image_feature in image_module.images_feature:
                row = row + 1
                worksheet.write(row, 0, image_module.moduleType + "/" + image_feature.featureType)
                worksheet.write(row, 1, str(image_feature.feature_actually_used) + " / " +
                                str(int(image_module.maxOccurance)))
                feature_probability = float(image_feature.feature_actually_used) / image_module.maxOccurance*100
                worksheet.write(row, 2, str(feature_probability))
                self.features_dict[image_feature.feature_name] = feature_probability
        workbook.close()

    def filter_module_and_feature(self, feature_path):
        indexStartModule = feature_path.find("-")
        indexEndModule = feature_path.rfind(".")
        return feature_path[indexStartModule+1:indexEndModule]

    def create_NFT_table(self):
        workbook = xlsxwriter.Workbook('NFTs.xlsx')
        worksheet = workbook.add_worksheet()
        # self.set_column_size(worksheet)
        worksheet.set_column(0, 0, 5)
        worksheet.set_column(1, 100, 40)
        merge_format1 = workbook.add_format({
            'bold': 1,
            'border': 1,
            'align': 'left',
            'valign': 'vcenter',
            'fg_color': 'yellow'})
        merge_format2 = workbook.add_format({
            'bold': 1,
            'border': 1,
            'align': 'left',
            'valign': 'vcenter',
            'fg_color': 'orange'})
        row = 0
        merge_format = []
        toggle_format = True
        nftCounter = 0
        for NFT in self.NFTs:
            worksheet.write(row, 0, NFT.image_path)
            row = row + 1
            if toggle_format:
                merge_format = merge_format1
                toggle_format = not toggle_format
            else:
                merge_format = merge_format2
                toggle_format = not toggle_format
            worksheet.merge_range(row-1, 0, row, 0, nftCounter, merge_format)
            nftCounter = nftCounter + 1
            col = 0
            total_probability = 1.0
            for feature_path in NFT.features_path:
                col = col + 1
                feature_probability = float(self.features_dict[feature_path] / 100)
                total_probability = total_probability * feature_probability
                module_feature_text = self.filter_module_and_feature(feature_path)
                worksheet.write(row-1, col, module_feature_text, merge_format)
                worksheet.write(row, col, feature_probability, merge_format)
            col = col + 1
            worksheet.merge_range(row-1, col, row, col, total_probability, merge_format)
            NFT.rarity = total_probability
            row = row + 1
        workbook.close()
