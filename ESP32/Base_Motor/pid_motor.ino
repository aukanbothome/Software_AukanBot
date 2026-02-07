// pid_motor.ino
// Prueba de control PID de velocidad para UN motor con encoder

#include <PID_v1.h>

// ==== PINS (AJUSTAR A TU HARDWARE) ====
const int ENCODER_A = 34;
const int ENCODER_B = 35;
const int MOTOR_PWM = 5;   // PWM
const int MOTOR_IN2 = 18;  // Sentido (si usas puente H)

const int PWM_CHANNEL = 0;

// ==== ENCODER ====
volatile long encoderCount = 0;
const int PULSOS_POR_VUELTA = 360;   // AJUSTA según tu encoder

void IRAM_ATTR encoderISR() {
  int b = digitalRead(ENCODER_B);
  if (b == HIGH) encoderCount++;
  else encoderCount--;
}

// ==== PID ====
double setpointRPM = 0;
double inputRPM = 0;
double outputPWM = 0;

// Kp, Ki, Kd - empiezan simples, luego ajustas
double Kp = 1.0, Ki = 0.5, Kd = 0.0;

PID pid(&inputRPM, &outputPWM, &setpointRPM, Kp, Ki, Kd, DIRECT);

unsigned long lastSample = 0;
const unsigned long SAMPLE_MS = 100;


// ==== SETUP ====
void setup() {
  Serial.begin(115200);

  pinMode(ENCODER_A, INPUT_PULLUP);
  pinMode(ENCODER_B, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(ENCODER_A), encoderISR, CHANGE);

  pinMode(MOTOR_PWM, OUTPUT);
  pinMode(MOTOR_IN2, OUTPUT);

  // PWM
  ledcSetup(PWM_CHANNEL, 15000, 8);
  ledcAttachPin(MOTOR_PWM, PWM_CHANNEL);

  digitalWrite(MOTOR_IN2, LOW);

  // PID config
  pid.SetMode(AUTOMATIC);
  pid.SetOutputLimits(0, 255);   // salida será el PWM
  pid.SetSampleTime(SAMPLE_MS);

  setpointRPM = 50.0;   // meta inicial: 50 RPM

  Serial.println("PID de motor iniciado. Cambia la referencia con 'Sxxx'.");
}


// ==== LOOP ====
void loop() {
  unsigned long now = millis();
  if (now - lastSample >= SAMPLE_MS) {
    lastSample = now;

    // Calcular RPM a partir de encoderCount
    long counts = encoderCount;
    encoderCount = 0;

    double vueltasPorMuestra = (double)counts / (double)PULSOS_POR_VUELTA;
    double muestrasPorMinuto = 60000.0 / (double)SAMPLE_MS;
    inputRPM = vueltasPorMuestra * muestrasPorMinuto;

    // Calcular PID
    pid.Compute();

    // Aplicar PWM
    ledcWrite(PWM_CHANNEL, (int)outputPWM);
    digitalWrite(MOTOR_IN2, LOW);  // dirección fija (adelante)

    // Debug
    Serial.print("Setpoint RPM: ");
    Serial.print(setpointRPM);
    Serial.print(" | RPM actual: ");
    Serial.print(inputRPM);
    Serial.print(" | PWM: ");
    Serial.println(outputPWM);
  }

  // Cambiar referencia desde el monitor serie:
  // Escribe por ejemplo: S80 y ENTER -> setpoint = 80 RPM
  if (Serial.available()) {
    String cmd = Serial.readStringUntil('\n');
    cmd.trim();
    if (cmd.startsWith("S")) {
      double s = cmd.substring(1).toDouble();
      setpointRPM = s;
      Serial.print("Nuevo setpoint RPM: ");
      Serial.println(setpointRPM);
    }
  }
}
