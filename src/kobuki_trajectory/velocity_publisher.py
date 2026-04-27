#!/usr/bin/env python3
# Publisher de velocidad — sigue el patron del wiki de ROS

import rospy
from geometry_msgs.msg import Twist

class VelocityPublisher:
    def __init__(self):
        # Patron ROS wiki: rospy.Publisher(topico, TipoMensaje, queue_size=10)
        self._pub = rospy.Publisher(
            '/mobile_base/commands/velocity',
            Twist,
            queue_size=10
        )

    def move(self, linear_x=0.0, angular_z=0.0):
        msg = Twist()
        msg.linear.x  = linear_x
        msg.angular.z = angular_z
        self._pub.publish(msg)

    def stop(self):
        self.move(0.0, 0.0)

