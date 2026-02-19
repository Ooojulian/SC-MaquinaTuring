import sys

# --- CONFIGURACIÓN DEL ALFABETO DE 17 SÍMBOLOS ---
ALFABETO = ['+', '-', '*', '/', '**', '//', 'a', 'b', 'x', 'y', 'A', 'B', 'X', 'Y', '0', '1', '2']
INDICES = {simb: i for i, simb in enumerate(ALFABETO)}

def cargar_tarjetas(nombre_archivo):
    tarjetas = []
    num_linea = 0

    try:
        with open(nombre_archivo, 'r') as f:
            for linea in f:

                # eliminar espacios extremos
                linea = linea.strip()

                # ignorar línea vacía
                if not linea:
                    continue

                # ignorar comentario completo
                if linea.startswith("#"):
                    continue

                # eliminar comentario al final
                if "#" in linea:
                    linea = linea.split("#")[0].strip()

                # volver a verificar si quedó vacía
                if not linea:
                    continue

                partes = linea.split(',')

                if len(partes) != len(ALFABETO):
                    print(f"Error línea {num_linea}: {len(partes)} columnas.")
                    sys.exit(1)

                fila = []

                for p in partes:

                    p = p.strip()

                    if p.startswith('**') or p.startswith('//'):
                        esc = p[:2]
                        resto = p[2:]
                    else:
                        esc = p[0]
                        resto = p[1:]

                    mov = int(resto[0])
                    sig = int(resto[1:])

                    fila.append([esc, mov, sig])

                tarjetas.append(fila)
                num_linea += 1

        return tarjetas

    except FileNotFoundError:
        print("Error: Archivo no encontrado.")
        sys.exit(1)

    tarjetas = []
    num_linea = 0
    try:
        with open(nombre_archivo, 'r') as f:
            for linea in f:
                linea = linea.strip()
                if not linea: continue
                partes = linea.split(',')
                if len(partes) != len(ALFABETO):
                    print(f"Error línea {num_linea}: {len(partes)} columnas.")
                    sys.exit(1)
                fila = []
                for p in partes:
                    p = p.strip()
                    if p.startswith('**') or p.startswith('//'):
                        esc = p[:2]; resto = p[2:]
                    else:
                        esc = p[0]; resto = p[1:]
                    mov = int(resto[0])
                    sig = int(resto[1:])
                    fila.append([esc, mov, sig])
                tarjetas.append(fila)
                num_linea += 1
        return tarjetas
    except FileNotFoundError:
        print("Error: Archivo no encontrado.")
        sys.exit(1)

def parsear_cinta(texto):
    cinta = []
    i = 0
    while i < len(texto):
        if i + 1 < len(texto) and texto[i:i+2] in ['**', '//']:
            cinta.append(texto[i:i+2]); i += 2
        else:
            cinta.append(texto[i]); i += 1
    return cinta

def interpretar_resultado(cinta):
    print("\n--- 🤖 REPORTE FINAL 🤖 ---")
    cinta_limpia = [s for s in cinta if s in ['1', '2']]
    unos = cinta_limpia.count('1')
    doses = cinta_limpia.count('2')
    print(f"Positivos (1): {unos}")
    print(f"Negativos (2): {doses}")
    print(f"✅ RESULTADO: {unos - doses}")

def ejecutar_maquina(tarjetas, cinta_str):
    cinta = parsear_cinta(cinta_str)
    pos = 0
    tarjeta = 0
    pasos = 0
    
    # Aumentamos los pasos porque la división gasta muchos movimientos
    max_pasos = 2000 
    
    print(f"\nSimulando: {cinta_str}")

    while 0 <= tarjeta < len(tarjetas):
        pasos += 1
        if pos < 0: cinta.insert(0, '0'); pos = 0
        elif pos >= len(cinta): cinta.append('0')
            
        simb = cinta[pos]
        if simb not in INDICES: break
        
        idx = INDICES[simb]
        instr = tarjetas[tarjeta][idx]
        
        nuevo, mov, sig = instr
        
        cinta[pos] = nuevo
        pos += 1 if mov == 1 else -1
        tarjeta = sig
        
        if pasos > max_pasos:
            print(f"🛑 Límite de pasos alcanzado ({max_pasos}).")
            break
            
    # --- AQUÍ ESTÁ EL CAMBIO PARA QUITAR LOS CEROS ---
    resultado_str = "".join(cinta).strip('0') 
    print(f"\nCinta Final: {resultado_str}")
    # -------------------------------------------------
    
    interpretar_resultado(cinta)
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 MaquinaTuring.py Entrada.txt")
    else:
        archivo = sys.argv[1]
        ejecutar_maquina(cargar_tarjetas(archivo), "+xxyy")