import subprocess
import time

def conexoes_ativas():
    #Usa o módulo subprocess para executar o comando netstat -n no terminal:
    #    -n: Mostra os endereços em formato numérico (sem DNS).
    #    capture_output=True: captura a saída do comando.
    #    text=True: retorna como string (em vez de bytes)
    try:
        resultado = subprocess.run(['netstat', '-n'], capture_output=True, text=True)
        linhas = resultado.stdout.splitlines()
        ips = []
        for linha in linhas:
            if "ESTABLISHED" in linha:
                partes = linha.split()
                if len(partes) >= 3:
                    ip_destino = partes[2].split(":")[0]
                    ips.append(ip_destino)
        print(ips)
        return ips
    except Exception as e:
        print(f"Erro ao capturar conexões: {e}")
        return []

def monitorar(ip_monitorado):
    print(f"Monitorando acesso ao IP: {ip_monitorado}")
    while True:
        ips_conectados = conexoes_ativas()
        if ip_monitorado in ips_conectados:
            print(f"🔔 IP {ip_monitorado} foi acessado!")
            break
        else:
            print("Nenhuma conexão com o IP monitorado.")
        time.sleep(5)

IPmonitorado = input("Ip a ser monitorado: ")
monitorar(IPmonitorado)
