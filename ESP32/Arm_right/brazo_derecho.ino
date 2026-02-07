#include <HardwareSerial.h>
#include <Servo.h>

HardwareSerial SerialUART(2);
Servo servoBrazo;

String buffer = "";
int SERVO_PIN = 23;

void moverBrazo(int ang) {
  servoBrazo.write(ang);
  Serial.print("OK:BRAZO_D:");
  Serial.println(ang);
}

void saludar() {
  for (int i = 0; i < 3; i++) {
    servoBrazo.write(90);
    delay(400);
    servoBrazo.write(20);
    delay(400);
  }
  servoBrazo.write(0);
  Serial.println("OK:SALUDAR");
}

void procesarComando(String cmd) {

  if (cmd == "SALUDAR") {
    saludar();
  }

  else if (cmd.startsWith("BRAZO_D")) {
    cmd.replace("BRAZO_D:", "");
    int ang = cmd.toInt();
    moverBrazo(ang);
  }

  else if (cmd == "STOP_BRAZOS") {
    moverBrazo(0);
    Serial.println("OK:STOP_BRAZOS");
  }

}

void setup() {
  Serial.begin(115200);
  SerialUART.begin(115200, SERIAL_8N1, 16, 17);
  servoBrazo.attach(SERVO_PIN);
  moverBrazo(0);
  Serial.println("ESP32 BRAZO DERECHO LISTO");
}

void loop() {
  while (SerialUART.available()) {
    char c = SerialUART.read();

    if (c == '\n') {
      procesarComando(buffer);
      buffer = "";
    } else buffer += c;
  }
}
