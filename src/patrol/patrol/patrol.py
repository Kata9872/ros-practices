
import rclpy
from rclpy.node import Node
from rcl_interfaces.msg import SetParametersResult
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

from .validation import is_valid


class Patrol(Node):
    def __init__(self):
        super().__init__('patrol')

        self.declare_parameter('linear_speed', 0.5)
        self.declare_parameter('turn_rate', 0.3)
        self.declare_parameter('publish_hz', 10.0)

        self.linear_speed = 0.5
        self.turn_rate = 0.3
        self.publish_hz = 10.0

        self.publisher = self.create_publisher(
            Twist, 'cmd_vel', 10
        )

        self.subscription = self.create_subscription(
            Pose, 'pose', self.pose_callback, 10
        )

        self.pose = None

        self.timer = self.create_timer(
            1.0 / self.publish_hz, self.timer_callback
        )

        self.add_on_set_parameters_callback(
            self.parameters_callback
        )

    def pose_callback(self, msg):
        self.pose = msg

    def timer_callback(self):
        if self.pose is None:
            return

        msg = Twist()
        msg.linear.x = self.linear_speed
        msg.angular.z = self.turn_rate
        self.publisher.publish(msg)

    def parameters_callback(self, params):
        for param in params:
            if param.name in (
                'linear_speed', 'turn_rate', 'publish_hz'
            ):
                if not is_valid(param.name, param.value):
                    return SetParametersResult(
                        successful=False,
                        reason='Invalid parameter value'
                    )

        for param in params:
            if param.name == 'linear_speed':
                self.linear_speed = param.value

            elif param.name == 'turn_rate':
                self.turn_rate = param.value

            elif param.name == 'publish_hz':
                if param.value != self.publish_hz:
                    self.destroy_timer(self.timer)
                    self.publish_hz = param.value
                    self.timer = self.create_timer(
                        1.0 / self.publish_hz,
                        self.timer_callback
                    )

        return SetParametersResult(successful=True)


def main(args=None):
    rclpy.init(args=args)
    node = Patrol()

    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
