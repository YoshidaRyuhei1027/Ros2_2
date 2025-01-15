#!/bin/bash
# SPDX-FileCopyrightText: 2025 Your Name
# SPDX-License-Identifier: BSD-3-Clause

# テスト結果を保持する変数
result=0

# テスト失敗時の出力関数
fail_test() {
    echo "Test failed at line $1: $2"
    result=1
}

# ROS 2 環境のセットアップ
source /opt/ros/foxy/setup.bash
source ~/ros2_ws/install/setup.bash

# 作業ディレクトリを設定
cd ~/ros2_ws

# ビルドの実行
colcon build || { echo "Build failed"; exit 1; }

# ログファイルのパス
LOG_FILE="/tmp/mypkg_test.log"

# ログファイルをクリア
> "$LOG_FILE"

# Launch ファイルを実行（タイムアウト付きで30秒間）
timeout 30s ros2 launch mypkg weather_publisher_and_analyzer.launch.py > "$LOG_FILE" 2>&1
if [ $? -ne 0 ]; then
    echo "Launch failed"
    fail_test $LINENO "Launch file execution failed"
fi

# ログファイルの存在確認
if [ ! -f "$LOG_FILE" ]; then
    echo "Log file does not exist: $LOG_FILE"
    fail_test $LINENO "Log file not generated"
fi

# ログファイルの確認
grep -q "Publishing: Name=" "$LOG_FILE" || fail_test $LINENO "'Publishing: Name=' not found in log"
grep -q "Received: Station=" "$LOG_FILE" || fail_test $LINENO "'Received: Station=' not found in log"
grep -q "Published analysis for station" "$LOG_FILE" || fail_test $LINENO "'Published analysis for station' not found in log"

# ログを表示（デバッグ用）
echo "===== Test Log ====="
cat "$LOG_FILE"
echo "===================="

# 一時ファイルを削除
rm -f "$LOG_FILE"

# テスト結果の出力
if [ $result -eq 0 ]; then
    echo "All tests passed."
else
    echo "One or more tests failed."
fi

exit $result


