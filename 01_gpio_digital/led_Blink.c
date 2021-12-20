/*
Wiring Pi 번호로 실행
gpio mode 7 out
//gpio readall
gpio write 7 1
gpio write 7 0
gpio mode 7 in

BCM 번호로 실행
gpio -g mode 4 out
//gpio readall
gpio -g write 4 1
gpio -g write 4 0
gpio -g mode 4 in
*/

// WiringPi PIN...
#include <wiringPi.h>
#define LED 7
int main(void)
{
    wiringPiSetup();
    pinMode(LED,OUTPUT);
    for(int i =0; i < 100; i++)
    {
        digitalWrite(LED,HIGH); delay(1);
        digitalWrite(LED,LOW); delay(1);
    }
    return 0;

}

//BCM PIN으로 하기 위해선, wiringPiSetupGpio()를 해준다 / LED 7 -> 4
//1.gcc -Wall -o 만들이름 파일이름 -lwiringPi 2. ./만들이름
// 실행 ./ 긔긔