#!/usr/bin/env bash
set -e

# 要按顺序..?
# 这是把所有的都换了, 如果只修改了部分, 只执行相关的就行
pip install -e archinfo
pip install -e pyvex
pip install -e cle
pip install -e claripy
pip install -e ailment
pip install -e angr[angrdb]
# pip install -e angr-management  # 这个会导致安装 qt 之类的, 可以不要



