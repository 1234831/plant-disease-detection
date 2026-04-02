import gradio as gr
import numpy as np
from PIL import Image
import tensorflow as tf

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
        return "Please upload an image"

    image = image.convert("RGB")
    image = image.resize((224, 224))

    img = np.array(image)
    img = np.expand_dims(img, axis=0)

    preds = model.predict(img, verbose=0)[0]

    top_index = np.argmax(preds)
    confidence = float(preds[top_index] * 100)
    label = format_label(CLASS_NAMES[top_index])

    return f"🔎 Prediction: {label}\n🔥 Confidence: {confidence:.2f}%"

with gr.Blocks() as app:
    gr.Markdown("# Tomato Disease Detection")

    image_input = gr.Image(type="pil", label="Upload Image")
    predict_btn = gr.Button("Predict")

    output_text = gr.Textbox(label="Result")

    predict_btn.click(
        fn=predict,
        inputs=image_input,
        outputs=output_text
    )

app.launch(ssr_mode=False)