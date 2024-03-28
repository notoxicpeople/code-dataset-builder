# config.py
from dotenv import load_dotenv
import os

load_dotenv()

# 環境変数からの設定読み込み
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
HUGGING_FACE_TOKEN = os.getenv("HUGGING_FACE_TOKEN")

# データセット関連の設定
DATASET_NAME_OPEN_MATH_INSTRUCT = "kunishou/OpenMathInstruct-1-1.8m-ja"
DATASET_NAME_THE_STACK_V2 = "bigcode/the-stack-v2-train-smol-ids"
SEPARATOR_OPEN_MATH_INSTRUCT = "[SEP]"  # OpenMathInstructの質問と解答のセパレータ

# 最終的な出力フォーマット
# [
#     {
#         "id": "OM_1",
#         "data_source": "The Stack v2 / OpenMathInstruct-1-1.8m-ja",
#         "language": "Python",
#         "detected_licenses": ["NVIDIA License"],
#         "license_type": "no_license / permissive",
#         "text": "code_sample"
#     }
# ]
COMMON_DATA_OPEN_MATH_INSTRUCT = {"data_source": DATASET_NAME_OPEN_MATH_INSTRUCT, "language": "Python", "detected_licenses": ["NVIDIA License"], "license_type": "permissive"}
COMMON_DATA_THE_STACK_V2 = {"data_source": DATASET_NAME_THE_STACK_V2, "language": "Python"}

# フィルタリングに使用する設定
LANG_FILTER = ["Python"]
LICENSE_TYPE_FILTER = ["permissive", "no_license"]

# その他の設定
TOKEN_SIZE_BYTES = 4  # 1トークンあたりの平均バイト数
SAMPLE_SIZE_TOKENS = 10**9  # 取得するトークンの数（10億トークン）
