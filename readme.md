## Analizador de hojas de vida y clasificador de posibles candidatos ##
![Ejemplo](https://github.com/vhngroup/excel_form_with_tkinter_openpyxl/blob/main/static/screen.png)
### Herramienta:
En este ejemplo a través del prompt de lenguaje natural, se le puede pedir al modelo que analice y responda a los siguientes interrogantes:
    - ¿Cumple el candidato los requisitos del puesto? (sí/no)
    - Enumere las competencias del candidato que se ajustan a los requisitos del puesto.
    - Indique los vacios existentes entre la experiencia del candidato y los requisitos del puesto.
    - Proporcione una puntuación porcentual sobre la adecuación del candidato al puesto de trabajo (0-100%)
* Se ha usado la API de OpenAI y el modelo "GPT-4".
* Para dar más precisión a los resultados se ha utilizado un agente de OpenAI lo que nos permite poder hacer preguntas en un lenguaje mas natural y con respuestas mas precisas.
### Uso:
    * Recomendamos siempre usar entorno virtual venv.
    * Instalamos las dependencias: pip install -r requirements.txt
    * Ejecutamos el script: streamlit run .\main.py
    * Se debe contar con una cuenta de OpenAI y crear en ella un proyecto y crear una contraseña de API, usar la variable "OPENAI_API_KEY".
    * Podemos seleccionar archivos de tipo PDF y Docx