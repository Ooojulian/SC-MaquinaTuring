# 🤖 Simulador de Máquina de Turing Multicinta

Un simulador avanzado de una Máquina de Turing de dos cintas (Doble Cinta) escrito en Python. Este motor está diseñado para ejecutar algoritmos matemáticos complejos, como la multiplicación y la potenciación ($x^y$), mediante la interacción sincronizada entre una cinta principal y una cinta auxiliar.

## 🚀 Características

* **Arquitectura de Doble Cinta:** Utiliza una cinta principal para la entrada/salida de datos y una cinta auxiliar como memoria de trabajo (ideal para subrutinas y cálculos temporales).
* **Comunicación entre Cintas:** Soporte para transiciones de estado que transfieren el control entre la cinta principal y la auxiliar mediante un sistema de "handshake".
* **Alfabeto Personalizado:** Configurado para procesar variables, marcadores y números con un alfabeto de 17 símbolos.
* **Trazabilidad Detallada:** Imprime en consola el paso a paso del estado de ambas cintas y la posición exacta de los cabezales durante la ejecución.
* **Control de Ciclos Infinitos:** Límite de pasos configurable para evitar desbordamientos en cálculos extensos.

## 🛠️ Estructura del Proyecto

* `MaquinaTuring.py`: El motor principal en Python que parsea las instrucciones, maneja la memoria de las cintas y ejecuta la simulación.
* `Entrada.txt`: Contiene la matriz de transiciones (lógica de estados) para la **Cinta 1** (Principal).
* `Auxiliar.txt`: Contiene la matriz de transiciones para la **Cinta 2** (Auxiliar).

## ⚙️ Alfabeto Soportado

La máquina reconoce el siguiente conjunto de símbolos:
`['+', '-', '*', '/', '$', '%', 'a', 'b', 'x', 'y', 'A', 'B', 'X', 'Y', '0', '1', '2']`

*Nota: El símbolo `0` representa el espacio en blanco (vacío) en las cintas.*

## 💻 Instalación y Uso

1. Clona este repositorio:
   ```bash
   git clone [https://github.com/tu-usuario/maquina-de-turing.git](https://github.com/tu-usuario/maquina-de-turing.git)
