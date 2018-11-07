//Constantes

const int trigPinCenter = 6;
const int echoPinCenter = 7;
const int trigPinRight = 8;
const int echoPinRight = 9;
const int trigPinLeft = 2;
const int echoPinLeft = 3;


// defines variables
long duration;
int distance;



void setup() {
pinMode(trigPinCenter, OUTPUT); // Sets the trigPin as an Output
pinMode(echoPinCenter, INPUT); // Sets the echoPin as an Input
pinMode(trigPinRight, OUTPUT); // Sets the trigPin as an Output
pinMode(echoPinRight, INPUT); // Sets the echoPin as an Input
pinMode(trigPinLeft, OUTPUT); // Sets the trigPin as an Output
pinMode(echoPinLeft, INPUT); // Sets the echoPin as an Input


Serial.begin(9600); // Starts the serial communication
}
void loop() {
// Clears the trigPin
digitalWrite(trigPinCenter, LOW);
delayMicroseconds(2);
// Sets the trigPin on HIGH state for 10 micro seconds
digitalWrite(trigPinCenter, HIGH);
delayMicroseconds(10);
digitalWrite(trigPinCenter, LOW);
// Reads the echoPin, returns the sound wave travel time in microseconds
duration = pulseIn(echoPinCenter, HIGH);
// Calculating the distance
distance= duration*0.034/2;
// Prints the distance on the Serial Monitor
Serial.print("C-");
Serial.print(distance);

digitalWrite(trigPinRight, LOW);
delayMicroseconds(2);
// Sets the trigPin on HIGH state for 10 micro seconds
digitalWrite(trigPinRight, HIGH);
delayMicroseconds(10);
digitalWrite(trigPinRight, LOW);
// Reads the echoPin, returns the sound wave travel time in microseconds
duration = pulseIn(echoPinRight, HIGH);
// Calculating the distance
distance= duration*0.034/2;
// Prints the distance on the Serial Monitor
Serial.print("-R-");
Serial.print(distance);

digitalWrite(trigPinLeft, LOW);
delayMicroseconds(2);
// Sets the trigPin on HIGH state for 10 micro seconds
digitalWrite(trigPinLeft, HIGH);
delayMicroseconds(10);
digitalWrite(trigPinLeft, LOW);
// Reads the echoPin, returns the sound wave travel time in microseconds
duration = pulseIn(echoPinLeft, HIGH);
// Calculating the distance
distance= duration*0.034/2;
// Prints the distance on the Serial Monitor
Serial.print("-L-");
Serial.println(distance);

delay(100);

}
