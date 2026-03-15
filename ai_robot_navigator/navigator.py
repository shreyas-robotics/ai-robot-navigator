import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class Navigator(Node):

    def __init__(self):
        super().__init__('navigator')

        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10)

        self.publisher = self.create_publisher(
            Twist,
            '/cmd_vel',
            10)

        self.get_logger().info("AI Robot Navigator started")

    def scan_callback(self, msg):

        twist = Twist()

        if len(msg.ranges) == 0:
            return

        min_distance = min(msg.ranges)

        if min_distance < 0.5:
            self.get_logger().info("Obstacle detected → STOP")
            twist.linear.x = 0.0
            twist.angular.z = 0.5
        else:
            self.get_logger().info("Path clear → MOVE FORWARD")
            twist.linear.x = 0.2
            twist.angular.z = 0.0

        self.publisher.publish(twist)


def main(args=None):
    rclpy.init(args=args)

    navigator = Navigator()

    rclpy.spin(navigator)

    navigator.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
