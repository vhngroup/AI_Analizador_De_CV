import streamlit as st
from utils import extract_text_from_file, classify_resume_with_gpt4
from dotenv import load_dotenv, find_dotenv
from os.path import join, dirname
import os

dotenv_path = join(dirname(__file__), '../.env') #Indica la ruta del fichero .env con las keys de OpenAI

#load_dotenv(find_dotenv(), override=True)
load_dotenv(dotenv_path)
apiKey = os.environ.get('OPENAI_KEY')

st.set_page_config(page_title="Clasificador de Hojas de vida", page_icon="📄", layout="centered")
st.title("Clasificador de Hojas de vida")


job_description = st.text_area("Por favor ingresa la descripción del trabajo")
resume = st.file_uploader("Resumen", accept_multiple_files=False, type=["pdf", "docx"])
if st.button("Generar Clasificación"):
    save_path = 'Cv_Inputs_Files/'+resume.name
    with st.spinner("Generando Clasificación..."):
        if resume is not None:
            #Guardamos el archivo en la carpeta de trabajo
            save_path = 'Cv_Inputs_Files/'+resume.name
            with open(save_path, 'wb') as f:
                f.write(resume.read())
            resume_text = extract_text_from_file(save_path)
            classification = classify_resume_with_gpt4(resume_text, job_description, apiKey)
            st.header("Resultado de la clasificación")
            st.write(classification)
        else:
            st.error("Por favor, sube un archivo de CV")

