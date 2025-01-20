#!/bin/bash

# エラーハンドリング
set -e
# set -u  # コメントアウトして実行を試みる

# ROS 2のトレースを無効にするために、環境変数を設定
export AMENT_TRACE_SETUP_FILES=""
export AMENT_PYTHON_EXECUTABLE=$(which python3)
export COLCON_TRACE=""

# ROS 2 Foxyのワークスペースとパッケージ設定
WORKSPACE=~/ros2_ws
SOURCE_SCRIPT=/opt/ros/foxy/setup.bash

# 必要な変数をチェック
if [ ! -d "$WORKSPACE" ]; then
    echo "Error: ワークスペース $WORKSPACE が存在しません。"
    exit 1
fi

# ROS 2 環境のセットアップ
if [ -f "$SOURCE_SCRIPT" ]; then
    source "$SOURCE_SCRIPT"
    echo "ROS 2 環境をセットアップしました。"
else
    echo "Error: ROS 2 のセットアップスクリプトが見つかりません。($SOURCE_SCRIPT)"
    exit 1
fi

# ワークスペースのセットアップ
cd "$WORKSPACE"
if [ -f "install/setup.bash" ]; then
    source install/setup.bash
    echo "ワークスペースの環境をセットアップしました。"
else
    echo "Error: ワークスペースのセットアップスクリプトが見つかりません。ビルドが必要かもしれません。"
    exit 1
fi

# パッケージ名とノード名を実行する
echo "サンプルノードを起動します..."
ros2 run mypkg weather_publisher
echo "テストが完了しました。"

