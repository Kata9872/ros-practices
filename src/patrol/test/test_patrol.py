
from unittest.mock import MagicMock

import pytest
import rclpy
from turtlesim.msg import Pose

from patrol.patrol import Patrol


@pytest.fixture
def node():
    rclpy.init()
    patrol = Patrol()
    yield patrol
    patrol.destroy_node()
    rclpy.shutdown()


def test_without_pose(node):
    node.publisher.publish = MagicMock()

    node.timer_callback()

    msg = node.publisher.publish.call_args.args[0]
    assert msg.linear.x == 0.0
    assert msg.angular.z == 0.0


def test_with_pose(node):
    node.publisher.publish = MagicMock()

    node.pose_callback(Pose(x=5.0, y=5.0))
    node.timer_callback()

    msg = node.publisher.publish.call_args.args[0]
    assert msg.linear.x == pytest.approx(0.5)
    assert msg.angular.z == pytest.approx(0.3)
