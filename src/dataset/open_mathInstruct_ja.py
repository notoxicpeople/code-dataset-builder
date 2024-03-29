from datasets import load_dataset
from tqdm import tqdm

from config.config import *


class OpenMathInstructJa:
    def load_dataset(self):
        """データセットのロードと加工を行う"""
        dataset = self._load_huggingface_dataset()
        filtered_data = self._filter_records(dataset["train"])
        return self._format_data(filtered_data)

    def _load_huggingface_dataset(self):
        """Hugging Faceからデータセットのロード"""
        return load_dataset(DATASET_NAME_OPEN_MATH_INSTRUCT)

    def _filter_records(self, dataset):
        """特定の条件に基づいてデータセットからレコードをフィルタリング"""
        return [record for record in tqdm(dataset, desc="Filtering records") if self._is_valid_record(record)]

    def _is_valid_record(self, record):
        """レコードが条件に合致するか確認"""
        return record.get("generated_solution_ja") and "<llm-code>" in record["generated_solution_ja"] and record.get("question_ja")

    def _format_data(self, data):
        """データを指定されたフォーマットに変換"""
        return [
            {**COMMON_DATA_OPEN_MATH_INSTRUCT, "id": f"OM_{str(record['index'])}", "content": f"{record['question_ja']}{SEPARATOR_OPEN_MATH_INSTRUCT}{record['generated_solution_ja']}"}
            for record in data
        ]
