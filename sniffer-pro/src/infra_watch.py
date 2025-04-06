# psutil (python system and process utility) é uma biblioteca multiplataforma para recuperar informações sobre processos em execução e utilização do sistema (CPU, memória, discos, rede, sensores) em Python . 
# É útil principalmente para monitoramento de sistema , criação de perfil , limitação de recursos de processo e gerenciamento de processos em execução .

import psutil
from datetime import datetime
import time
# Limites
CPU_LIMIT = 28.0  # %
RAM_LIMIT = 80.0  # %
DISK_LIMIT = 50.0  # % livre

LOG_FILE = "monitoramento.txt"

def registrar_alerta(mensagem):
    with open("meu_arquivo.txt", "a", encoding="utf-8") as arquivo:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        arquivo.write(f"[{timestamp}] {mensagem}\n")


def monitorar():
    cpu = psutil.cpu_percent(interval=3)
    ram = psutil.virtual_memory().percent
    disco = psutil.disk_usage('/').percent
    livre_disco = 100 - disco

    log = f"[{datetime.now()}] CPU: {cpu}% | RAM: {ram}% | Disco Livre: {livre_disco:.2f}%"
    print(log)

    alerta = ""
    if cpu > CPU_LIMIT:
        alerta += f"⚠️ CPU em {cpu}% (limite: {CPU_LIMIT}%)"
        registrar_alerta(alerta)
    if ram > RAM_LIMIT:
        alerta += f"⚠️ RAM em {ram}% (limite: {RAM_LIMIT}%)"
        registrar_alerta(alerta)
    if livre_disco > DISK_LIMIT:
        alerta += f"⚠️ Espaço em disco alto: {livre_disco:.2f}% livre (mínimo: {DISK_LIMIT}%)"
        registrar_alerta(alerta)
    if alerta != "":
        print(alerta)


while True:
    monitorar()
    time.sleep(0.3)
