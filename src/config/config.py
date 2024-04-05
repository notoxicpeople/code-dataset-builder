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

# その他の設定
TOKEN_SIZE_BYTES_THE_STACK_V2 = 4  # 1トークンあたりの平均バイト数
SAMPLE_SIZE_TOKENS_THE_STACK_V2 = 10**9  # 取得するトークンの数

# フィルタリングに使用する設定
LANG_FILTER_THE_STACK_V2 = ["Python"]
LICENSE_TYPE_FILTER_THE_STACK_V2 = ["permissive", "no_license"]
DETECTED_LICENSES_FILTER_THE_STACK_V2 = [
    "0BSD",
    "BSD-1-Clause",
    "BSD-2-Clause",
    "BSD-3-Clause",
    "AFL-2.0",
    "Apache-1.1",
    "Apache-2.0",
    "APSL-2.0",
    "Artistic-1.0",
    "Artistic-2.0",
    "AAL",
    "BSL-1.0",
    "BSD-2-Clause-Patent",
    "CDDL-1.0",
    "CPL-1.0",
    "CUA-OPL-1.0",
    "EPL-1.0",
    "EPL-2.0",
    "eCos-2.0",
    "ECL-1.0",
    "EFL-1.0",
    "EFL-2.0",
    "Entessa",
    "EUDatagrid",
    "Fair",
    "Frameworx-1.0",
    "AGPL-3.0",
    "GPL-2.0",
    "GPL-3.0",
    "LGPL-2.1",
    "LGPL-3.0",
    "HPND",
    "IPL-1.0",
    "Intel",
    "IPA",
    "ISC",
    "jabberpl",
    "BSD-3-Clause-LBNL",
    "LPL-1.0",
    "LPL-1.02",
    "MIT",
    "MIT-0",
    "CVW",
    "Motosoto",
    "MPL-1.0",
    "MPL-1.1",
    "MPL-2.0",
    "MulanPSL-2.0",
    "Multics",
    "NASA-1.3",
    "Naumen",
    "NGPL",
    "Nokia",
    "NTP",
    "OCLC-2.0",
    "OGTSL",
    "OSL-2.0",
    "OLDAP-2.8",
    "PHP-3.0",
    "Python-2.0",
    "CNRI-Python",
    "QPL-1.0",
    "RPSL-1.0",
    "RPL-1.1",
    "RSCPL",
    "OFL-1.1",
    "Sleepycat",
    "SISSL",
    "SPL-1.0",
    "Watcom-1.0",
    "NCSA",
    "Unlicense",
    "VSL-1.0",
    "WXwindows",
    "Xnet",
    "ZPL-2.0",
    "Zlib",
]
