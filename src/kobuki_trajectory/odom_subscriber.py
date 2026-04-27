#!/usr/bin/env python3
# Subscriber de odometria — sigue el patron del wiki de ROS

import rospy
import math
import tf
from nav_msgs.msg import Odometry

class OdomSubscriber:
    def __init__(self):
        self.x        = 0.0
        self.y        = 0.0
        self.yaw      = 0.0
        self.received = False

        # Patron ROS wiki: rospy.Subscriber(topico, TipoMensaje, callback)
        rospy.Subscriber('/odom', Odometry, self._callback)

    def _callback(self, msg):
        # Extraer posicion
        self.x = msg.pose.pose.position.x
        self.y = msg.pose.pose.position.y

        # Extraer orientacion (quaternion -> euler)
        q = msg.pose.pose.orientation
        _, _, self.yaw = tf.transformations.euler_from_quaternion(
            [q.x, q.y, q.z, q.w]
        )
        self.received = True

    def wait_for_data(self, rate):
        rospy.loginfo("Esperando datos de odometria...")
        while not self.received and not rospy.is_shutdown():
            rate.sleep()
        rospy.loginfo("Odometria recibida.")
