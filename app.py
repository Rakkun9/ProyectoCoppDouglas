import os
from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import sympy as sp  # Importar Sympy para cálculos simbólicos

# Inicializar Flask
app = Flask(__name__)

# Crear la función para generar el costo total con Sympy
def calcular_costo_total_simb(costo_incremental, costo_constante, costo_fijo_inicial, unidades):
    # Definir la variable simbólica
    x = sp.Symbol('x')

    # Función del costo marginal (derivada del costo total)
    costo_marginal = costo_incremental * x + costo_constante

    # Integrar el costo marginal para obtener el costo total
    costo_total_simb = sp.integrate(costo_marginal, x) + costo_fijo_inicial

    # Sustituir el valor de las unidades en el costo total
    costo_total = costo_total_simb.subs(x, unidades)
    return float(costo_total)  # Convertir el resultado a un número flotante

# Ruta principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para realizar cálculos
@app.route('/calcular', methods=['POST'])
def calcular():
    try:
        # Obtener datos del formulario
        costo_incremental = float(request.form['costo_incremental'])
        costo_constante = float(request.form['costo_constante'])
        costo_fijo_inicial = float(request.form['costo_fijo_inicial'])
        unidades = int(request.form['unidades'])
        margen_ganancia = float(request.form['margen_ganancia'])

        # Validar datos ingresados
        if unidades <= 0:
            error = "La cantidad de unidades debe ser mayor a 0."
            return render_template('index.html', error=error)

        if margen_ganancia < 0:
            error = "El margen de ganancia no puede ser negativo."
            return render_template('index.html', error=error)

        # Calcular el costo total usando Sympy
        costo_total = calcular_costo_total_simb(costo_incremental, costo_constante, costo_fijo_inicial, unidades)

        # Calcular el precio de venta mínimo
        precio_venta_minimo = (costo_total * (1 + margen_ganancia / 100)) / unidades

        # Generar gráfico
        generar_grafico(costo_incremental, costo_constante, costo_fijo_inicial, unidades)

        # Renderizar resultados
        return render_template('index.html',
                               resultado=costo_total,
                               unidades=unidades,
                               precio_venta_minimo=precio_venta_minimo,
                               margen_ganancia=margen_ganancia)

    except ValueError:
        error = "Por favor, ingrese valores numéricos válidos."
        return render_template('index.html', error=error)

# Función para generar un gráfico usando Matplotlib
def generar_grafico(costo_incremental, costo_constante, costo_fijo_inicial, unidades_max):
    x = range(unidades_max + 1)
    y = [calcular_costo_total_simb(costo_incremental, costo_constante, costo_fijo_inicial, u) for u in x]

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label="Costo total", color="blue")
    plt.title("Costo Total vs Unidades Producidas")
    plt.xlabel("Unidades Producidas")
    plt.ylabel("Costo Total")
    plt.grid()
    plt.legend()
    plt.tight_layout()

    if not os.path.exists("static"):
        os.makedirs("static")
    plt.savefig("static/grafico.png")
    plt.close()

# Ejecutar la aplicación
if __name__ == "__main__":
    app.run(debug=True)
