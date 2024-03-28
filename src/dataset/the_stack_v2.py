import os

import boto3
from tqdm import tqdm
from datasets import load_dataset
from smart_open import open

from config.config import *


class TheStackV2:
    def __init__(self):
        self.s3_client = None
        self.sampled_byte_size = SAMPLE_SIZE_TOKENS * TOKEN_SIZE_BYTES

    def load_dataset(self):
        """データセットのロードと処理"""
        dataset = self._load_huggingface_dataset()
        all_contents = self._collect_data(dataset)
        return self._format_data(all_contents)

    def _load_huggingface_dataset(self):
        """huggingfaceからデータセットのロード"""
        return load_dataset(DATASET_NAME_THE_STACK_V2, split="train", streaming=True, token=HUGGING_FACE_TOKEN)

    def _collect_data(self, dataset):
        """データセットからデータを収集し、条件に一致するものをダウンロード"""
        total_bytes_downloaded = 0
        all_contents = []

        with tqdm(total=self.sampled_byte_size, desc="Downloading") as progress_bar:
            for row in dataset:
                if total_bytes_downloaded >= self.sampled_byte_size:
                    break

                contents = self._filter_and_download_files(row["files"])
                for content in contents:
                    content_size = len(content["content"].encode("utf-8"))
                    total_bytes_downloaded += content_size
                    progress_bar.update(content_size)

                    if total_bytes_downloaded <= self.sampled_byte_size:
                        all_contents.append(content)

        return all_contents

    def _filter_and_download_files(self, files):
        """ファイルをフィルタリングし、ダウンロードして内容を取得"""
        contents = []
        for file in files:
            if file["language"] in LANG_FILTER and file["license_type"] in LICENSE_TYPE_FILTER:
                content = self._download_content(file["blob_id"], file["src_encoding"])
                contents.append(
                    {
                        "id": f"TS_{file['blob_id']}",
                        "content": content,
                        "detected_licenses": file["detected_licenses"],
                        "license_type": file["license_type"],
                        "language": file["language"],
                    }
                )
        return contents

    def _download_content(self, blob_id, src_encoding):
        """S3よりコンテンツをダウンロード"""
        s3_url = f"s3://softwareheritage/content/{blob_id}"
        s3_client = self._setup_aws_session()
        with open(s3_url, "rb", compression=".gz", transport_params={"client": s3_client}) as fin:
            content = fin.read().decode(src_encoding)
        return content

    def _setup_aws_session(self):
        """AWSセッションとS3クライアントの設定"""
        if not self.s3_client:
            session = boto3.Session(aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
            self.s3_client = session.client("s3")
        return self.s3_client

    def _format_data(self, data):
        """データを共通フォーマットに変換"""
        return [{**COMMON_DATA_THE_STACK_V2, **record} for record in data]
