import pandas as pd
from config import ProductionConfig as cfg

class data_merging_class:

    def __init__(self):
        pd.set_option('display.max_columns', None)
        pd.set_option('max_colwidth', None)


    def read_tsv_file(self, file_path, column_name_list):

        df = pd.read_csv(file_path, sep = '\t', usecols=column_name_list)
        df.columns = cfg.new_column_names_list  # rename column names

        rename_category = {'HOF': 'cyberbullying'}
        df['binary_classes'].replace(rename_category, inplace=True)

        return df


    def read_excel(self, file_path, column_name_list):

        df =  pd.read_excel(file_path, usecols=column_name_list)
        df.columns = cfg.new_column_names_list  # rename column names

        rename_category = {'HOF': 'cyberbullying'}
        df['binary_classes'].replace(rename_category, inplace=True)

        return df


    def read_csv(self, file_path, column_name_list):

        df = pd.read_csv(file_path, usecols=column_name_list)
        df.columns = cfg.new_column_names_list

        rename_category = {'HOF': 'cyberbullying'}
        df['binary_classes'].replace(rename_category, inplace=True)

        return df


    def read_txt(self, file_path):

        df = pd.read_table(file_path, header=None)
        df.columns =  ['binary_classes', 'text']  # rename columns
        df['multiple_classes'] = None  # add new column

        binary_to_category = {0: 'cyberbullying', 1: 'NOT'}
        df['binary_classes'].replace(binary_to_category, inplace=True)

        return df


    def combine_data(self):

        tsv_df_1 = self.read_tsv_file(cfg.tsv_dataset_1, cfg.existing_column_name_list)
        tsv_df_2 = self.read_tsv_file(cfg.tsv_dataset_2, cfg.existing_column_name_list)
        xlsx_df_3 = self.read_excel(cfg.xlsx_dataset_3, cfg.existing_column_name_list_2)
        csv_df_4 = self.read_csv(cfg.csv_dataset_4, cfg.existing_column_name_list_2)
        csv_df_5 = self.read_csv(cfg.csv_dataset_5, cfg.existing_column_name_list_2)
        txt_df_6 = self.read_txt(cfg.txt_dataset_6)

        df_list = [tsv_df_1, tsv_df_2, xlsx_df_3, csv_df_4, csv_df_5, txt_df_6]
        combined_df = pd.concat(df_list)

        combined_df.drop_duplicates(keep='last', inplace=True)

        combined_df.to_csv(cfg.combined_dataset, index=False)


if __name__ == "__main__":

    obj = data_merging_class()

    obj.combine_data()