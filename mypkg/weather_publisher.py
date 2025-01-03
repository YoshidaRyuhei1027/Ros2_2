import rclpy
from rclpy.node import Node
from person_msgs.msg import Person

class WeatherPublisher(Node):
    def __init__(self):
        super().__init__('weather_publisher')
        self.publisher_ = self.create_publisher(Person, 'weather_data', 10)
        self.create_timer(2.0, self.publish_weather_data)

    def publish_weather_data(self):
        msg = Person()
        msg.name = "Weather Station A"
        msg.temperature = 25.5  # 温度 (例: 25.5°C)
        msg.humidity = 60.0  # 湿度 (例: 60%)
        self.publisher_.publish(msg)
        self.get_logger().info(f"Publishing: Name={msg.name}, Temp={msg.temperature}°C, Humidity={msg.humidity}%")

def main():
    rclpy.init()
    node = WeatherPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

