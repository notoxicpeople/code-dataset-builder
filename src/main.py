from dotenv import load_dotenv

from dataset.open_mathInstruct_ja import OpenMathInstructJa
from dataset.the_stack_v2 import TheStackV2
from util.util import load_and_merge_datasets, save_data_to_file


def main():
    dataset_classes = [OpenMathInstructJa(), TheStackV2()]
    merged_data = load_and_merge_datasets(dataset_classes)
    save_data_to_file(merged_data, "result.parquet")


if __name__ == "__main__":
    main()
