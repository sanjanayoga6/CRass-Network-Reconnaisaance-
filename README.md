# 🛡️ CRass: Attack-Defense Cyber Range Simulation

## 📌 Overview
CRass (Cyber Range as a Service) is a GUI-based cybersecurity simulation tool that demonstrates both **attack** and **defense** operations in a controlled environment.  

The system uses **Nmap** for network reconnaissance and provides **intelligent defense recommendations** based on detected vulnerabilities. It simulates a real-world cyber range where users can understand attacker and defender perspectives.

---

## ⚔️ Attack Module (Reconnaissance)
The attack module performs network scanning using Nmap to identify potential vulnerabilities.

### Features:
- Detects open ports
- Identifies running services
- Supports multiple scan types:
  - Quick Scan (`-F`)
  - Service Detection (`-sV`)
  - OS Detection (`-O`)
  - Full Scan (`-A`)
- Calculates:
  - 🚨 Risk Level (LOW / MEDIUM / HIGH / CRITICAL)
  - 📊 Threat Score (0–100)

---

## 🛡️ Defense Module (Hardening)
The defense module analyzes scan results and provides mitigation strategies.

### Features:
- Identifies exposed ports
- Suggests security improvements:
  - SSH hardening
  - Web server protection
  - Database security
- Recommends:
  - Firewall configuration
  - Service restriction
  - Patch management
  - IDS/IPS implementation

---

## 💻 Technologies Used
- **Python** – Backend logic  
- **Flask** – Web framework  
- **Nmap** – Network scanning  
- **HTML & CSS** – User Interface  
- **VS Code** – Development environment  

---

## 🧠 Working Process
1. User enters target IP address  
2. Selects mode (Attack / Defense)  
3. Chooses scan type (Attack mode)  
4. System performs scanning or analysis  
5. Displays results on UI  
6. Generates downloadable report  

---

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/sanjanayoga6/CRass-Attack-Defense-CyberRange.git
cd CRass-Attack-Defense-CyberRange

````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
python app.py
```

### 4. Open in browser

```
http://127.0.0.1:5000
```


## 📊 Features Summary

* GUI-based cyber range simulation
* Attack and Defense modules
* Risk level classification
* Threat scoring system
* Intelligent security recommendations
* Downloadable scan reports

## ⚠️ Limitations

* Defense module is simulation-based
* Requires Nmap installation
* OS detection may require administrative privileges
* Limited to single target scanning

## 🔮 Future Enhancements

* CVE-based vulnerability detection
* Graphical visualization (charts)
* Multi-target scanning
* User authentication system
* Real-time monitoring dashboard

## 📚 References

* Nmap Official Documentation
* Flask Documentation
* Python Documentation

## ⭐ Note

This project is developed for educational purposes as part of a **Cyber Range Simulation Activity**.



