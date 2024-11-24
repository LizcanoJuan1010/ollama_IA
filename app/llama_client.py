import subprocess
import base64
from PIL import Image
from io import BytesIO
import subprocess
def preprocess_image(image_path):
    """
    Preprocesa una imagen y la convierte a formato Base64.
    """
    try:
        # Abre la imagen
        with Image.open(image_path) as img:
            # Redimensiona la imagen si es necesario (opcional)
            img = img.resize((224, 224))  # Cambia según las especificaciones del modelo
            # Convierte la imagen a bytes
            buffer = BytesIO()
            img.save(buffer, format="JPEG")
            image_bytes = buffer.getvalue()
            # Codifica la imagen en Base64
            return base64.b64encode(image_bytes).decode("utf-8")
    except Exception as e:
        raise ValueError(f"Error al procesar la imagen: {str(e)}")


def generate_from_model(prompt=None, image_path=None, model="llama3.2-vision:11b"):
    """
    Genera una respuesta desde el modelo usando texto.
    """
    try:
        if not prompt:
            raise ValueError("El prompt es obligatorio si no se proporciona una imagen.")

        # Asegurarse de incluir comillas alrededor del prompt
        command = ["ollama", "run", model, f'"{prompt}"']

        print(f"Ejecutando comando: {' '.join(command)}")  # Depuración

        # Ejecutar el comando
        result = subprocess.run(command, capture_output=True, text=True)

        # Manejo de errores en la ejecución
        if result.returncode != 0:
            return {"error": result.stderr.strip()}

        # Retornar la salida del modelo
        return {"response": result.stdout.strip()}

    except FileNotFoundError:
        return {"error": "El comando 'ollama' no se encontró. Verifica la configuración del PATH."}
    except Exception as e:
        return {"error": str(e)}
