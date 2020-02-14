"""
analyst_task.py
~~~~~~~~~~~~~~~
Author: William Murphy

"""
import os
import xlrd
import pandas as pd
from pathlib import Path
from typing import Dict, List
from pprint import pprint

# Setup for displaying the max columns in pandas
pd.set_option('display.max_colwidth', -1)


class ProcessExcelData(object):
    """Process excel data into a Pandas DataFrame"""

    def __init__(self):
        self.file_names: List[str] = []
        self.data_frames: Dict[str, Dict[str, pd.DataFrame]] = {}

    def load_data_sets(self, *args) -> None:
        """Load in the data sets into the file_names list.

        :arg args: str:
        :returns None:
        """
        for a in args:
            # Load each data set into the files list, if the file exists.
            if (type(a) is str
                    and os.path.exists(os.path.join(Path(__file__).parent, a))):
                self.file_names.append(os.path.join(Path(__file__).parent, a))
            else:
                raise IOError(f"IOError: File: {os.path.join(Path(__file__).parent, a)} not found.")

    def read_excel_to_df(self) -> None:
        """Load each excel sheet into a Pandas DataFrame
        :arg chunk_size: int:
        :returns None:
        """
        for f in self.file_names:
            current = {}
            xl = pd.ExcelFile(f)
            for sheet_name in xl.sheet_names:
                reader = xl.parse(sheet_name=sheet_name)
                current.update({sheet_name: reader})
            self.data_frames.update({f: current})

    def extract_brooklyn_data(self, file_name: str) -> pd.DataFrame:
        """Extract the Brooklyn borough data."""
        f = os.path.join(Path(__file__).parent, file_name)
        borough_df = self.data_frames.get(f)
        return borough_df[borough_df["Borough"]=="Brooklyn"]






def main():
    #school_data = "demographic-snapshot-2014-15-to-2018-19-(public).xlsx"
    demographic_data = "school-ela-results-2013-2019-(public).xlsx"

    data_processor = ProcessExcelData()
    data_processor.load_data_sets(demographic_data)
    data_processor.read_excel_to_df()
    print(data_processor.data_frames.keys())




if __name__ == '__main__':
    main()


