from flask import Flask, render_template
import RPi.GPIO as GPIO

LED_PIN = 4
LED_PIN2 = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)


app = Flask(__name__)


@app.route("/")
def main():
    return render_template("led.html")


@app.route("/led/<cmd>")
def led_op(cmd):
    if cmd == "on":
        GPIO.output(LED_PIN, GPIO.HIGH)
        return "<p>LED ON</p>"
    elif cmd == "off":
        GPIO.output(LED_PIN, GPIO.LOW)
        return "<p>LED OFF</p>"
    elif cmd == "on2":
        GPIO.output(LED_PIN2, GPIO.HIGH)
        return "<p>LED2 ON</p>"
    elif cmd == "off2":
        GPIO.output(LED_PIN2, GPIO.LOW)
        return "<p>LED2 OFF</p>"
    else:
        return "<p>404 error</p>"


if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", debug=True)
    finally:
        GPIO.cleanup()