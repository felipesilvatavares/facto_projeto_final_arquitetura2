String readString;
int porta_rele1 = 10;
int porta_rele2 = 7;
int porta_rele3 = 8;
int porta_rele4 = 4;

void setup() {
  pinMode(12, OUTPUT);
  pinMode(13, OUTPUT);
  pinMode(2, OUTPUT);
  
  pinMode(porta_rele1, OUTPUT); 
  digitalWrite(porta_rele1, HIGH);

  pinMode(porta_rele2, OUTPUT); 
  digitalWrite(porta_rele2, HIGH);

  pinMode(porta_rele3, OUTPUT); 
  digitalWrite(porta_rele3, HIGH);

  pinMode(porta_rele4, OUTPUT); 
  digitalWrite(porta_rele4, HIGH);
  
  Serial.begin(9600);
}


void loop() { 
  digitalWrite(12, HIGH);
  digitalWrite(13, HIGH);
  digitalWrite(2, HIGH);
   
  while (Serial.available()) {
      delay(2);
      char c = Serial.read();
      readString += c;
    }

   readString.trim();
  
    if (readString.length() >0) {
      Serial.println(readString);

      if (readString == "ligarar"){
        digitalWrite(porta_rele1, LOW);
      }
      else
      if (readString == "desligarar"){
        digitalWrite(porta_rele1, HIGH);
      }
      else
      if (readString == "abrirportao"){
        digitalWrite(porta_rele3, HIGH);
        digitalWrite(porta_rele2, LOW);
        delay(5000);
        digitalWrite(porta_rele2, HIGH);
      }
      else
      if (readString == "fecharportao"){
        digitalWrite(porta_rele2, HIGH);
        digitalWrite(porta_rele3, LOW);
        delay(5000);
        digitalWrite(porta_rele3, HIGH);
      }
      else
      if (readString == "acenderluz"){
        digitalWrite(porta_rele4, LOW);
      }
      else
      if (readString == "desligarluz"){
        digitalWrite(porta_rele4, HIGH);
      }
          
     readString="";
  } 
}
