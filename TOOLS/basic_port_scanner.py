target_host = input("Enter the target IP or domain: ")
try:
    target_ip = socket.gethostbyname(target_host)
except socket.gaierror:
    print(f"Error: Unable to resolve '{target_host}'. Please enter a valid IP or domain.")
    exit()

target_ports = range(1, 66000)

print(f"Scanning {target_host} ({target_ip})...")

for port in target_ports:
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.1)
        result = client.connect_ex((target_ip, port))
        if result == 0:
            print(f"Port {port} is open")
        client.close()
    except KeyboardInterrupt:
        print("\nScan interrupted by user.")
        break
    except Exception as e:
        print(f"Error scanning port {port}: {e}")
        continue

print("Scan complete.")
