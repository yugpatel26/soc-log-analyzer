import csv


def load_logs():
    with open("login_logs.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
         print(f"Time: {row['timestamp']}, IP: {row['ip_address']}, User: {row['username']}, Status: {row['status']}, Location: {row['location']}")

load_logs()