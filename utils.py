from openai import OpenAI
import PyPDF2
import mimetypes
import docx2txt
import pymupdf as fitz

def classify_resume_with_gpt4(resume_text, job_description, apiKey):
    cliente = OpenAI(api_key=apiKey)
    prompt = f"""
    You are a AI assistant that helps classify resumes. Given the job description below,
    analyze the following resume and determine if the candidate is a good fit for the position. 
    The answer is in spanish.

    Job Description:
    {job_description}

    Resume:
    {resume_text}

    Sobre la base de lo anterior, por favor responda:
    - ¿Cumple el candidato los requisitos del puesto? (sí/no)
    - Enumere las competencias del candidato que se ajustan a los requisitos del puesto.
    - Indique las lagunas existentes entre la experiencia del candidato y los requisitos del puesto.
    - Proporcione una puntuación porcentual sobre la adecuación del candidato al puesto de trabajo (0-100%)
    """
    response = cliente.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Yu are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    )
    # Esxtraemos y regresamos la respuesta del modelo
    return response.choices[0].message.content


def validate_file(file_path):
    mime_type, _ = mimetypes.guess_type(file_path)
    if mime_type == 'application/pdf':
        return "PDF"
    elif mime_type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
        return "DOCX"
    else:
        return "Unknown format"

def extract_text_from_file(file_path):
    if validate_file(file_path) == "PDF":        
        with open(file_path, 'rb') as f:
            #reader = PyPDF2.PdfReader(f, strict=False)
            reader = fitz.open(file_path)
            text = ""
            for page_num in range(len(reader)):
            #for page in reader.pages:
                #text += page.extract_text()
                text += reader[page_num].get_text()
            reader.close()
            return text
    elif validate_file(file_path) == "DOCX":
        text = docx2txt.process(file_path)
        return text
    else:
        return "Invalid file format"
