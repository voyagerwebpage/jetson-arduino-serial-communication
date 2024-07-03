void setup() 
{
    /*
    IMPORTANT: assigned 115200 as the data rate in bits per second (baud) for serial data transmission, value can be changed to 9600
     */
    Serial.begin(115200);

    while(!Serial) {
        ; // waiting for the serial port to connect
    }
}

const char TERMINATOR = '|'; 

void loop()
{
    /*
    Constantly checking for data from the Jetson, once data is received the data is sent for processing inside the if condition.
    */
    if (Serial.avaiable() > 0)
    {
        // char messageBuffer[32];
        // int size = Serial.readBytesUntill('\n', messageBuffer, 32);
        String commandFromJetson = Serial.readStringUntill(TERMINATOR);

        //confirm
        //S
        String ackMsg = "Received from Jetson: " + commandFromJetson;

        Serial.print(ackMsg);
        //Serial.flush();
    }
    delay(500);
}