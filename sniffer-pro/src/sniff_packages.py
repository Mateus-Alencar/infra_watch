from scapy.all import sniff, IP, IPv6, DNS
from datetime import datetime
import os

os.makedirs("../logs", exist_ok=True)

def registrar_log(mensagem):
    with open("../logs/pacotes.log", "a", encoding="utf-8") as arquivo:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        arquivo.write(f"[{timestamp}] {mensagem}\n")

def analisar_pacote(p):
    if IP in p:
        info = f"[IPv4] {p[IP].src} --> {p[IP].dst}"
    elif IPv6 in p:
        info = f"[IPv6] {p[IPv6].src} --> {p[IPv6].dst}"
    else:
        info = "[Outro pacote]"

    if DNS in p:
        info += " | DNS: " + p[DNS].summary()

    print(info)
    registrar_log(info)

print("🎯 Iniciando captura de pacotes...")
sniff(prn=analisar_pacote)
