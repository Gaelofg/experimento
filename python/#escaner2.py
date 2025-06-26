#escaner2
import subprocess
import time

ips_activas = []

# Escanear desde .1 hasta .254
for i in range(1, 255):
    ip = f"192.167.1.{i}"  # Cambia el '1' por tu red local si es necesario
    comando = ["ping", "-n", "1", ip]  # En Windows usar '-n', en Linux '-c'
    
    resultado = subprocess.run(comando, stdout=subprocess.DEVNULL)
    
    if resultado.returncode == 0:
        print(f"{ip} está activa ✅")
        ips_activas.append(ip)
    else:
        # Para evitar saturar la consola, solo mostramos el progreso cada 25 IPs
        if i % 25 == 0:
            print(f"Probadas {i} IPs...")

    # Pequeña pausa para no saturar la red y la CPU
    time.sleep(0.05)

# Guardar las IPs activas en un archivo
with open("activos.txt", "w") as archivo:
    for ip in ips_activas:
        archivo.write(ip + "\n")

print("\nEscaneo completo. Resultados guardados en 'activos.txt'")
