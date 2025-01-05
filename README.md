# Weather Analyzer
## 概要
Weather Analyzerは、ROS 2を活用して気象データを配信・解析するためのパッケージです。

Publisherノード: 天気情報（例：気温、湿度、気圧など）をトピックにパブリッシュします。
Subscriberノード: 配信されたデータをサブスクライブし、以下のような解析を行います：
平均気温の計算
異常値の検出（例：温度が設定範囲外になった場合のアラート）

## ノード一覧
1. weather_publisher
機能:
ランダム生成された気象データ、または外部API（例：OpenWeatherMap）から取得したデータを weather_data トピックに配信。
送信するデータは以下の形式です：
気温（°C）
湿度（%）
気圧（hPa）
2. weather_analyzer
機能:
weather_data より、以下の解析を実行：
平均気温をリアルタイムで計算
設定された閾値を超える異常値の検出と警告表示

## 使用準備
以下の手順で環境をセットアップしてください。

1.各自のワーキングディレクトリに移動し、リポジトリをクローン
- ```git clone https://github.com/YoshidaRyuhei1027/Ros2_2.git```
2.パッケージをビルド
- ```colcon build```
3.ビルド後の環境を適用
- ```source ~/.bashrc```


## 動作環境
必要なソフトウェア
- Python 3.7以上
- ROS 2 Humble Hawksbill
- テスト環境
- OS: Ubuntu 22.04.2 LTS
- コンテナ: 上田教授提供のROS 2 Humble対応コンテナ

## ライセンス
- このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます．
- このパッケージのコードの一部は、下記のスライド(CC-BY-SA 4.0 by Ryuichi Ueda)のものを、本人の許可を得て自身の著作としたものです。
   ryuichiueda/slides_marp/robosys2024
- © 2024 Ryuhei Yoshida
