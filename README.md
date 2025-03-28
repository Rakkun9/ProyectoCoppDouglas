# Aplicación de Función de Producción Cobb-Douglas

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.0.1-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

Aplicación web desarrollada con Flask para calcular y visualizar la función de producción Cobb-Douglas, utilizada en economía para modelar la relación entre inputs (trabajo y capital) y outputs (producción).

## Características Principales

- 🧮 **Cálculo preciso** de producción total (Q) usando la fórmula:  
  **Q = A × Lᵅ × Kᵝ**
- 📊 **Gráficos interactivos** de:
  - Producción vs Trabajo (con capital fijo)
  - Producción vs Capital (con trabajo fijo)
- 📈 **Análisis económico** completo:
  - Productividades marginales (PML y PMK)
  - Rendimientos a escala (crecientes, constantes o decrecientes)
- 🛠️ **Validación de datos** para parámetros económicos válidos
- 🎨 **Interfaz intuitiva** con explicaciones integradas

## Requisitos Técnicos

- Python 3.8 o superior
- Dependencias principales:

  ```bash
  Flask==2.0.1
  matplotlib==3.4.3
  numpy==1.21.2
  