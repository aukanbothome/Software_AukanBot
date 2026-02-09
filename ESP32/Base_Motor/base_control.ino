// base_control.ino
// ESP32 BASE controller: receives commands via UART2 and controls two DC motors

#include <HardwareSerial.h>

HardwareSerial SerialUART(2);   // UART2 (RX=16, TX=17 by default)

// MOTOR DRIVER PINS  (ADJUST TO YOUR WIRING)
const int MOTOR_L1 = 5;   // Front left motor PWM
const int MOTOR_L2 = 18;  // Rear left motor PWM (optional)
const int MOTOR_R1 = 19;  // Front right motor PWM
const int MOTOR_R2 = 21;  // Rear right motor PWM (optional)

// ESP32 PWM CHANNELS
const int CH_L = 0;
const int CH_R = 1;

String buffer = "";

// ======================= MOTOR FUNCTIONS =======================

void stopBase() {
  ledcWrite(CH_L, 0);
  ledcWrite(CH_R, 0);
  digitalWrite(MOTOR_L2, LOW);
  digitalWrite(MOTOR_R2, LOW);
  Serial.println("OK:STOP_BASE");
}

void baseExplorar() {
  // Slow forward motion
  ledcWrite(CH_L, 120);
  ledcWrite(CH_R, 120);
  digitalWrite(MOTOR_L2, LOW);
  digitalWrite(MOTOR_R2, LOW);
  Serial.println("OK:BASE_EXPLORAR");
}

void baseVel(float v, float w) {
  // v = linear velocity (approx. m/s)
  // w = angular velocity (approx. rad/s)
  // Simple PWM mapping: to be tuned for the real robot

  int base_pwm = 150;                    // base PWM 
  int left  = base_pwm + (int)(v*100) - (int)(w*80);
  int right = base_pwm + (int)(v*100) + (int)(w*80);

  left  = constrain(left,  0, 255);
  right = constrain(right, 0, 255);

  ledcWrite(CH_L, left);
  ledcWrite(CH_R, right);

  digitalWrite(MOTOR_L2, LOW);
  digitalWrite(MOTOR_R2, LOW);

  Serial.print("OK:BASE_VEL ");
  Serial.print(v); Serial.print(" ");
  Serial.println(w);
}


// ======================= COMMAND PROCESSING =======================

void procesarComando(String cmd) {

  cmd.trim();

  if (cmd == "STOP_BASE") {
    stopBase();
  }

  else if (cmd == "BASE_EXPLORAR") {
    baseExplorar();
  }

  else if (cmd.startsWith("BASE_VEL")) {
    // Example: BASE_VEL:0.20,0.50
    cmd.replace("BASE_VEL:", "");
    int coma = cmd.indexOf(',');
    if (coma > 0) {
      float v = cmd.substring(0, coma).toFloat();
      float w = cmd.substring(coma + 1).toFloat();
      baseVel(v, w);
    }
  }

  else if (cmd.startsWith("BASE_GOTO")) {
    // For now reception confirmation
    Serial.println("OK:BASE_GOTO");
  }

  else if (cmd == "PING") {
    SerialUART.println("PONG");
  }

  else {
    Serial.print("ERR:CMD_DESCONOCIDO ");
    Serial.println(cmd);
  }
}


// ======================= SETUP =======================

void setup() {
  Serial.begin(115200);                              // USB debug
  SerialUART.begin(115200, SERIAL_8N1, 16, 17);      // UART2

  pinMode(MOTOR_L1, OUTPUT);
  pinMode(MOTOR_L2, OUTPUT);
  pinMode(MOTOR_R1, OUTPUT);
  pinMode(MOTOR_R2, OUTPUT);

  // PWM ESP32 configuration (frecuency 15 kHz, 8 bits)
  ledcSetup(CH_L, 15000, 8);
  ledcSetup(CH_R, 15000, 8);
  ledcAttachPin(MOTOR_L1, CH_L);
  ledcAttachPin(MOTOR_R1, CH_R);

  stopBase();

  Serial.println("ESP32 BASE LISTO");
}


// ======================= LOOP =======================

void loop() {
  while (SerialUART.available()) {
    char c = SerialUART.read();

    if (c == '\n') {
      if (buffer.length() > 0) {
        Serial.print("CMD: ");
        Serial.println(buffer);
        procesarComando(buffer);
        buffer = "";
      }
    } else {
      buffer += c;
    }
  }
}

