#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from person_msgs.msg import Person
from person_msgs.msg import Analysis

class WeatherAnalyzer(Node):
    def __init__(self):
        super().__init__('weather_analyzer')
        self.get_logger().info("WeatherAnalyzer node has been started.")
        
        
        self.sub = self.create_subscription(Person, 'weather_data', self.analyze_weather_data, 10)
        
        
        self.pub = self.create_publisher(Analysis, 'weather_analysis', 10)

    def analyze_weather_data(self, msg):
        
        self.get_logger().info(f"Received: Station={msg.name}, Temperature={msg.temperature}°C, Humidity={msg.humidity}%")
        
        
        analysis = Analysis()
        analysis.station = msg.name
        analysis.average_temperature = msg.temperature
        analysis.is_high_temperature = msg.temperature > 30.0
        analysis.is_low_humidity = msg.humidity < 20.0

        
        if analysis.is_high_temperature:
            self.get_logger().warn(f"High Temperature Alert at {msg.name}! Temp={msg.temperature}°C")
        if analysis.is_low_humidity:
            self.get_logger().warn(f"Low Humidity Alert at {msg.name}! Humidity={msg.humidity}%")
        
        
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

