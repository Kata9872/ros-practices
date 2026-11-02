
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy
from turtlesim.msg import Pose


class SensorSubscriber(Node):
    def __init__(self):
        super().__init__('sensor_subscriber')

        self.declare_parameter('reliability', 'best_effort')

        mode = self.get_parameter('reliability').value

        if mode not in ('reliable', 'best_effort'):
            raise ValueError('Invalid reliability mode')

        reliability = (
            ReliabilityPolicy.RELIABLE
            if mode == 'reliable'
            else ReliabilityPolicy.BEST_EFFORT
        )

        self.subscription = self.create_subscription(
            Pose,
            'sensor_pose',
            self.callback,
            QoSProfile(
                depth=10,
                reliability=reliability
            )
        )

    def callback(self, msg):
        self.get_logger().info(
            f'Pose: x={msg.x:.2f}, y={msg.y:.2f}'
        )


def main(args=None):
    rclpy.init(args=args)
    node = SensorSubscriber()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
  
