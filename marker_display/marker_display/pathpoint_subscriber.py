import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point

class DataSubscriber(Node):
    def __init__(self):
        super().__init__('data_subscriber')
        self.subscription = self.create_subscription(
            Float32MultiArray,
            'data_topic',
            self.listener_callback,
            10  # QoS depth
        )
        self.marker_publisher = self.create_publisher(Marker, 'marker_topic', 10)  # Publisher for markers

    def listener_callback(self, msg):
        self.get_logger().info('Received data: %s' % msg.data)
        # Publish marker
        marker = Marker()
        marker.header.frame_id = "map"  # Set the frame in which the marker is to be displayed
        marker.header.stamp = self.get_clock().now().to_msg()
        marker.type = Marker.LINE_STRIP  # Marker type
        marker.action = Marker.ADD
        marker.scale.x = 0.1  # Line width
        marker.color.r = 1.0
        marker.color.g = 0.0
        marker.color.b = 0.0
        marker.color.a = 1.0
        marker.points = []  # List of points for the line strip

        for i in range(0, len(msg.data), 2):
            point = Point()
            point.x = msg.data[i]
            point.y = msg.data[i + 1]
            marker.points.append(point)

        self.marker_publisher.publish(marker)

def main(args=None):
    rclpy.init(args=args)
    data_subscriber = DataSubscriber()
    rclpy.spin(data_subscriber)
    data_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
