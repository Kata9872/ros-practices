
from launch import LaunchDescription
from launch.actions import (
    DeclareLaunchArgument,
    ExecuteProcess,
)
from launch.conditions import IfCondition
from launch.substitutions import (
    LaunchConfiguration,
    PathJoinSubstitution,
)
from launch_ros.actions import Node


def generate_launch_description():
    namespace = LaunchConfiguration('namespace')
    record = LaunchConfiguration('record')
    bag_dir = LaunchConfiguration('bag_dir')
    reliability = LaunchConfiguration('subscriber_reliability')

    sensor_topic = PathJoinSubstitution([
        '/', namespace, 'sensor_pose'
    ])

    return LaunchDescription([
        DeclareLaunchArgument(
            'namespace',
            default_value='robot_a'
        ),
        DeclareLaunchArgument(
            'record',
            default_value='false'
        ),
        DeclareLaunchArgument(
            'bag_dir',
            default_value='/tmp/pr05_bag'
        ),
        DeclareLaunchArgument(
            'subscriber_reliability',
            default_value='best_effort'
        ),

        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim',
            namespace=namespace,
            output='screen'
        ),

        Node(
            package='patrol',
            executable='patrol',
            namespace=namespace,
            remappings=[
                ('pose', 'turtle1/pose'),
                ('cmd_vel', 'turtle1/cmd_vel'),
            ],
            output='screen'
        ),

        Node(
            package='course_bringup',
            executable='pose_relay',
            namespace=namespace,
            output='screen'
        ),

        Node(
            package='course_bringup',
            executable='sensor_subscriber',
            namespace=namespace,
            parameters=[{
                'reliability': reliability
            }],
            output='screen'
        ),

        ExecuteProcess(
            condition=IfCondition(record),
            cmd=[
                'ros2', 'bag', 'record',
                '-s', 'mcap',
                '-o', bag_dir,
                sensor_topic
            ],
            output='screen'
        )
    ])
  
