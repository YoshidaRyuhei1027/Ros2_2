# Ros2_2
Weather Analyzer
概要
Weather Analyzerは、ROS 2を活用して気象データを配信・解析するためのパッケージです。

Publisherノード: 天気情報（例：気温、湿度、気圧など）をトピックにパブリッシュします。
Subscriberノード: 配信されたデータをサブスクライブし、以下のような解析を行います：
平均気温の計算
異常値の検出（例：温度が設定範囲外になった場合のアラート）
グラフの生成（データを可視化）
ノード一覧
1. weather_publisher
機能:
ランダム生成された気象データ、または外部API（例：OpenWeatherMap）から取得したデータを weather_data トピックに配信。
送信するデータは以下の形式です：
気温（°C）
湿度（%）
気圧（hPa）
2. weather_analyzer
機能:
weather_data トピックを購読し、以下の解析を実行：
平均気温をリアルタイムで計算。
設定された閾値を超える異常値の検出と警告表示。
Matplotlibを使用したグラフの生成（例：気温推移の可視化）。
使用準備
以下の手順で環境をセットアップしてください。

必要なソフトウェアのインストール
ターミナルで以下を実行：

bash
コードをコピーする
sudo apt install python3-pip
pip install matplotlib
sudo apt-get install git  # Git未インストールの場合のみ
リポジトリのクローン
ワーキングディレクトリに移動し、以下を実行：

bash
コードをコピーする
git clone https://github.com/ユーザー名/リポジトリ名.git
cd リポジトリ名
パッケージのビルド
以下を実行：

bash
コードをコピーする
colcon build
環境設定の反映
ビルド後に以下を実行：

bash
コードをコピーする
source install/setup.bash
使用方法
以下のコマンドでノードを起動します。

Publisherノードの起動
気象データを配信する weather_publisher を起動：

bash
コードをコピーする
ros2 run mypkg weather_publisher
Subscriberノードの起動
データを解析・表示する weather_analyzer を起動：

bash
コードをコピーする
ros2 run mypkg weather_analyzer
動作環境
必要なソフトウェア
Python 3.7以上
ROS 2 Humble Hawksbill
テスト環境
OS: Ubuntu 22.04.2 LTS
コンテナ: 上田教授提供のROS 2 Humble対応コンテナ
ライセンス
このソフトウェアパッケージは、3条項BSDライセンスの下で提供されます。

本パッケージの一部のコードは、以下を参考に作成されました：

Ryuichi Ueda氏のスライド「robosys2024」（CC-BY-SA 4.0）
© 2025 あなたの名前
