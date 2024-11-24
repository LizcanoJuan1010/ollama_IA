from flask import Blueprint, request, jsonify
from .llama_client import generate_from_model

# Crear un blueprint para el API
api = Blueprint("api", __name__)

@api.route("/generate", methods=["POST"])
def generate():
    """
    Endpoint para generar una respuesta usando texto, imágenes o ambos.
    """
    try:
        # Obtener datos enviados en la solicitud
        data = request.json

        # Extraer el prompt y la ruta de la imagen (si existen)
        prompt = data.get("prompt", None)
        image_path = data.get("image_path", None)

        # Verificar que al menos el prompt esté presente
        if not prompt:
            return jsonify({"error": "El campo 'prompt' es obligatorio."}), 400

        # Generar la respuesta usando el modelo
        response = generate_from_model(prompt=prompt, image_path=image_path)

        # Devolver la respuesta del modelo
        return jsonify(response)

    except Exception as e:
        # Manejar errores de forma general
        return jsonify({"error": str(e)}), 500
