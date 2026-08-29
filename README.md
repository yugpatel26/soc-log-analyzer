# 🔍 SOC Log Analyzer

A Python-based command-line tool that analyzes login/authentication logs and detects suspicious activity — inspired by real SOC (Security Operations Center) analyst workflows.

## 🎯 Features

- **Load Logs** — Parse and display login log entries (timestamp, IP address, username, status, location)
- **Detect Suspicious IPs** — Flags IPs with 3+ failed login attempts (brute-force detection)
- **Search by IP/Username** — Look up all activity for a specific IP address or username (case-insensitive)
- **Save Report to CSV** — Exports suspicious IPs to a `suspicious_report.csv` file for record-keeping
- **Detect Successful Login After Failures** — Flags accounts that had multiple failed attempts followed by a successful login — a strong indicator of a potentially compromised account

## 🛠️ Tech Stack

- Python 3
- `csv` module (for reading/writing log data)

## 🚀 How to Run

1. Clone this repository:
```bash
   git clone https://github.com/yugpatel26/soc-log-analyzer.git
```
2. Navigate to the project folder:
```bash
   cd soc-log-analyzer
```
3. Run the application:
```bash
   python main.py
```

## 📖 How It Works

The tool reads login attempt records from `login_logs.csv`. Using a menu-driven interface, users can:
1. View all logged login attempts.
2. Detect IPs with excessive failed login attempts.
3. Search logs by IP address or username.
4. Identify accounts that succeeded after multiple failed attempts (possible compromise)

Suspicious activity is flagged directly in the console, and a summary report can be exported to CSV for further review.

## 📊 Example Log Format

```csv
timestamp,ip_address,username,status,location
2026-08-08 10:15:20,192.168.1.10,admin,failed,India
2026-08-08 10:15:22,192.168.1.10,admin,failed,India
```

## 🧠 Key Learnings

- Working with CSV data using Python's `csv` module (`DictReader`, `DictWriter`)
- Using dictionaries to aggregate and count events (grouping by IP)
- Using sets to track unique values efficiently
- Simulating real-world SOC analyst detection logic (brute-force detection, compromised account indicators)
- Git/GitHub workflow, including resolving merge conflicts and recovering from a corrupted repository

## 📝 Note

This project was built to explore practical, hands-on Python applications in the cybersecurity domain, particularly focused on log analysis techniques used by SOC (Security Operations Center) analysts.

## 👤 Author

**Yug Patel**
GitHub: [@yugpatel26](https://github.com/yugpatel26)