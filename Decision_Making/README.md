# Robot Decision Making System

### A Finite State Machine–based Architecture for RoboCup Challenges

---

## Overview

This repository documents the **Decision Making System** used by the robot across multiple RoboCup-style challenges.

The decision-making logic is implemented using **Finite State Machines (FSMs)**, where:

- Each challenge has its own state machine  
- States represent robot behaviors  
- Transitions are triggered by events  
- The FSM acts as the logical backbone of the robot  
- All perception and action modules are coordinated through states  

The system is fully implemented in **Python** and integrates multiple subsystems such as navigation, perception, manipulation, and human–robot interaction.

---

## Decision Making Architecture

- Event-driven FSM  
- One FSM per challenge  
- Modular and scalable  
- Robust to errors and unexpected situations  
- Designed for real-world human interaction  

---

## Integrated Subsystems

- Mobility control  
- Path planning  
- Object detection and recognition  
- Pose estimation  
- Speech recognition  
- Text-to-speech (TTS)  
- Arm manipulation  
- Mapping  
- Face recognition  
- Button-based interaction  

---

# RoboCup Challenges

---

## Challenge 1: Help Me Carry

### Description

The robot assists a person by following them, detecting a bag, picking it up, avoiding obstacles, and delivering it to a designated location before returning.

### State Flow Summary

- Waits for a person to approach  
- Signals readiness to follow  
- Follows the person  
- Stops when the person stops  
- Searches for a bag  
- Navigates to the bag  
- Picks up the bag  
- Returns to the starting point  
- Avoids obstacles if detected  
- Delivers the bag  
- Joins a return queue  

### Events (Examples)

- `b` → Person identified  
- `f` → Person starts walking  
- `k` → Bag detected  
- `o` → Obstacle detected  
- `q` → Bag delivered  

### Key Functions Used

- Pose estimation  
- Object detection  
- Speech recognition  
- Path planning  
- Arm control  

---

## Challenge 2: General Purpose Service Robot

### Description

The robot waits for spoken instructions, executes commands, navigates to instruction points, and safely handles obstacles during execution.

### Behavior Summary

- Idle waiting  
- Receives voice commands  
- Executes assigned tasks  
- Reports task completion  
- Handles navigation obstacles  

### Key Events

- `b` → Command given  
- `e` → Instruction point reached  
- `f` → Obstacle detected  
- `g` → Obstacle avoided  

---

## Challenge 3: Receptionist

### Description

The robot acts as a receptionist, greeting guests, asking questions, offering drinks, guiding them to seats, and introducing them to others.

### Behavior Summary

- Detects guest arrival  
- Conducts initial interaction  
- Guides guest to drinks  
- Identifies drink choice  
- Escorts guest to living room  
- Assigns a seat  
- Introduces guests  
- Handles lost guests and obstacles  

### Key Events

- `b` → Guest detected  
- `f` → Drink identified  
- `k` → Guest lost  
- `n` → Obstacle detected  

---

## Challenge 4: Storing Groceries

### Description

The robot organizes groceries by detecting objects on a table, classifying them, transporting them to storage, and performing special actions such as pouring cereal.

### Behavior Summary

- Navigate to table  
- Detect and classify objects  
- Transport items to storage  
- Store items correctly  
- Handle obstacles  
- Finish task and report completion  

---

## Challenge 5: Clean the Table

### Description

The robot cleans a table by identifying, picking up, classifying, and disposing or storing objects while handling errors and obstacles.

### Behavior Summary

- Go to the table  
- Analyze table contents  
- Classify objects  
- Pick and drop objects  
- Verify table status  
- Finish when table is empty  

### Key Events

- `c` → Table reached  
- `f` → Object picked  
- `j` → Table empty  
- `k` → Obstacle detected  

---

## Challenge 6: Enhanced General Purpose Service Robot

### Description

An autonomous service robot that scans the arena, removes trash, organizes misplaced objects, assists people, and executes commands dynamically.

### Behavior Summary

- Continuous arena scanning  
- Trash detection and disposal  
- Object relocation  
- Human assistance  
- Command understanding and execution  
- Obstacle handling  

---

## Challenge 7: Restaurant

### Description

The robot works as a waiter, managing customer interactions, taking orders, delivering food, and requesting human assistance when needed.

### Behavior Summary

- Monitor customer queue  
- Navigate to customer  
- Take and confirm orders  
- Go to kitchen  
- Deliver orders  
- Handle delivery errors and obstacles  

---

## Challenge 8: Give Me a Hand

### Description

The robot assists a human operator by receiving objects, interpreting instructions, confirming actions, navigating to destinations, and returning.

### Behavior Summary

- Navigate to operator  
- Receive object  
- Interpret command  
- Request confirmation if needed  
- Navigate to target  
- Place object  
- Return to operator  
- Handle obstacles and errors  

---

## Implementation Notes

- All FSMs are implemented in Python  
- Each state corresponds to a robot behavior  
- Transitions are strictly event-driven  
- Designed for robustness under real-world uncertainty  
- Easily extendable to new challenges  

---

## Conclusion

This decision-making framework provides a clear, modular, and robust architecture for autonomous robots operating in dynamic environments, ensuring reliable behavior across multiple service-oriented RoboCup challenges.


Este repositorio documenta el sistema de toma de decisiones del robot, diseñado para los distintos desafíos de RoboCup.
El sistema está basado en máquinas de estados finitos (FSM), donde cada reto posee su propia lógica de decisión, eventos y transiciones.

La implementación está desarrollada en Python, integrando múltiples subsistemas del robot como navegación, percepción, manipulación y comunicación humano-robot.

Visión General del Sistema

El Decision Making System es el núcleo lógico del robot y cumple las siguientes funciones:

Coordina el comportamiento del robot mediante estados y eventos

Define cómo el robot reacciona ante el entorno y las personas

Integra todos los módulos del robot:

Control de movilidad

Planeamiento de trayectorias

Detección y reconocimiento de objetos

Estimación de pose

Reconocimiento y síntesis de voz

Control del brazo robótico

Mapeo y reconocimiento facial

Cada desafío se implementa como una máquina de estados independiente, lo que facilita:

Reutilización de lógica

Escalabilidad

Depuración

Claridad del comportamiento del robot

Arquitectura de Decisión

Cada estado (Qn) representa una acción o situación específica del robot.

Los eventos (a, b, c, …) representan estímulos del entorno o resultados de acciones.

Las transiciones entre estados son event-driven.

Cada estado requiere un conjunto específico de funciones del robot.

Desafíos Implementados
Challenge 1: Help Me Carry
Descripción

El robot asiste a una persona transportando una bolsa desde el punto de recogida hasta una zona designada, evitando obstáculos y manteniendo interacción verbal.

Flujo General

Espera a que una persona se acerque

Sigue a la persona

Detecta y recoge la bolsa

Navega evitando obstáculos

Entrega la bolsa y regresa

Estados Principales

Q1 – Esperando persona: El robot permanece atento a la aparición de una persona.

Q2 – Listo para seguir: Indica verbalmente que está preparado.

Q3 – Siguiendo persona: Mantiene seguimiento activo.

Q4 – Esperando indicación: Se detiene y espera instrucciones.

Q5 – Detección de bolsa: Busca la bolsa indicada.

Q6 – Navegación a la bolsa: Se desplaza hacia ella.

Q7 – Recogida de bolsa: Usa el brazo robótico.

Q8 – Retorno a inicio: Regresa con la bolsa.

Q9 – Detección de obstáculos: Recalcula ruta.

Q10 – Entrega de bolsa: Deposita la bolsa.

Q11 – Fila de retorno: Mantiene distancia social.

Eventos Clave

Identificación de persona

Recepción de órdenes

Detección y aseguramiento de bolsa

Obstáculos detectados o evadidos

Entrega completada

Challenge 2: General Purpose Service Robot
Descripción

Robot de servicio general capaz de recibir órdenes, ejecutarlas y reportar su estado.

Flujo General

Espera instrucciones

Recibe y entiende una orden

Ejecuta la tarea

Finaliza y solicita nuevas instrucciones

Estados

Q1 – Inactivo

Q2 – Recepción de comando

Q3 – Ejecución

Q4 – Finalización

Q5 – Navegación a punto

Q6 – Gestión de obstáculos

Challenge 3: Receptionist
Descripción

Robot recepcionista que da la bienvenida a invitados, los guía, ofrece bebidas y los presenta.

Flujo General

Detecta invitado

Realiza preguntas iniciales

Guía a bebidas

Identifica bebida elegida

Guía a la sala

Presenta al invitado

Estados Clave

Detección de invitados

Interacción verbal

Guía autónoma

Manejo de invitados perdidos

Detección y evasión de obstáculos

Challenge 4: Storing Groceries
Descripción

El robot organiza y almacena objetos de supermercado en ubicaciones correctas.

Flujo General

Navega a la mesa

Selecciona objeto

Transporta

Almacena

Vierte cereal si es requerido

Estados

Selección

Transporte

Almacenamiento

Vertido

Finalización

Obstáculos

Challenge 5: Clean the Table
Descripción

El robot limpia una mesa clasificando y retirando objetos hasta dejarla vacía.

Flujo General

Navega a la mesa

Analiza objetos

Clasifica

Recoge

Deposita

Verifica limpieza

Challenge 6: Enhanced General Purpose Service Robot
Descripción

Versión avanzada del robot de servicio general, capaz de limpiar basura, ordenar objetos y ayudar personas.

Capacidades

Detección de basura

Detección de objetos fuera de lugar

Interacción humana avanzada

Ejecución de órdenes complejas

Manejo robusto de obstáculos

Challenge 7: Restaurant
Descripción

Robot camarero que atiende clientes, toma pedidos y los entrega.

Flujo General

Observa la fila

Detecta cliente

Toma pedido

Confirma pedido

Recoge comida

Entrega

Finaliza turno

Challenge 8: Give Me a Hand

Descripción

Robot asistente que recibe objetos del operador y los entrega a un destino indicado.

Flujo General

Navega al operador

Recibe objeto

Interpreta orden

Solicita confirmación

Navega al destino

Coloca objeto

Regresa

Estados Destacados

Interpretación de órdenes

Confirmaciones

Manejo de ambigüedad

Gestión de obstáculos

Reintentos automáticos

Implementación

Lenguaje: Python

Paradigma: Máquinas de Estados Finitos

Transiciones basadas en eventos

Modular y escalable

Compatible con simulación y robot real

Subsistemas Integrados

Mobility Control

Path Planning

Object Detection & Recognition

Pose Estimation

Speech Recognition

Text-to-Speech

Arm Control

Mapping

Face Recognition

Button Interface
