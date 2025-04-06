import requests

def get_global_ip():
    response = requests.get('https://api.ipify.org?format=json')
    ip_data = response.json()
    return ip_data['ip']

global_ip = get_global_ip()
print(f"グローバルIPv4アドレス: {global_ip}")

def get_global_ipv6():
    response = requests.get('https://api64.ipify.org?format=json')
    ip_data = response.json()
    return ip_data['ip']

global_ipv6 = get_global_ipv6()
print(f"グローバルIPv6アドレス: {global_ipv6}")