# Weather-Analyzer

[![ROS 2 Test](https://github.com/YoshidaRyuhei1027/Weather-Analyzer/actions/workflows/test.yml/badge.svg)](https://github.com/YoshidaRyuhei1027/Weather-Analyzer/actions/workflows/test.yml)

## 概要
**Weather Analyzer** は、ROS 2 を利用して気象データを配信・解析するためのパッケージです。
weather_analyzer.py の中で、self.pub.publish(analysis) を通じて解析結果を weather_analysis トピックにパブリッシュしています。この処理により、解析結果が他のノードでも利用可能になっています。

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
 
### 使用例 ###
ステップ1:Weather Publisher ノードを起動
1つ目のターミナルで、天気データをパブリッシュする weather_publisher.py を起動します。
``` ros2 run mypkg weather_publisher ```
以下のようなログが表示されます:
```
[INFO] [1234567890.123456]: Publishing: Name=Weather Station A, Temp=25.5°C, Humidity=60.0%
[INFO] [1234567892.123456]: Publishing: Name=Weather Station A, Temp=25.5°C, Humidity=60.0%
```
ステップ2: Weather Analyzer ノードを起動
2つ目のターミナルで、受信した天気データを解析し、解析結果をパブリッシュする weather_analyzer.py を起動します。
``` ros2 run mypkg weather_analyzer ```
以下のようなログが表示されます:
```
[INFO] [1234567890.456789]: Received: Station=Weather Station A, Temperature=25.5°C, Humidity=60.0%
[INFO] [1234567890.456890]: Published analysis for station Weather Station A.
```
高温や低湿度の警報が発生した場合は、以下のような警告も表示されます:
```
[WARN] [1234567890.789123]: High Temperature Alert at Weather Station A! Temp=35.0°C
[WARN] [1234567890.789456]: Low Humidity Alert at Weather Station A! Humidity=15.0%
```
ステップ 3: 解析結果を確認
3つ目のターミナルで、解析結果を確認します。以下のコマンドを実行してください:
```
ros2 topic echo /weather_analysis
```
出力例:
```
station: Weather Station A
average_temperature: 25.5
is_high_temperature: false
is_low_humidity: false
```
警報がある場合:
```
station: Weather Station A
average_temperature: 35.0
is_high_temperature: true
is_low_humidity: false
```

---

## ライセンス ##
- 本ソフトウェアパッケージは、3条項BSDライセンスの下で再頒布および使用が許可されています。
- 一部のコードは、以下のスライドの内容を参考に作成されています（CC-BY-SA 4.0 by Ryuichi Ueda）:
  - [ryuichiueda/slides_marp/robosys2024](https://github.com/ryuichiueda/slides_marp/tree/master/robosys2024)
- © 2024 Ryuhei Yoshida

---

## 備考 ##
mypkg 内の talker.py と listener.py は学習用に作成されたもので、作成者が振り返りのために残しています。




