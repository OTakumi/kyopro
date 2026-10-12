#!/usr/bin/env python3
import sys

# 再帰上限の引き上げ（DFSや木の探索で必須）
sys.setrecursionlimit(2 * 10**6)

# 高速入力
input = sys.stdin.readline

# 頻出定数
INF = 10**18
MOD = 998244353
# DIRS4 = [(-1, 0), (1, 0), (0, -1), (0, 1)]


# 入力用ショートカット
def ii():
    return int(input())


def mi():
    return map(int, input().split())


def li():
    return list(map(int, input().split()))


def si():
    return input().rstrip()


def solve() -> None:
    # 例:
    # n, m = mi()
    # a = li()
    a, b = mi()

    if a * b % 2 == 0:
        print("Even")
    else:
        print("Odd")


if __name__ == "__main__":
    solve()
