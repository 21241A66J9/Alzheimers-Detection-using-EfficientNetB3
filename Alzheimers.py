#Interface for the project

import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image, ImageTk
import threading
import time
import math
import numpy as np
import tensorflow as tf


# Load model
model = tf.keras.models.load_model('C:/Users/21241a66j9/OneDrive/Desktop/al/best.keras')

# Class labels and descriptions
class_info = {
    0: ('Mild Dementia', '🧠 Early signs of memory loss, slight confusion. Monitoring and early treatment recommended.'),
    1: ('Moderate Dementia', '🧠 Pronounced cognitive decline. Needs regular support and care.'),
    2: ('Non Demented', '🧠 No signs of dementia. Brain appears healthy in the scan.'),
    3: ('Very Mild Dementia', '🧠 Minimal but noticeable memory lapses. Lifestyle and medical advice can help.')
}

# Prediction logic
def predict_image(filepath):
    img = tf.keras.preprocessing.image.load_img(filepath, target_size=(224, 224))
    img_array = tf.keras.preprocessing.image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions, axis=1)[0]
    probability = round(np.max(predictions) * 100, 2)
    return predicted_class, probability

# Prediction process with animation
def predict_image_with_animation(filepath):
    hide_content()
    window.config(bg="#01081D")
    loader_canvas.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    progress_bar.place(relx=0.5, rely=0.5, y=130, anchor=tk.CENTER)  # Positioned below animation
    animate.set(True)
    draw_brain_wave()
    window.update()

    start_progress_bar()

    # Reduced delay to 1 second
    time.sleep(1)

    predicted_class, probability = predict_image(filepath)
    name, description = class_info[predicted_class]

    animate.set(False)
    loader_canvas.place_forget()
    progress_bar.place_forget()
    show_content()
    window.config(bg=bg_main)

    result_label.config(
        text=f"🧠 Prediction: {name}\n🔍 Confidence: {probability}%",
        fg=active_fg,
        font=('Arial', 20, 'bold')
    )
    note_label.config(
        text=description,
        fg=subtle_fg
    )

def start_progress_bar():
    progress_bar['value'] = 0
    max_value = 100
    def loop():
        current = progress_bar['value']
        if current < max_value:
            progress_bar['value'] = current + 5
            window.after(50, loop)
    loop()

def upload_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        image = Image.open(file_path).resize((250, 250))
        photo = ImageTk.PhotoImage(image)
        mri_image_label.config(image=photo)
        mri_image_label.image = photo
        threading.Thread(target=predict_image_with_animation, args=(file_path,)).start()

def reset_app():
    mri_image_label.config(image='')
    mri_image_label.image = None
    result_label.config(text='')
    note_label.config(text='')

def toggle_dark_mode():
    global is_dark, bg_main, bg_container, active_fg, subtle_fg
    is_dark = not is_dark
    if is_dark:
        bg_main = "#1E2A38"
        bg_container = "#3A617E"
        active_fg = "#00FFAA"
        subtle_fg = "#B0E0E6"
    else:
        bg_main = "#F0F0F0"
        bg_container = "#FFFFFF"
        active_fg = "#222"
        subtle_fg = "#444"
    apply_theme()

def apply_theme():
    window.config(bg=bg_main)
    container.config(bg=bg_container)
    mri_image_label.config(bg=bg_container)
    loader_canvas.config(bg="#01081D")
    result_label.config(bg=bg_container, fg=active_fg)
    note_label.config(bg=bg_container, fg=subtle_fg)
    reset_button.config(bg=bg_container, fg="white" if is_dark else "black")
    dark_mode_button.config(bg=bg_container, fg="white" if is_dark else "black")

def hide_content():
    container.pack_forget()

def show_content():
    container.pack(pady=20, padx=20, fill='both', expand=True)

# === Theme Variables ===
is_dark = True
bg_main = "#1E2A38"
bg_container = "#3A617E"
active_fg = "#00FFAA"
subtle_fg = "#B0E0E6"

# === Window Setup ===
window = tk.Tk()
window.title("🧠 Alzheimer's MRI Classifier")
window.geometry("700x550")
window.config(bg=bg_main)

# === Buttons Top Frame ===
top_btns = tk.Frame(window, bg=bg_main)
top_btns.pack(fill='x', pady=10)

reset_button = tk.Button(top_btns, text="🔄 Reset", command=reset_app, bg=bg_container, fg="white", relief='flat', font=('Arial', 10, 'bold'))
reset_button.pack(side='left', padx=10)

dark_mode_button = tk.Button(top_btns, text="🌓 Toggle Theme", command=toggle_dark_mode, bg=bg_container, fg="white", relief='flat', font=('Arial', 10, 'bold'))
dark_mode_button.pack(side='left', padx=10)

upload_btn = tk.Button(top_btns, text="📁 Upload MRI Image", command=upload_image, bg="#4CAF50", fg="white", font=('Arial', 12, 'bold'))
upload_btn.pack(side='right', padx=10)

# === Main Container ===
container = tk.Frame(window, bg=bg_container, bd=3, relief='ridge')
container.pack(pady=20, padx=20, fill='both', expand=True)

mri_image_label = tk.Label(container, bg=bg_container)
mri_image_label.pack(pady=15)

result_label = tk.Label(container, text="", font=('Arial', 20, 'bold'), bg=bg_container, fg=active_fg)
result_label.pack(pady=10)

note_label = tk.Label(container, text="", font=('Arial', 11), bg=bg_container, fg=subtle_fg, wraplength=500, justify='center')
note_label.pack(pady=5)

# === Brain Animation Setup ===
loader_canvas = tk.Canvas(window, width=200, height=200, bg="#01081D", highlightthickness=0)
animate = tk.BooleanVar(value=False)

def draw_brain_wave():
    if not animate.get():
        return
    loader_canvas.delete("all")
    time_now = time.time()
    center_x, center_y = 100, 100
    for i in range(8):
        angle = i * (360 / 8)
        radians = math.radians(angle)
        r = 40 + 10 * math.sin(time_now * 2 + i)
        x = center_x + r * math.cos(radians)
        y = center_y + r * math.sin(radians)
        size = 8 + 4 * math.sin(time_now * 3 + i)
        loader_canvas.create_oval(x - size, y - size, x + size, y + size, fill="#00FFAA", outline="")
    window.after(50, draw_brain_wave)

# === Progress Bar ===
progress_bar = tk.ttk.Progressbar(window, orient="horizontal", length=180, mode="determinate")

# === Start Main Loop ===
window.mainloop()
