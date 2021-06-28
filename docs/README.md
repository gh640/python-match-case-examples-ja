# Python `match` `case` サンプル集

(Japanese) Python 3.10 で導入された `match` `case` 構文のサンプル集です。

## 必須

- Docker
- Docker Compose

## 使い方

リポジトリをチェックアウトします。

ビルドします。

```bash
cd python-match-case-examples-ja/
docker-compose build
```

Pytest でサンプルを実行します。

```bash
docker-compose run --rm python
```

## テストケース

| ケース | 関数 |
| --- | --- |
| リテラルパターン | `test_literal_pattern()` |
| or `|` パターン | `test_literal_with_or_pattern()` |
| キャプチャパターン | `test_capture_pattern()` |
| ワイルドカード `_` パターン | `test_wildcard_pattern()` |
| バリューパターン 1 | `test_value_pattern_1_attrs()` |
| バリューパターン 2 | `test_value_pattern_2_enum()` |
| グループパターン | `test_group_pattern()` |
| シーケンスパターン 1 | `test_sequence_pattern_1_list_like_syntax()` |
| シーケンスパターン 2 | `test_sequence_pattern_2_tuple_like_syntax()` |
| マッピングパターン | `test_mapping_pattern()` |
| `if` ガード | `test_if_guard()` |
| クラスパターン 1 | `test_class_pattern_1_positional_args()` |
| クラスパターン 2 | `test_class_pattern_2_match_args()` |
| クラスパターン 3 | `test_class_pattern_3_with_if_guard()` |
| `as` パターン | `test_as_pattern()` |

## 参考

- PEP 634 (dev): https://www.python.org/dev/peps/pep-0634/
