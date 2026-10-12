#!/usr/bin/env python3
import sys

# 再帰上限の引き上げ（DFSや木の探索で必須）
sys.setrecursionlimit(2 * 10**6)

input = sys.stdin.readline

INF = 10**18
{% if mod %}
MOD = {{ mod }}
{% else %}
MOD = 998244353
{% endif %}
{% if yes_str %}
YES = "{{ yes_str }}"
{% endif %}
{% if no_str %}
NO = "{{ no_str }}"
{% endif %}
# DIRS4 = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def ii():
    return int(input())


def mi():
    return map(int, input().split())


def li():
    return list(map(int, input().split()))


def si():
    return input().rstrip()


def solve() -> None:
    pass


if __name__ == "__main__":
    solve()
