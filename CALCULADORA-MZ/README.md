# Proyecto CALCULADORA - Midori Zapata

## 1. Descripción del Sistema
Este proyecto implementa un sistema de generación 
de números pseudoaleatorios y la realización de pruebas estadísticas 
para analizar su comportamiento. Está desarrollado en Python 3.10 usando 
Tkinter, numpy y matplotlib, y cuenta con una interfaz gráfica 
intuitiva.

El sistema permite:
- Generar números pseudoaleatorios mediante distintos algoritmos.
- Realizar pruebas estadísticas de media, varianza y uniformidad (Chi²).
- Visualizar resultados numéricos, histogramas y tablas de frecuencias.

## 2. Estructura del Proyecto
Proyecto_PRNG/
├── main.py 
├── generators.py 
├── tests.py 
├── utils.py 
├── README.md 

## 3. Algoritmos Implementados

### 3.1 Generadores de Números Pseudoaleatorios
- **Cuadrados Medios**: Calcula los números tomando los dígitos centrales del cuadrado de la semilla.
- **Productos Medios**: Genera números usando los dígitos centrales del producto de dos semillas.
- **Multiplicador Constante**: Usa una constante multiplicativa sobre la semilla para generar la secuencia.

### 3.2 Pruebas Estadísticas
- **Prueba de Media**: Verifica que la media de la secuencia esté cerca de 0.5.
- **Prueba de Varianza**: Evalúa la dispersión de los números generados.
- **Prueba de Uniformidad (Chi²)**: Compara la distribución observada con la distribución uniforme esperada.

## 4. Interfaz Gráfica (GUI)
La GUI está dividida en **3 pestañas**:

1. **Generadores**
   - Entradas: Semilla(s), Cantidad de números a generar (`n`)
   - Botones: `Cuadrados Medios`, `Productos Medios`, `Multiplicador Constante`
   - Muestra: Resultados numéricos y **histograma** de los números generados

2. **Pruebas**
   - Botones: `Prueba Media`, `Prueba Varianza`, `Prueba Uniformidad (Chi²)`
   - Muestra: Resultados de las pruebas estadísticas

3. **Variables**
   - Permite configurar parámetros adicionales como `k` para la prueba Chi² (opcional)
   - Preparada para futuras extensiones

## 5. Dependencias
- Python 3.10
- Librerías estándar:
  - `tkinter`
- Librerías externas:
  - `numpy`
  - `matplotlib`
