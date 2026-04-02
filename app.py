import gradio as gr
import numpy as np
from PIL import Image
import tensorflow as tf

# Load model
model = tf.keras.models.load_model("model.keras", compile=False)

CLASS_NAMES = [
    'Bacterial_spot',
    'Early_blight',
    'Late_blight',
    'Leaf_Mold',
    'Septoria_leaf_spot',
    'Spider_mites Two-spotted_spider_mite',
    'Target_Spot',
    'Tomato_Yellow_Leaf_Curl_Virus',
    'Tomato_mosaic_virus',
    'healthy',
    'powdery_mildew'
]

def format_label(label):
    return label.replace("_", " ")

def predict(image):
    if image is None:
        return "<p style='font-size:20px;'>⚠️ Please upload an image</p>"

    # Preprocess image
    image = image.convert("RGB")
    image = image.resize((224, 224))

    img = np.array(image)
    img = np.expand_dims(img, axis=0)

    # Prediction
    preds = model.predict(img, verbose=0)[0]

    top_index = np.argmax(preds)
    confidence = float(preds[top_index] * 100)
    label = format_label(CLASS_NAMES[top_index])

    # Styled Output
    return f"""
    <div style="text-align:center; padding:20px; border-radius:15px; background-color:#f5f5f5;">
        <div style="font-size:28px; font-weight:bold; color:#2c3e50;">
            🔎 {label}
        </div>
        <div style="font-size:22px; margin-top:10px; color:#e74c3c;">
            🔥 Confidence: {confidence:.2f}%
        </div>
    </div>
    """

# UI
with gr.Blocks(theme=gr.themes.Soft()) as app:
    gr.Markdown(
        """
        <h1 style='text-align:center; color:#27ae60;'>🍅 Tomato Disease Detection</h1>
        <p style='text-align:center;'>Upload a tomato leaf image and get prediction instantly</p>
        """
    )

    with gr.Row():
        image_input = gr.Image(type="pil", label="Upload Leaf Image")

    predict_btn = gr.Button("🚀 Predict", variant="primary")

    output_text = gr.Markdown(label="Result")

    predict_btn.click(
        fn=predict,
        inputs=image_input,
        outputs=output_text
    )

app.launch(ssr_mode=False)