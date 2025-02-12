# ALECS DDOS ATTACK PREMIUM v2.0 🚀

## Descriere
ALECS DDOS ATTACK PREMIUM este un instrument avansat de testare a securității rețelelor, dezvoltat de ALECS Security Labs. Acest tool permite testarea rezistenței serverelor la atacuri DDoS prin simularea traficului TCP și UDP.

⚠️ **ATENȚIE**: Acest instrument este destinat EXCLUSIV pentru testare și cercetare pe sisteme pentru care aveți permisiune explicită de testare!

## Caracteristici 🌟
- Interface colorată și animată
- Suport pentru atacuri TCP și UDP
- Sistem multi-threading pentru performanță maximă
- Validare avansată a țintelor
- Statistici în timp real
- Rapoarte detaliate
- Sistem de logging pentru debugging

## Cerințe Sistem 💻
- Python 3.7 sau mai nou
- Sistem de operare: Windows/Linux/MacOS
- Conexiune la internet
- Drepturi de administrator (pentru anumite funcționalități)

## Instalare 🔧

1. Clonați repository-ul:
```bash
git clone https://github.com/arian222/alecs-ddos-premium.git
cd alecs-ddos-premium
```

2. Instalați dependințele necesare:
```bash
pip install -r requirements.txt
```

Sau instalați manual dependințele:
```bash
pip install colorama
```

## Utilizare 📝

1. Rulați scriptul:
```bash
python ddos_simulator.py
```

2. Urmați instrucțiunile din interfață:
   - Confirmați că aveți permisiunea de testare
   - Introduceți adresa IP țintă
   - Specificați portul țintă (0-65535)
   - Setați durata atacului (în secunde)
   - Alegeți numărul de thread-uri
   - Selectați metoda de atac (TCP/UDP)

## Exemple de Utilizare 🎯

### Test Basic
```bash
Target IP: 127.0.0.1
Target Port: 80
Durată: 30
Thread-uri: 10
Metodă: TCP
```

### Test Avansat
```bash
Target IP: 192.168.1.1
Target Port: 443
Durată: 60
Thread-uri: 50
Metodă: UDP
```

## Monitorizare și Statistici 📊
- Bara de progres colorată în timp real
- Rata de pachete trimise pe secundă
- Număr total de pachete trimise
- Rata de succes
- Erori întâmpinate

## Troubleshooting 🔍

### Erori Comune:
1. "Adresă IP invalidă":
   - Verificați formatul adresei IP (ex: 192.168.1.1)
   
2. "Nu s-a putut rezolva adresa IP":
   - Verificați conexiunea la internet
   - Verificați dacă adresa IP este accesibilă
   
3. "Port invalid":
   - Folosiți porturi între 0 și 65535
   - Verificați dacă portul este deschis pe țintă

## Securitate și Responsabilitate 🛡️

⚠️ **AVERTISMENT**:
- Folosiți acest tool DOAR pentru testare autorizată
- Obțineți permisiune scrisă înainte de testare
- Nu folosiți pentru activități malițioase
- Respectați legile și regulamentele locale

## Logging și Debugging 📝
- Fișierul `ddos.log` conține informații detaliate despre execuție
- Verificați acest fișier pentru depanarea problemelor

## Suport 💬
Pentru suport și întrebări, contactați ALECS Security Labs:
- Email: alecsalecs021@gmail.com
- Website: www.alecs-security.com

## Licență 📄
Copyright © 2024 ALECS Security Labs. Toate drepturile rezervate.

## Actualizări 🔄
Verificați periodic repository-ul pentru actualizări și îmbunătățiri.

---
Creat cu ❤️ de ALECS Security Labs 
