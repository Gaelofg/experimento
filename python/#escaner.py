#escaner
import subprocess

ips_activas = []

for i in range(1, 11):
    ip = f"192.168.1.{i}"
    comando = ["ping", "-n", "1", ip]
    resultado = subprocess.run(comando, stdout=subprocess.DEVNULL)

    if resultado.returncode == 0:
        print(f"{ip} está activa ✅")
        ips_activas.append(ip)
    else:
        print(f"{ip} no respondió ❌")

with open("activos.txt", "w") as archivo:
    for ip in ips_activas:
        archivo.write(ip + "\n")

print("Escaneo terminado ✔")