import os
from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import numpy as np

# Inicializar Flask
app = Flask(__name__)

# Función para calcular la producción Cobb-Douglas
def calcular_produccion_cobb_douglas(A, L, K, alpha, beta):
    """
    Calcula la producción usando la función Cobb-Douglas
    Q = A * (L^alpha) * (K^beta)
    """
    return A * (L ** alpha) * (K ** beta)

# Función para calcular la productividad marginal
def calcular_productividad_marginal(A, L, K, alpha, beta, factor):
    """
    Calcula la productividad marginal del trabajo (PML) o capital (PMK)
    factor: 'L' para trabajo o 'K' para capital
    """
    if factor == 'L':
        return alpha * A * (L ** (alpha - 1)) * (K ** beta)
    elif factor == 'K':
        return beta * A * (L ** alpha) * (K ** (beta - 1))
    else:
        return None

# Ruta principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para realizar cálculos
@app.route('/calcular', methods=['POST'])
def calcular():
    try:
        # Obtener datos del formulario
        A = float(request.form['A'])
        L = float(request.form['L'])
        K = float(request.form['K'])
        alpha = float(request.form['alpha'])
        beta = float(request.form['beta'])
        
        # Validar datos ingresados
        if L <= 0 or K <= 0:
            error = "Los valores de L y K deben ser mayores a 0."
            return render_template('index.html', error=error)
        
        if alpha < 0 or beta < 0:
            error = "Los valores de alpha y beta no pueden ser negativos."
            return render_template('index.html', error=error)

        # Calcular la producción total
        produccion_total = calcular_produccion_cobb_douglas(A, L, K, alpha, beta)
        
        # Calcular productividades marginales
        PML = calcular_productividad_marginal(A, L, K, alpha, beta, 'L')
        PMK = calcular_productividad_marginal(A, L, K, alpha, beta, 'K')
        
        # Calcular rendimientos a escala
        rendimientos = alpha + beta
        
        if rendimientos > 1:
            tipo_rendimientos = "crecientes a escala"
        elif rendimientos == 1:
            tipo_rendimientos = "constantes a escala"
        else:
            tipo_rendimientos = "decrecientes a escala"
        
        # Generar gráficos
        generar_graficos(A, L, K, alpha, beta)
        
        # Renderizar resultados
        return render_template('index.html',
                             produccion_total=produccion_total,
                             PML=PML,
                             PMK=PMK,
                             rendimientos=rendimientos,
                             tipo_rendimientos=tipo_rendimientos,
                             A=A, L=L, K=K, alpha=alpha, beta=beta)

    except ValueError:
        error = "Por favor, ingrese valores numéricos válidos."
        return render_template('index.html', error=error)

# Función para generar gráficos
def generar_graficos(A, L, K, alpha, beta):
    # Gráfico 1: Producción vs Trabajo (con capital fijo)
    L_values = np.linspace(1, L*2, 100)
    Q_L = [calcular_produccion_cobb_douglas(A, l, K, alpha, beta) for l in L_values]
    
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    plt.plot(L_values, Q_L, label=f"Producción (K fijo en {K})", color="blue")
    plt.title("Producción vs Trabajo (Capital fijo)")
    plt.xlabel("Trabajo (L)")
    plt.ylabel("Producción (Q)")
    plt.grid()
    plt.legend()
    
    # Gráfico 2: Producción vs Capital (con trabajo fijo)
    K_values = np.linspace(1, K*2, 100)
    Q_K = [calcular_produccion_cobb_douglas(A, L, k, alpha, beta) for k in K_values]
    
    plt.subplot(1, 2, 2)
    plt.plot(K_values, Q_K, label=f"Producción (L fijo en {L})", color="green")
    plt.title("Producción vs Capital (Trabajo fijo)")
    plt.xlabel("Capital (K)")
    plt.ylabel("Producción (Q)")
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