# code-dataset-builder

## 実行方法

- .env.sample をコピーし、.env と名前を変更し、.env の内容を変更してください。
- 以下でライブラリをインストールし、実行してください。

```bash
poetry install
python src/main.py
```

- 実行結果は result.parquet として直下に保存されます。

## 出力ファイル
- OpenMathInstructは問題と回答が分かれているので、これを統合し一つのカラムとし、質問と回答の間に任意の文字列を入れるようにした。
- 実行結果は以下の形式で出力されます。
- 出力ファイルは、parquet ファイルとなります。
- ID には、衝突を避けるためにデータソースのイニシャルをつけています。
- ID はそれぞれ、The Stack v2 の場合は blob_id、OpenMathInstruct-1-1.8m-ja の場合は index カラムになります。

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
