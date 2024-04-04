# code-dataset-builder
## 概要
The Stack v2とOpenMathInstruct-jaを対象として、これらのデータセットをダウンロードした上で、同じフォーマットに整形し、ローカル環境に保存するスクリプトです。

## 実行方法
- .env.sample をコピーし、.env と名前を変更し、.envの内容を変更してください。
- 以下でライブラリをインストールし、実行してください。

```bash
poetry install
python src/main.py
```

- 実行結果は result.parquet として直下に保存されます。
  
## 設定値
config.py内において、以下の値を修正することで、挙動を変更できます。
- __SEPARATOR_OPEN_MATH_INSTRUCT__
  - OpenMathInstructの回答と質問を統合する際のセパレータを指定できます。
  - デフォルトでは[SEP]となっています。
- __TOKEN_SIZE_BYTES__
  - The Stackのみの設定値で、1トークンあたりのバイト数を指定できます。
  - この値とSAMPLE_SIZE_TOKENSをかけて、ダウンロード対象の容量を計算しています。
  - ダウンロード対象の容量を超えたら、ダウンロードを停止します。
- __SAMPLE_SIZE_TOKENS__
  - The Stackのみの設定値で、ダウンロードするトークン量を指定できます。
  - この値とTOKEN_SIZE_BYTESをかけて、ダウンロード対象の容量を計算しています。
  - ダウンロード対象の容量を超えたら、ダウンロードを停止します。
- __LANG_FILTER__
  - The Stackのみの設定値で、ダウンロード対象の言語を複数指定できます。
  - C++やPythonなどを指定すると、指定された言語のみをダウンロードします。
- __LICENSE_TYPE_FILTER__
  - The Stackのみの設定値で、ダウンロード対象のライセンスを複数指定できます。
  - 値は、"permissive"と"no_license"の2種類で、前者はオープンソースで使う上で寛容なライセンスが設定されているコードを表し、後者はライセンスが設定されていないコードを表します。

## 処理概要
### OpenMathInstruct-1-1.8m-ja
1. データセットをhugging faceからダウンロードします。
2. \<llm-code>という単語が回答カラムに存在するかどうかが、コードが回答に含まれているかのサインのため、単語が無いコードは処理対象外とします。
3. OpenMathInstructは問題と回答が分かれているので、問題と回答の間に任意の文字列を入れて統合し、1つのカラムにします。
4. 規定のフォーマットに整形し、The Stack v2の結果と統合し、ローカルに保存します。

### The Stack v2
1. データセットの一覧をhugging faceからダウンロードします。
2. S3から1の情報を利用して、コード本体をダウンロードします。
3. 言語の種類（Pythonなど）、ライセンスの種類（無記載など）をフィルタリングし、対象のコードのみをダウロードします。
4. 規定のフォーマットに整形し、OpenMathInstructの結果と統合し、ローカルに保存します。

### 共通
- 実行結果は以下の形式で出力されます。
- 出力ファイルは、parquet ファイルとなります。
- ID には、衝突を避けるためにデータソースのイニシャルをつけています。
  - The Stack v2はTS,OpenMathInstructはOM
  - ID はそれぞれ、The Stack v2の場合は、blob_id、OpenMathInstruct-1-1.8m-jaの場合は、indexカラムになります。

```json
[
  {
    "id": "OM_1",
    "data_source": "The Stack v2 / OpenMathInstruct-1-1.8m-ja",
    "language": "Python",
    "detected_licenses": ["NVIDIA License"],
    "license_type": "no_license / permissive",
    "text": "code_sample"
  }
]
```
