import nmap
import datetime

def calculate_risk(open_ports):
    count = len(open_ports)

    if count == 0:
        return "LOW", 10
    elif count <= 5:
        return "MEDIUM", 40
    elif count <= 10:
        return "HIGH", 70
    else:
        return "CRITICAL", 90


# ⚔️ ATTACK MODULE
def scan_target(target, scan_type):
    nm = nmap.PortScanner()

    if scan_type == "quick":
        arguments = "-F"
    elif scan_type == "service":
        arguments = "-sV"
    elif scan_type == "os":
        arguments = "-O"
    elif scan_type == "full":
        arguments = "-A"
    else:
        arguments = "-F"

    nm.scan(target, arguments=arguments)

    open_ports = []

    result = "=== ⚔️ ATTACK MODE (Reconnaissance) ===\n"
    result += f"Scan Time: {datetime.datetime.now()}\n"
    result += f"Target: {target}\n\n"

    for host in nm.all_hosts():
        result += f"Host: {host}\n"
        result += f"State: {nm[host].state()}\n"

        for proto in nm[host].all_protocols():
            result += f"\nProtocol: {proto}\n"

            for port in nm[host][proto]:
                service = nm[host][proto][port]['name']
                open_ports.append(port)
                result += f"Port: {port} | Service: {service}\n"

    # 🔥 Risk + Score
    risk, score = calculate_risk(open_ports)

    result += f"\n🚨 Risk Level: {risk}\n"
    result += f"📊 Threat Score: {score}/100\n"

    # Save report
    with open("scan_report.txt", "w") as f:
        f.write(result)

    return result, open_ports


# 🛡️ DEFENSE MODULE
def defense_analysis(target, open_ports):
    result = "=== 🛡️ DEFENSE MODE (Hardening) ===\n"
    result += f"Target: {target}\n\n"

    if not open_ports:
        result += "No attack data found. Run Attack Mode first.\n"
        return result

    result += "🔍 Detected Exposure:\n"
    for port in open_ports:
        result += f"- Port {port} is open\n"

    result += "\n🛡️ Recommended Actions:\n"

    if 22 in open_ports:
        result += "• Secure SSH → disable root login, use key authentication\n"
    if 21 in open_ports:
        result += "• Disable FTP or use secure alternatives (SFTP)\n"
    if 80 in open_ports:
        result += "• Secure Web Server → use HTTPS & WAF\n"
    if 443 in open_ports:
        result += "• Verify SSL/TLS configuration\n"
    if 3306 in open_ports:
        result += "• Restrict database access (MySQL)\n"

    if len(open_ports) > 5:
        result += "• Too many open ports → apply firewall rules (UFW)\n"

    result += "• Disable unused services\n"
    result += "• Enable IDS/IPS systems\n"
    result += "• Regular patching & updates\n"

    result += "\n✔ Defense simulation complete\n"

    with open("scan_report.txt", "w") as f:
        f.write(result)

    return result