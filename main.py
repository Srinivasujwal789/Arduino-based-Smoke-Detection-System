
For Arduino, libraries are specified in the code and installed via the IDE:
- `WiFi.h` (built-in with ESP32 support)
- `ESP32_MailClient.h` (install via Library Manager)

---

#### 3. Source Code (`src/main.ino`)
```cpp
#include <WiFi.h>
#include <ESP32_MailClient.h>

// Wi-Fi credentials
const char* ssid = "YOUR_WIFI_SSID";
const char* password = "YOUR_WIFI_PASSWORD";

// SMTP email settings
#define SMTP_HOST "smtp.gmail.com"
#define SMTP_PORT 465
#define EMAIL_SENDER "your_email@gmail.com"
#define EMAIL_PASSWORD "your_app_specific_password"  // Use App Password for Gmail
#define EMAIL_RECIPIENT "recipient_email@example.com"

// Pin definitions
const int MQ6_PIN = 34;  // Analog pin for MQ6 sensor
const int GREEN_LED = 26;
const int RED_LED = 27;
const int BUZZER = 25;

// Threshold for smoke detection
const int SMOKE_THRESHOLD = 500;  // Adjust based on calibration

// Email object
SMTPData smtpData;

void setup() {
  Serial.begin(115200);
  
  // Initialize pins
  pinMode(GREEN_LED, OUTPUT);
  pinMode(RED_LED, OUTPUT);
  pinMode(BUZZER, OUTPUT);
  pinMode(MQ6_PIN, INPUT);

  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  Serial.print("Connecting to Wi-Fi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nConnected to Wi-Fi");
}

void loop() {
  int sensorValue = analogRead(MQ6_PIN);
  Serial.print("MQ6 Sensor Value: ");
  Serial.println(sensorValue);

  if (sensorValue < SMOKE_THRESHOLD) {
    // No smoke detected
    digitalWrite(GREEN_LED, HIGH);
    digitalWrite(RED_LED, LOW);
    digitalWrite(BUZZER, LOW);
  } else {
    // Smoke detected
    digitalWrite(GREEN_LED, LOW);
    digitalWrite(RED_LED, HIGH);
    digitalWrite(BUZZER, HIGH);
    sendEmailAlert();
    delay(5000);  // Prevent multiple emails in quick succession
    digitalWrite(BUZZER, LOW);  // Turn off buzzer after 5s
  }

  delay(1000);  // Check every second
}

void sendEmailAlert() {
  smtpData.setLogin(SMTP_HOST, SMTP_PORT, EMAIL_SENDER, EMAIL_PASSWORD);
  smtpData.setSender("Smoke Detector", EMAIL_SENDER);
  smtpData.setPriority("High");
  smtpData.setSubject("Smoke Detected!");
  smtpData.setMessage("Smoke detected by the system on " + String(millis()/1000) + " seconds uptime.", false);
  smtpData.addRecipient(EMAIL_RECIPIENT);

  if (!MailClient.sendMail(smtpData)) {
    Serial.println("Error sending email: " + MailClient.smtpErrorReason());
  } else {
    Serial.println("Email sent successfully!");
  }

  smtpData.empty();  // Clear SMTP data for next use
}
