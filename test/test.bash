#!/bin/bash
# SPDX-FileCopyrightText: 2024 Ryusei Fujimura
# SPDX-License-Identifier: BSD-3-Clause

ng () {
	echo ${1}行目が違うよ
	res=1
}

res=0

dir=~  # デフォルトの作業ディレクトリ
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build || exit 1  # ビルドエラーで終了
source $dir/.bashrc

# ノードの起動とログ取得
timeout 20 ros2 launch mypkg weather_publisher_and_analyzer.launch.py > /tmp/mypkg.log

# ログ確認
grep "Publishing: Name=" /tmp/mypkg.log || ng ${LINENO}
grep "Received: Station=" /tmp/mypkg.log || ng ${LINENO}

# デバッグ用
cat /tmp/mypkg.log

[ "$res" = 0 ] && echo OK || echo テスト失敗
exit "$res"

