#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from person_msgs.msg import Person  # 入力メッセージ型
from person_msgs.msg import Analysis  # 出力メッセージ型（新規作成）

class WeatherAnalyzer(Node):
    def __init__(self):
        super().__init__('weather_analyzer')
        self.get_logger().info("WeatherAnalyzer node has been started.")
        
        # Subscriber: 'weather_data' トピックからデータを受信
        self.sub = self.create_subscription(Person, 'weather_data', self.analyze_weather_data, 10)
        
        # Publisher: 'weather_analysis' トピックに解析結果をパブリッシュ
        self.pub = self.create_publisher(Analysis, 'weather_analysis', 10)

    def analyze_weather_data(self, msg):
        # 受信データのログ出力（デバッグ用）
        self.get_logger().info(f"Received: Station={msg.name}, Temperature={msg.temperature}°C, Humidity={msg.humidity}%")
        
        # 解析処理
        analysis = Analysis()
        analysis.station = msg.name
        analysis.average_temperature = msg.temperature  # 現時点ではそのまま利用（例: 温度平均値計算可）
        analysis.is_high_temperature = msg.temperature > 30.0
        analysis.is_low_humidity = msg.humidity < 20.0

        # 解析結果をログに出力（デバッグ用）
        if analysis.is_high_temperature:
            self.get_logger().warn(f"High Temperature Alert at {msg.name}! Temp={msg.temperature}°C")
        if analysis.is_low_humidity:
            self.get_logger().warn(f"Low Humidity Alert at {msg.name}! Humidity={msg.humidity}%")
        
        # 解析結果を新しいトピックにパブリッシュ
        self.pub.publish(analysis)
        self.get_logger().info(f"Published analysis for station {msg.name}.")

def main():
    rclpy.init()
    node = WeatherAnalyzer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()

