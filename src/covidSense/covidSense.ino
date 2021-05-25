#define adc A0
#define avgResolution 5
//PARAMETERS
double b = 3380;
double r0 = 10000.0;
double t0 = 298.0;


void setup() {
  // put your setup code here, to run once:
  pinMode(adc, INPUT);
  Serial.begin(9600);
}

void loop() {
  double rSum= 0;
  double r; 
  double adcVal;
  for (int i=0; i < avgResolution; ++i) {
    adcVal = analogRead(adc);
    r = (1023 * r0  / adcVal) - r0;
//    Serial.println(R);
    rSum += r;
  }
//  Serial.println(adc_sum);
  double rAvg = rSum/(double) avgResolution;
  double temperatureK = b / (log(rAvg / r0) + (b / t0));
//  Serial.println(temperatureK);

  double temperatureF = (temperatureK - 273.15) * (9.0/5.0) + 32;
  Serial.println(temperatureF);
  
  delay(1000);
//  Serial.println("hello");
  
}
