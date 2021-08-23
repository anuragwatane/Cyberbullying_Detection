import pandas as pd
from config import ProductionConfig as cfg

class data_merging_class:

    def __init__(self):
        pd.set_option('display.max_columns', None)
        pd.set_option('max_colwidth', None)


    def read_tsv_file(self, file_path, column_name_list):

        df = pd.read_csv(file_path, sep = '\t', usecols=column_name_list)
        df.columns = cfg.new_column_names_list  # rename column names

        rename_category = {'HOF': 'cyberbullying', 'PRFN': 'OFFN'}
        df['binary_classes'].replace(rename_category, inplace=True)

        df['multiple_classes'].replace(rename_category, inplace=True)

        return df


    def read_excel(self, file_path, column_name_list):

        df =  pd.read_excel(file_path, usecols=column_name_list)
        df.columns = cfg.new_column_names_list  # rename column names

        rename_category = {'HOF': 'cyberbullying', 'PRFN': 'OFFN'}
        df['binary_classes'].replace(rename_category, inplace=True)

        df['multiple_classes'].replace(rename_category, inplace=True)

        return df


    def read_csv(self, file_path, column_name_list):

        df = pd.read_csv(file_path, usecols=column_name_list)

        column_rename_dict = {'tweet': 'text', 'task1': 'binary_classes', 'task2': 'multiple_classes', 'class': 'multiple_classes'}
        df.rename(columns=column_rename_dict, inplace=True)

        if 'binary_classes' not in df.columns:
            df['binary_classes'] = df['multiple_classes']

        unique_labels = df['binary_classes'].unique()

        if 'HOF' in unique_labels or 'racism' in unique_labels:
            rename_category = {'HOF': 'cyberbullying', 'racism': 'cyberbullying', 'sexism': 'cyberbullying', 'none': 'NOT'}
            df['binary_classes'].replace(rename_category, inplace=True)

        elif 2 in df['binary_classes'].unique():
            rename_category = {0: 'cyberbullying', 1: 'cyberbullying', 2: 'NOT'}
            df['binary_classes'].replace(rename_category, inplace=True)

        unique_labels = df['multiple_classes'].unique()

        if 'PRFN' in unique_labels or 'racism' in unique_labels:
            rename_category = {'PRFN': 'OFFN', 'racism': 'OFFN', 'sexism': 'OFFN', 'none': 'NONE'}
            df['multiple_classes'].replace(rename_category, inplace=True)

        elif 2 in df['multiple_classes'].unique():
            rename_category = {0: 'HATE', 1: 'OFFN', 2: 'NONE'}
            df['multiple_classes'].replace(rename_category, inplace=True)

        return df


    def read_txt(self, file_path):

        df = pd.read_table(file_path, header=None)
        df.columns =  ['binary_classes', 'text']  # rename columns
        df['multiple_classes'] = 'NONE'  # add new column

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
        csv_df_7 = self.read_csv(cfg.csv_dataset_7, cfg.existing_column_name_list_3)
        csv_df_9 = self.read_csv(cfg.csv_dataset_9, cfg.existing_column_name_list_4)

        df_list = [tsv_df_1, tsv_df_2, xlsx_df_3, csv_df_4, csv_df_5, txt_df_6, csv_df_7, csv_df_9]
        combined_df = pd.concat(df_list)

        combined_df.drop_duplicates(keep='last', inplace=True)

        combined_df.to_csv(cfg.combined_dataset, index=False)


if __name__ == "__main__":

    obj = data_merging_class()

    obj.combine_data()