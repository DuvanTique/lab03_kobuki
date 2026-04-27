#!/usr/bin/env python3
"""
Nodo principal del paquete kobuki_trajectory.
Orquesta el subscriber, publisher y controller.

Uso:
  rosrun kobuki_trajectory trajectory_node.py _largo:=1.0 _ancho:=0.5
"""

import rospy

from kobuki_trajectory.odom_subscriber       import OdomSubscriber
from kobuki_trajectory.velocity_publisher    import VelocityPublisher
from kobuki_trajectory.trajectory_controller import TrajectoryController

def main():
    # Patron ROS wiki: rospy.init_node al inicio del nodo principal
    rospy.init_node('kobuki_trajectory', anonymous=True)

    # Leer parametros pasados con _param:=valor
    largo = rospy.get_param('~largo', 1.0)
    ancho = rospy.get_param('~ancho', 0.5)

    rospy.loginfo("Figura: %.2f m x %.2f m" % (largo, ancho))

    rate = rospy.Rate(10)

    # Instanciar modulos (subscriber y publisher)
    odom = OdomSubscriber()
    vel  = VelocityPublisher()

    # Esperar que lleguen datos antes de continuar
    odom.wait_for_data(rate)

    # Esperar confirmacion del usuario
    input("\n>>> Presiona ENTER para iniciar la trayectoria...\n")

    # Ejecutar la trayectoria
    ctrl = TrajectoryController(odom, vel, largo, ancho)
    ctrl.run_rectangle()

    # Patron ROS wiki: rospy.spin() mantiene el nodo vivo
    # (aqui no es estrictamente necesario porque el nodo
    # termina al acabar la trayectoria, pero se incluye
    # para seguir el patron estandar)
    # rospy.spin()

# Patron ROS wiki: try/except ROSInterruptException
if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
