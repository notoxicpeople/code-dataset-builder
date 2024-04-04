# code-dataset-builder

## 概要

The Stack v2 と OpenMathInstruct-ja を対象として、これらのデータセットをダウンロードした上で、同じフォーマットに整形し、ローカル環境に保存するスクリプトです。

## 実行方法

- .env.sample をコピーし、.env と名前を変更し、.env の内容を変更してください。
  - hugging face および、AWS S3 を使用するので、AWS アクセスキー ID（AWS_ACCESS_KEY_ID）、AWS シークレットキー（AWS_SECRET_ACCESS_KEY）、hugging face トークン（HUGGING_FACE_TOKEN）の設定が必要です。
- 以下でライブラリをインストールし、実行してください。

```bash
poetry install
python src/main.py
```

- 実行結果は result.parquet として直下に保存されます。

## 設定値

config.py 内において、以下の値を修正することで、挙動を変更できます。

- **SEPARATOR_OPEN_MATH_INSTRUCT**
  - OpenMathInstruct の回答と質問を統合する際のセパレータを指定できます。
  - デフォルトでは[SEP]となっています。
- **TOKEN_SIZE_BYTES_THE_STACK_V2**
  - The Stack のみの設定値で、1 トークンあたりのバイト数を指定できます。
  - この値と SAMPLE_SIZE_TOKENS をかけて、ダウンロード対象の容量を計算しています。
  - ダウンロード対象の容量を超えたら、ダウンロードを停止します。
  - デフォルトでは、1 トークンあたり 4 バイトが設定されています。
- **SAMPLE_SIZE_TOKENS_THE_STACK_V2**
  - The Stack のみの設定値で、ダウンロードするトークン量を指定できます。
  - この値と TOKEN_SIZE_BYTES をかけて、ダウンロード対象の容量を計算しています。
  - ダウンロード対象の容量を超えたら、ダウンロードを停止します。
  - デフォルトでは、１０ BT が設定されています。
- **LANG_FILTER_THE_STACK_V2**
  - The Stack のみの設定値で、ダウンロード対象の言語を複数指定できます。
  - C++や Python などを指定すると、指定された言語のみをダウンロードします。
- **LICENSE_TYPE_FILTER_THE_STACK_V2**
  - The Stack のみの設定値で、ダウンロード対象のライセンスを複数指定できます。
  - 値は、"permissive"と"no_license"の 2 種類で、前者はオープンソースで使う上で寛容なライセンスが設定されているコードを表し、後者はライセンスが設定されていないコードを表します。

## 処理概要

### OpenMathInstruct-1-1.8m-ja

1. データセットを hugging face からダウンロードします。
2. \<llm-code>という単語が回答カラムに存在するかどうかが、コードが回答に含まれているかのサインのため、単語が無いコードは処理対象外とします。
3. OpenMathInstruct は問題と回答が分かれているので、問題と回答の間に任意の文字列を入れて統合し、1 つのカラムにします。
4. 規定のフォーマットに整形し、The Stack v2 の結果と統合し、ローカルに保存します。

### The Stack v2

1. データセットの一覧を hugging face からダウンロードします。
2. S3 から 1 の情報を利用して、コード本体をダウンロードします。
3. 言語の種類（Python など）、ライセンスの種類（無記載など）をフィルタリングし、対象のコードのみをダウロードします。
4. 規定のフォーマットに整形し、OpenMathInstruct の結果と統合し、ローカルに保存します。

### 共通

- 実行結果は以下の形式で出力されます。
- 出力ファイルは、parquet ファイルとなります。
- ID には、衝突を避けるためにデータソースのイニシャルをつけています。
  - The Stack v2 は TS,OpenMathInstruct は OM
  - ID はそれぞれ、The Stack v2 の場合は、blob_id、OpenMathInstruct-1-1.8m-ja の場合は、index カラムになります。

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
