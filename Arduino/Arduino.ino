#include <Servo.h>

#define pinDigServo1 2

int angulo = 45;
String cadena;
Servo servoMotor1;

void setup()
{
    Serial.begin(9600);
    servoMotor1.attach(pinDigServo1);
    servoMotor1.write(angulo);
}

void loop()
{
    if (Serial.available())
    {
        cadena = Serial.readString();

        if (cadena == "1")
        {
            angulo = angulo + 2;
        }
        if (cadena == "-1")
        {
            angulo = angulo - 2;
        }

        if (cadena == "end")
        {

            angulo = 45;
        }
        servoMotor1.write(angulo);
    }
}
