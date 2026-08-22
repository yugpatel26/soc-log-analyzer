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


def search_logs():
    search_term = input("Enter IP address or username to search: ")
    found = False
    with open("login_logs.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["ip_address"] == search_term or row["username"] == search_term:
                print(f"Time: {row['timestamp']}, IP: {row['ip_address']}, User: {row['username']}, Status: {row['status']}, Location: {row['location']}")
                found = True
    if not found:
        print("No records found.")


while True:
    print("----SOC LOG ANALYZER----")
    print("1. Load Logs")
    print("2. Detect Suspicious IPs")
    print("3. Search by IP/Username")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        load_logs()
    elif choice == "2":
        detect_suspicious_ips()
    elif choice == "3":
        search_logs()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")