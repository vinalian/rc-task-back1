from pandas import read_csv, DataFrame

__all__ = [
    'Main_script'
]


class Main_script:
    def __init__(self, file_path):
        self.data = read_csv(file_path, delimiter=';')
        self.data['код'] = self.data['код'].astype(str)
        self.data = self.data.fillna('')
        self.years = self.data.columns[2:]
        self.ready_data = DataFrame(columns=['проект'] + list(self.years))

    def __traverse_tree(self, code, project):
        children = self.data[self.data['код'].str.startswith(code + '.')]

        if children.empty:
            new_row = {'проект': project}
            for year in self.years:
                new_row[year] = self.data[self.data['код'] == code][year].values[0]
            self.ready_data.loc[len(self.ready_data)] = new_row

        else:
            for i, row in children.iterrows():
                self.__traverse_tree(row['код'], project + row['проект'])

    def process_data(self):
        root_codes = self.data[self.data['код'].str.count('.') == 0]['код'].values
        for code in root_codes:
            self.__traverse_tree(code, '')
