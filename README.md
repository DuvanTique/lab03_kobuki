# Laboratorio No. 03 - Fundamentos de Robótica Móvil
**Universidad Nacional de Colombia**  
Curso: Robótica Móvil 2026-I

## Descripción
Este repositorio contiene el desarrollo del Laboratorio No. 03,
enfocado en el uso del robot Kobuki mediante ROS Noetic.

## Integrantes
- Nombre 1
- Nombre 2
- Nombre 3
- Nombre 4

## Estructura del repositorio
kobuki_trajectory/
├── scripts/
│   └── trajectory_node.py       # Nodo principal
└── src/
└── kobuki_trajectory/
├── odom_subscriber.py   # Subscriber de /odom
├── velocity_publisher.py # Publisher de velocidad
└── trajectory_controller.py # Lógica de control
## Requisitos
- Ubuntu 20.04
- ROS Noetic
- Robot Kobuki

## Instrucciones de uso
```bash
cd ~/Kobuki_ws
catkin_make
source devel/setup.bash
roslaunch kobuki_node minimal.launch --screen
rosrun kobuki_trajectory trajectory_node.py _largo:=1.0 _ancho:=0.5
```

## Actividad 1 - Tópicos explorados
| Tópico | Tipo | Descripción |
|--------|------|-------------|
| /mobile_base/commands/velocity | geometry_msgs/Twist | Control de velocidad |
| /odom | nav_msgs/Odometry | Odometría del robot |
| /mobile_base/events/cliff | kobuki_msgs/CliffEvent | Sensores de desnivel |
| /mobile_base/events/bumper | kobuki_msgs/BumperEvent | Sensores de choque |

## Respuestas preguntas de análisis
**¿Qué sensores usa el Kobuki para la odometría?**  
Encoders en las ruedas de tracción...

**¿Por qué la odometría presenta errores en línea recta?**  
Por deslizamiento de ruedas, diferencias en el diámetro...

**¿Función de los sensores cliff?**  
Detectan bordes usando sensores IR hacia abajo...

