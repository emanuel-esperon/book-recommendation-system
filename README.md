# Sistema de recomendación de libros

Proyecto de análisis y desarrollo de un sistema de recomendación de libros utilizando técnicas de filtrado colaborativo.

Se implementan y comparan tres modelos:

- KNN ítem-ítem
- KNN usuario-usuario
- SVD mediante factorización matricial

Además, se analizan las métricas de desempeño según distintos grupos de usuarios.

## Dataset

Se utiliza el dataset **Book-Crossing**, compuesto por información sobre:

- Libros
- Usuarios
- Calificaciones de libros

Los archivos se descargan automáticamente desde el repositorio utilizado en el notebook de análisis y preprocesamiento.

## Estructura del proyecto

```text
.
├── eda_y_preprocesamiento.ipynb
├── modelo_knn_item.ipynb
├── modelo_knn_usuario.ipynb
├── modelo_svd.ipynb
├── metrics.py
├── requeriments.txt
└── .gitignore
```
## Instalación

Se recomienda utilizar un entorno virtual de python
  python -m venv venv

En Windows:
  venv\Scripts\activate

Linux o macOS
  source venv/bin/activate

instalar las dependencias
  pip install -r requeriments.txt

## Ejecución

1. Abrir eda_y_preprocesamiento.ipynb.
2. Ejecutar las celdas para descargar y procesar el dataset.
3. Verificar que se hayan generado ratings_limpios.csv y resumen_usuario.csv.
4. Ejecutar alguno de los notebooks de modelos:

Tecnologías utilizadas:
* Python
* Pandas
* Numpy
* SciPy
* Matplotlib
* Scikit-Surprise
* Jupyter Notebook

  
 
