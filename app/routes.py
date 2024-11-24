from flask import Blueprint, request, jsonify
from .llama_client import generate_from_model

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

        # Validar que al menos uno esté presente
        if not prompt and not image_path:
            return jsonify({"error": "El campo 'prompt' o 'image_path' es obligatorio."}), 400

        # Llamar a la función de generación
        response = generate_from_model(prompt=prompt, image_path=image_path)

        # Devolver la respuesta generada
        return jsonify(response)

    except Exception as e:
        print(f"Error interno: {e}")
        return jsonify({"error": "Error interno en el servidor.", "detalle": str(e)}), 500
