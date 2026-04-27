#!/usr/bin/env python3
# Controlador de trayectoria — logica de movimiento basada en odometria

import rospy
import math

class TrajectoryController:
    def __init__(self, odom_sub, vel_pub, largo, ancho):
        self.odom  = odom_sub
        self.vel   = vel_pub
        self.largo = largo
        self.ancho = ancho

        self.linear_speed  = 0.15  # m/s
        self.angular_speed = 0.4   # rad/s

        # Patron ROS wiki: rospy.Rate(hz) y rate.sleep()
        self.rate = rospy.Rate(10)

    def move_straight(self, distance):
        rospy.loginfo("Avanzando %.2f m" % distance)
        x0 = self.odom.x
        y0 = self.odom.y

        while not rospy.is_shutdown():
            traveled = math.sqrt(
                (self.odom.x - x0)**2 + (self.odom.y - y0)**2
            )
            if traveled >= distance:
                break
            self.vel.move(linear_x=self.linear_speed)
            self.rate.sleep()

        self.vel.stop()
        rospy.sleep(0.5)

    def rotate(self, angle_deg):
        rospy.loginfo("Girando %d grados" % angle_deg)
        angle_rad = math.radians(angle_deg)
        direction = 1.0 if angle_rad > 0 else -1.0

        rotated  = 0.0
        prev_yaw = self.odom.yaw

        while not rospy.is_shutdown():
            delta    = self.odom.yaw - prev_yaw
            delta    = (delta + math.pi) % (2 * math.pi) - math.pi
            rotated += abs(delta)
            prev_yaw = self.odom.yaw

            if rotated >= abs(angle_rad):
                break
            self.vel.move(angular_z=direction * self.angular_speed)
            self.rate.sleep()

        self.vel.stop()
        rospy.sleep(0.5)

    def run_rectangle(self):
        sides = [self.largo, self.ancho, self.largo, self.ancho]
        for i, side in enumerate(sides):
            rospy.loginfo("--- Lado %d/4: %.2f m ---" % (i + 1, side))
            self.move_straight(side)
            if i < len(sides) - 1:
                self.rotate(90)
        rospy.loginfo("Trayectoria completada!")
        self.vel.stop()

