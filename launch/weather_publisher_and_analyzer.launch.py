from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='mypkg',
            executable='weather_publisher',
            name='weather_publisher',
            output='screen'
        ),
        Node(
            package='mypkg',
            executable='weather_analyzer',
            name='weather_analyzer',
            output='screen'
        ),
    ])

