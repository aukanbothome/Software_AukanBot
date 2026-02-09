# Robot Decision Making System a

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
