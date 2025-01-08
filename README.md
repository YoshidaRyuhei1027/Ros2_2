# Weather-Analyzer

## 概要
**Weather Analyzer** は、ROS 2 を利用して気象データを配信・解析するためのパッケージです。

### 機能
- **Publisherノード**: 天気情報（例：気温、湿度、気圧など）をトピックに配信
- **Subscriberノード**: データを解析し、以下を実施
  - 平均気温の計算
  - 異常値の検出（設定範囲外の温度に対するアラート表示）

---

## ノード一覧

### 1. **weather_publisher**
- **機能**:
  - ランダムに生成された気象データ、または外部API（例：OpenWeatherMap）から取得したデータを `weather_data` トピックに配信
- **送信データ形式**:
  - 気温（°C）
  - 湿度（%）
  - 気圧（hPa）

### 2. **weather_analyzer**
- **機能**:
  - `weather_data` トピックからデータをサブスクライブし、以下の解析を実行
    - 平均気温のリアルタイム計算
    - 設定された閾値を超える異常値の検出と警告表示

---

## 使用準備

### 環境セットアップ手順
1. **リポジトリのクローン**  ```git clone https://github.com/YoshidaRyuhei1027/Ros2_2.git```
2. **パッケージのビルド**
   ```colcon build```
3. **ビルド後の環境を適用**
   ```source /opt/ros/foxy/setup.bash```
   ```source ~/ros2_ws/install/setup.bash```

### 動作環境 ###
- 必要なソフトウェア:
  -Python 3.6以上
  -ROS 2 Foxy Fitzroy
- テスト環境
  - OS: Ubuntu 20.04 LTS
  - コンテナ: OSRF 提供の ROS 2 Foxy 対応コンテナ

---

## ライセンス ##
- 本ソフトウェアパッケージは、3条項BSDライセンスの下で再頒布および使用が許可されています。
- 一部のコードは、以下のスライドの内容を参考に作成されています（CC-BY-SA 4.0 by Ryuichi Ueda）: ryuichiueda/slides_marp/robosys2024
- © 2024 Ryuhei Yoshida

---

## 備考 ##
mypkg 内の talker.py と listener.py は学習用に作成されたもので、作成者が振り返りのために残しています。




