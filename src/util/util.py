import json
import pandas as pd
import pyarrow as pyarrow
import pyarrow.parquet as parquet


def load_and_merge_datasets(dataset_classes):
    """
    複数のデータセットをロードしてマージする
    :param dataset_classes: データセットクラスのリスト
    :return: マージされたデータセット
    """
    all_data = []
    for dataset_class in dataset_classes:
        dataset = dataset_class.load_dataset()
        all_data.extend(dataset)
    return all_data


def save_data_to_file(data, file_path):
    """
    データをparquetファイルに保存する
    :param data: 保存するデータ
    :param file_path: 保存するファイルのパス
    """
    df = pd.DataFrame(data)
    table = pyarrow.Table.from_pandas(df)
    parquet.write_table(table, file_path)
