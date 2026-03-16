# 🤖 Simulador de Máquina de Turing Multicinta

Un simulador avanzado de una Máquina de Turing de dos cintas (Doble Cinta) escrito en Python. Este motor está diseñado para ejecutar algoritmos matemáticos complejos, como la multiplicación, la potenciación y la radicación, mediante la interacción sincronizada entre una cinta principal y una cinta auxiliar.

## 🚀 Características

* **Arquitectura de Doble Cinta:** Utiliza una cinta principal para la entrada/salida de datos y una cinta auxiliar como memoria de trabajo (ideal para subrutinas y cálculos temporales).
* **Comunicación entre Cintas:** Soporte para transiciones de estado que transfieren el control entre la cinta principal y la auxiliar mediante un sistema de "handshake".
* **Lógica Unaria:** Utiliza un sistema de representación de datos basado en el conteo de caracteres, permitiendo procesar operaciones aritméticas paso a paso.
* **Trazabilidad Detallada:** Imprime en consola el paso a paso del estado de ambas cintas y la posición exacta de los cabezales durante la ejecución.
* **Control de Ciclos Infinitos:** Límite de pasos configurable para evitar desbordamientos en cálculos extensos o algoritmos de fuerza bruta.

## 🛠️ Estructura del Proyecto

* `MaquinaTuring.py`: El motor principal en Python que parsea las instrucciones, maneja la memoria de las cintas y ejecuta la simulación.
* `Entrada.txt`: Contiene la matriz de transiciones (lógica de estados) para la **Cinta 1** (Principal).
* `Auxiliar.txt`: Contiene la matriz de transiciones para la **Cinta 2** (Auxiliar).

## 🔠 Alfabeto y Sintaxis

La máquina opera utilizando un sistema unario, donde el valor de un número está representado por la cantidad de veces que se repite una letra. El alfabeto completo es:
`['+', '-', '*', '/', '$', '%', 'a', 'b', 'x', 'y', 'A', 'B', 'X', 'Y', '0', '1', '2']`

### 1. Operadores Matemáticos (Inician la cadena)
* `+` : Suma
* `-` : Resta
* `*` : Multiplicación
* `$` : Potenciación 
* `%` : Radicación (Raíz cuadrada)

### 2. Operandos (Variables Unarias)
* **`x`**: Representa el **Primer Operando** (o la base) si es un número **positivo**. Ej: `xxx` = 3.
* **`y`**: Representa el **Segundo Operando** (o el exponente) si es un número **positivo**. Ej: `yy` = 2.
* **`a`**: Representa el **Primer Operando** si es un número **negativo**. Ej: `aa` = -2.
* **`b`**: Representa el **Segundo Operando** si es un número **negativo**. Ej: `bbbb` = -4.

### 3. Símbolos del Sistema (Uso Interno de la Máquina)
* **`X`, `Y`, `A`, `B`**: Versiones mayúsculas de las variables. La máquina las usa como "marcadores" para saber qué caracteres ya han sido procesados y no perder la cuenta.
* **`0`**: Representa el espacio en blanco o celda vacía en la cinta.
* **`1`, `2`**: Contadores numéricos temporales utilizados por la máquina para transferir valores entre cintas o almacenar resultados parciales.
* **`/`**: Muro o separador de memoria utilizado en algoritmos complejos (como la radicación) para aislar candidatos.

## 📐 Cómo Formatear una Operación

Para ejecutar la máquina, debes pasarle una cadena de texto como argumento. La estructura siempre debe ser:
`[Operador][Operando 1][Operando 2]`

### Ejemplos de Uso:

**Suma Positiva (2 + 3):**
* Operador: `+`
* Primer operando (2): `xx`
* Segundo operando (3): `yyy`
* **Entrada:** `+xxyyy`

**Multiplicación con Negativos (-3 * 2):**
* Operador: `*`
* Primer operando (-3): `aaa`
* Segundo operando (2): `yy`
* **Entrada:** `*aaayy`

**Potenciación (2 al cubo):**
* Operador: `$`
* Base (2): `xx`
* Exponente (3): `yyy`
* **Entrada:** `$xxyyy`

**Radicación (Raíz cuadrada de 4):**
* Operador: `%`
* Número (4): `xxxx`
* *(En la lógica de raíz cuadrada, la máquina asume el índice 2, por lo que las `y` pueden omitirse o usarse como formato de entrada base dependiendo de la configuración)*.
* **Entrada:** `%xxxx`

## 💻 Instalación y Ejecución

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone [https://github.com/tu-usuario/maquina-de-turing.git](https://github.com/tu-usuario/maquina-de-turing.git)
