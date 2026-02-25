import sys

# --- CONFIGURACIÓN DEL ALFABETO DE 17 SÍMBOLOS ---
ALFABETO = ['+', '-', '*', '/', '$', '//', 'a', 'b', 'x', 'y', 'A', 'B', 'X', 'Y', '0', '1', '2']
INDICES = {simb: i for i, simb in enumerate(ALFABETO)}

def cargar_tarjetas(nombre_archivo):
    tarjetas = []
    num_linea = 0

    try:
        with open(nombre_archivo, 'r') as f:
            for linea in f:
                linea = linea.strip()

                if not linea or linea.startswith("#"):
                    continue

                if "#" in linea:
                    linea = linea.split("#")[0].strip()

                if not linea:
                    continue

                partes = linea.split(',')

                if len(partes) != len(ALFABETO):
                    print(f"Error en {nombre_archivo} línea {num_linea}: {len(partes)} columnas.")
                    sys.exit(1)

                fila = []

                for p in partes:
                    p = p.strip()

                    # Extraer el símbolo a escribir
                    if p.startswith('**') or p.startswith('//'):
                        esc = p[:2]
                        resto = p[2:]
                    else:
                        esc = p[0]
                        resto = p[1:]

                    # --- NUEVA LÓGICA PARA LEER 'e' ---
                    cambia_cinta = False
                    if 'e' in resto:
                        partes_resto = resto.split('e')
                        mov = int(partes_resto[0])
                        sig = int(partes_resto[1])
                        cambia_cinta = True
                    else:
                        mov = int(resto[0])
                        sig = int(resto[1:])

                    # Añadimos un 4to parámetro: el booleano cambia_cinta
                    fila.append([esc, mov, sig, cambia_cinta])

                tarjetas.append(fila)
                num_linea += 1

        return tarjetas

    except FileNotFoundError:
        print(f"Error: Archivo {nombre_archivo} no encontrado.")
        sys.exit(1)

def parsear_cinta(texto):
    cinta = []
    i = 0
    while i < len(texto):
        if i + 1 < len(texto) and texto[i:i+2] in ['**', '//']:
            cinta.append(texto[i:i+2])
            i += 2
        else:
            cinta.append(texto[i])
            i += 1
    return cinta

def interpretar_resultado(cinta):
    print("\n--- 🤖 REPORTE FINAL 🤖 ---")
    cinta_limpia = [s for s in cinta if s in ['1', '2']]
    unos = cinta_limpia.count('1')
    doses = cinta_limpia.count('2')
    print(f"Positivos (1): {unos}")
    print(f"Negativos (2): {doses}")
    print(f"✅ RESULTADO: {unos - doses}")

def ejecutar_maquina(tarjetas1, tarjetas2, cinta_str):
    # Inicialización de la Doble Cinta
    cinta1 = parsear_cinta(cinta_str)
    cinta2 = ['*'] # La cinta auxiliar empieza con un *
    
    pos1 = 0
    pos2 = 0
    
    tarjeta = 0
    pasos = 0
    cinta_activa = 1 # 1 para principal, 2 para auxiliar
    
    # Aumenté los pasos porque las multiplicaciones requieren muchos movimientos
    max_pasos = 10000
    
    print(f"\nSimulando Entrada: {cinta_str}")
    print("-" * 60)

    while True:
        # 1. Determinar el contexto activo
        cinta = cinta1 if cinta_activa == 1 else cinta2
        pos = pos1 if cinta_activa == 1 else pos2
        tarjetas = tarjetas1 if cinta_activa == 1 else tarjetas2

        # 2. Verificar finalización (si pide un estado que no existe en su tarjeta)
        if tarjeta < 0 or tarjeta >= len(tarjetas):
            print(f"\nFin de proceso: Estado {tarjeta} no definido en Cinta {cinta_activa}.")
            break

        # 3. Control de límites de la cinta activa
        if pos < 0: 
            cinta.insert(0, '0')
            pos = 0
            if cinta_activa == 1: pos1 = 0 
            else: pos2 = 0
        elif pos >= len(cinta): 
            cinta.append('0')
            
        simb = cinta[pos]
        
        # Si encuentra un símbolo no reconocido, se detiene
        if simb not in INDICES: 
            break
            
        # --- VISUALIZACIÓN DE AMBAS CINTAS ---
        # Marcamos las posiciones de los cabezales, mostrando solo el activo entre corchetes []
        # --- VISUALIZACIÓN DE AMBAS CINTAS (COMPACTA) ---
        # Marcamos la posición de los cabezales con corchetes
        vis1 = [f"[{s}]" if i == pos1 else s for i, s in enumerate(cinta1)]
        vis2 = [f"[{s}]" if i == pos2 else s for i, s in enumerate(cinta2)]
        
        # Unimos todo sin espacios extra y quitamos los ceros de relleno
        c1_str = "".join([item for item in vis1 if item != '0'])
        c2_str = "".join([item for item in vis2 if item != '0'])
            
        # Imprimimos en el formato simplificado
        print(f"paso {pasos} estado {tarjeta}")
        
        # Pequeña ayuda visual: ponemos un '>' en la cinta que está activa ese turno
        if cinta_activa == 1:
            print(f"1>:{c1_str}\n2 :{c2_str}\n")
        else:
            print(f"1 :{c1_str}\n2>:{c2_str}\n")
        # ------------------------------------------------
        # -------------------------------------
        
        # 4. Leer la instrucción
        idx = INDICES[simb]
        instr = tarjetas[tarjeta][idx]
        nuevo, mov, sig, cambia_cinta = instr
        
        # 5. Escribir y Mover
        cinta[pos] = nuevo
        desplazamiento = 1 if mov == 1 else -1
        
        if cinta_activa == 1:
            pos1 += desplazamiento
        else:
            pos2 += desplazamiento
            
        # 6. Actualizar el estado (y cambiar de cinta si aplica)
        tarjeta = sig
        pasos += 1
        
        if cambia_cinta:
            cinta_activa = 2 if cinta_activa == 1 else 1
        
        if pasos > max_pasos:
            print(f"\n🛑 Límite de pasos alcanzado ({max_pasos}).")
            break
            
    # Resultado de la Cinta 1
    resultado_str = "".join(cinta1).replace('0', '') 
    print("-" * 60)
    print(f"\nCinta 1 Final: {resultado_str}")
    interpretar_resultado(cinta1)

if __name__ == "__main__":
    # Archivos por defecto
    archivo1 = "Entrada.txt"
    archivo2 = "Auxiliar.txt"
    
    # Verificamos si el usuario pasó la cinta como argumento
    if len(sys.argv) > 1:
        cinta_input = sys.argv[1]
    else:
        # Si no se pasa nada, usamos una por defecto y avisamos
        cinta_input = "*ayy"
        print(f"⚠️ No se proporcionó cinta. Usando valor por defecto: {cinta_input}")
        print("💡 Uso correcto: python3 MaquinaTuring.py [cinta]\n")
    
    # Cargamos las tarjetas y ejecutamos
    tarjetas1 = cargar_tarjetas(archivo1)
    tarjetas2 = cargar_tarjetas(archivo2)
    
    ejecutar_maquina(tarjetas1, tarjetas2, cinta_input)