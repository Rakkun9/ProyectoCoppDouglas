 Resumen
Este proyecto es una herramienta basada en Python que permite a los usuarios calcular el costo total de producción, a partir del costo marginal y el costo fijo inicial. También proporciona una interfaz web construida con Flask, lo que permite a los usuarios ingresar valores de manera interactiva y visualizar representaciones gráficas de sus datos de costos. Además, la aplicación puede sugerir un precio de venta para lograr un margen de ganancia específico basado en los costos calculados.

Características
Cálculo de Costos: Utiliza el cálculo integral para calcular el costo total de producción a partir de la función de costo marginal.
Representación Gráfica: Genera gráficos con la biblioteca Matplotlib de Python, lo que permite visualizar los datos de costo de producción.
Optimización de Ganancias: La aplicación calcula el punto de equilibrio y sugiere un precio de venta para lograr ganancias deseadas.
Interfaz Web: El marco Flask permite que el usuario interactúe con la herramienta a través de una interfaz web, facilitando la entrada y salida de datos.
Requisitos
Para ejecutar este proyecto, se necesitan las siguientes bibliotecas de Python:

Flask: Marco web para crear la aplicación.
SymPy: Biblioteca de matemáticas simbólicas para realizar el cálculo integral.
Matplotlib: Biblioteca para crear gráficos y visualizaciones.

Para instalar las bibliotecas necesarias, ejecuta:
pip install Flask sympy matplotlib

Uso:
1. Clona el repositorio: git clone https://github.com/ConnorSnow/proyectocalcint
2. Navega al directorio del proyecto: cd proyectocalcint
3. Ejecuta la aplicación Flask: python app.py
4.  Abre un navegador web y accede a http://127.0.0.1:5000/ para interactuar con la aplicación.


Cómo Funciona:

La aplicación calcula el costo total de producción mediante la integración de la función de costo marginal.

La fórmula utilizada para la función de costo marginal es una ecuación lineal, por ejemplo, C'(x) = a * x + b, donde a es el costo incremental por unidad y b es el costo constante.

Después de realizar la integración, el costo total se calcula sumando el costo fijo inicial al resultado de la integral.

El usuario puede ajustar parámetros como el costo marginal, el costo inicial y el número de unidades producidas.

La aplicación también grafica la función de costo y proporciona una herramienta interactiva para comprender la estructura de costos.


Ejemplo

Cuando el usuario ingresa:

Costo marginal: 5x + 200

Costo fijo inicial: 1000

Unidades producidas: 10

La herramienta calcula el costo total de producción y sugiere un precio de venta óptimo para lograr los márgenes de ganancia deseados.
