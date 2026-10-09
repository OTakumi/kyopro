# デフォルト: main.py のテスト
test file="main.py":
    oj test -c "uv run {{file}}"

# 手動実行
run file="main.py":
    uv run {{file}}

# サンプルダウンロード（例: just dl abc300 a）
dl contest task:
    oj download https://atcoder.jp/contests/{{contest}}/tasks/{{contest}}_{{task}}

# 提出
submit file="main.py":
    oj submit {{file}} --yes
