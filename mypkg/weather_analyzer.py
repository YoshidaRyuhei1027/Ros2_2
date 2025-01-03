#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from person_msgs.msg import Person  # Personメッセージ型を利用

class WeatherAnalyzer(Node):
    def __init__(self):
        super().__init__('weather_analyzer')
        self.get_logger().info("WeatherAnalyzer node has been started and subscribed to 'weather_data' topic.")
        self.sub = self.create_subscription(Person, 'weather_data', self.analyze_weather_data, 10)

    def analyze_weather_data(self, msg):
        # 受信データをログに出力
        self.get_logger().info(f"Received: Station={msg.name}, Temperature={msg.temperature}°C, Humidity={msg.humidity}%")
        
        # 温度が30°Cを超える場合の警告
        if msg.temperature > 30.0:
            self.get_logger().warn(f"High Temperature Alert at {msg.name}! Temp={msg.temperature}°C")
        
        # 湿度が20%未満の場合の警告
        if msg.humidity < 20.0:
            self.get_logger().warn(f"Low Humidity Alert at {msg.name}! Humidity={msg.humidity}%")

def main():
    rclpy.init()
    node = WeatherAnalyzer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()

