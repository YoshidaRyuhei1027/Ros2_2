import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Talker(Node):  # Nodeクラスを継承
    def __init__(self):
        super().__init__("talker")  # ノード名を"talker"に設定
        self.pub = self.create_publisher(Int16, "countup", 10)
        self.create_timer(0.5, self.cb)  # 0.5秒ごとにcbメソッドを呼び出す
        self.n = 0  # カウント用変数

    def cb(self):  # cbメソッドをクラス内に定義
        msg = Int16()
        msg.data = self.n
        self.pub.publish(msg)
        self.get_logger().info(f"Publishing: {msg.data}")
        self.n += 1

def main():
    rclpy.init()
    node = Talker()  # Talkerクラスのオブジェクトを作成
    rclpy.spin(node)  # ノードをスピンさせて実行状態にする
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()

