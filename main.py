import csv


def load_logs():
    with open("login_logs.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
         print(f"Time: {row['timestamp']}, IP: {row['ip_address']}, User: {row['username']}, Status: {row['status']}, Location: {row['location']}")

def detect_suspicious_ips():
    failed_attempts = {}
    with open("login_logs.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["status"] == "failed":
                ip = row["ip_address"]
                if ip in failed_attempts:
                    failed_attempts[ip] = failed_attempts[ip] + 1
                else:
                    failed_attempts[ip] = 1

    for ip, count in failed_attempts.items():
        if count >= 3: 
            print(f"SUSPICIOUS: {ip} had {count} failed login attempts!")


load_logs()
detect_suspicious_ips()
