#define adc A0
#define avgResolution 5
//PARAMETERS
double b = 3380;
double r0 = 10000.0;
double t0 = 298.0;

int high= -1;
int low= -1;

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
    rSum += r;
  }
  double rAvg = rSum/(double) avgResolution;
  double temperatureK = b / (log(rAvg / r0) + (b / t0));
  int temperatureF = (int) (temperatureK - 273.15) * (9.0/5.0) + 32;
  if(temperatureF > high){
    high = temperatureF;
    if(low == -1) low = high;
  }
  else if(temperatureF < low) low = temperatureF;
  Serial.println(String(low) + ',' + String(high));
  delay(500);
}
