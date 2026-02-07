// base_control.ino
// ESP32 de la BASE: recibe comandos por UART2 y controla 2 motores DC

#include <HardwareSerial.h>

HardwareSerial SerialUART(2);   // UART2 (RX=16, TX=17 por defecto)

// PINS DEL DRIVER DE MOTORES  (AJUSTA A TU CONEXIÓN)
const int MOTOR_L1 = 5;   // PWM izquierda adelante
const int MOTOR_L2 = 18;  // PWM izquierda atrás (opcional)
const int MOTOR_R1 = 19;  // PWM derecha adelante
const int MOTOR_R2 = 21;  // PWM derecha atrás (opcional)

// Canales PWM del ESP32
const int CH_L = 0;
const int CH_R = 1;

String buffer = "";

// ======================= FUNCIONES DE MOTOR =======================

void stopBase() {
  ledcWrite(CH_L, 0);
  ledcWrite(CH_R, 0);
  digitalWrite(MOTOR_L2, LOW);
  digitalWrite(MOTOR_R2, LOW);
  Serial.println("OK:STOP_BASE");
}

void baseExplorar() {
  // Adelante lento
  ledcWrite(CH_L, 120);
  ledcWrite(CH_R, 120);
  digitalWrite(MOTOR_L2, LOW);
  digitalWrite(MOTOR_R2, LOW);
  Serial.println("OK:BASE_EXPLORAR");
}

void baseVel(float v, float w) {
  // v = velocidad lineal (m/s aprox)
  // w = velocidad angular (rad/s aprox)
  // Mapeo simple a PWM: aquí luego ajustas a tu robot real

  int base_pwm = 150;                    // PWM base
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


// ======================= PROCESAR COMANDOS =======================

void procesarComando(String cmd) {

  cmd.trim();

  if (cmd == "STOP_BASE") {
    stopBase();
  }

  else if (cmd == "BASE_EXPLORAR") {
    baseExplorar();
  }

  else if (cmd.startsWith("BASE_VEL")) {
    // Ejemplo: BASE_VEL:0.20,0.50
    cmd.replace("BASE_VEL:", "");
    int coma = cmd.indexOf(',');
    if (coma > 0) {
      float v = cmd.substring(0, coma).toFloat();
      float w = cmd.substring(coma + 1).toFloat();
      baseVel(v, w);
    }
  }

  else if (cmd.startsWith("BASE_GOTO")) {
    // Por ahora solo confirmamos recepción
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

  // Configurar PWM ESP32 (frecuencia 15 kHz, 8 bits)
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
