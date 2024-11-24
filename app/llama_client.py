import subprocess
import base64
from PIL import Image
from io import BytesIO

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
    try:
        if not prompt and not image_path:
            raise ValueError("Se requiere al menos un prompt o una imagen.")

        # Construir el comando
        command = ["ollama", "run", model, f'"{prompt}"']
        print(f"Ejecutando comando: {' '.join(command)}")  # Log para depuración

        # Ejecutar el comando
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            encoding="utf-8"
        )

        # Verificar errores
        if result.returncode != 0:
            print(f"Error del comando: {result.stderr.strip()}")  # Log del error
            return {"error": result.stderr.strip()}

        # Log para depuración de salida
        print(f"Salida del modelo: {result.stdout.strip()}")

        # Retornar la salida
        return {"response": result.stdout.strip()}

    except FileNotFoundError:
        return {"error": "El comando 'ollama' no se encontró. Verifica la configuración del PATH."}
    except Exception as e:
        return {"error": str(e)}
