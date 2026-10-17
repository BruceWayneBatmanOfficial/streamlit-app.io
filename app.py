import streamlit as st
from PIL import Image

# 1. Page Configuration & Title
st.set_page_config(page_title="Hack Club Fractal Generator", layout="centered")
st.title("🌌 Hack Club Fractal Explorer")
st.write("Adjust parameters to dynamically compile the Julia Fractal formula.")

# 2. Interactive Input Controls
width, height = 600, 450

col1, col2, col3 = st.columns(3)
with col1:
    preset = st.selectbox(
        "Shape Preset", 
        ["Sea Horse", "Sieving Galaxies", "Classic Dendrite", "Custom"]
    )
with col2:
    max_iterations = st.slider("Detail Depth", min_value=50, max_value=300, value=200, step=10)
with col3:
    color_theme = st.selectbox("Color Profile", ["Cosmic Neon", "Solar Flare", "Monochrome"])

# Map coordinates based on user preset selection
if preset == "Sea Horse":
    real_val, imag_val = -0.74543, 0.11301
elif preset == "Sieving Galaxies":
    real_val, imag_val = 0.28, 0.008
elif preset == "Classic Dendrite":
    real_val, imag_val = -0.4, 0.6
else:
    real_val = st.number_input("Real Component (Cr)", value=-0.74543, step=0.01, format="%.5f")
    imag_val = st.number_input("Imaginary Component (Ci)", value=0.11301, step=0.01, format="%.5f")

c = complex(real_val, imag_val)

# 3. Execution & Image Generation
if st.button("Generate Matrix Grid", type="primary", use_container_width=True):
    with st.spinner("Calculating mathematical infinity plane..."):
        img = Image.new("RGB", (width, height), "white")
        pixels = img.load()

        for i in range(width):
            for y in range(height):
                # Map standard coordinates to complex boundary plane
                zi = (i / width) * 3 - 1.5
                zy = (y / height) * 2 - 1.0 
                z = complex(zi, zy)
                
                count = 0
                while abs(z) < 2 and count < max_iterations:
                    z = z**2 + c
                    count += 1
                    
                # Color Vector Mapping Engine
                if count == max_iterations:
                    pixels[i, y] = (0, 0, 0)
                else:
                    if color_theme == "Cosmic Neon":
                        r = int((count * 5) % 256)
                        g = int((count * 2) % 256)
                        b = 150
                    elif color_theme == "Solar Flare":
                        r = 240
                        g = int((count * 7) % 256)
                        b = int((count * 2) % 256)
                    else:  # Monochrome
                        gray = int((count * 255 / max_iterations) % 256)
                        r, g, b = gray, gray, gray
                        
                    pixels[i, y] = (r, g, b)

        # Output Visual Result
        st.image(img, caption=f"Julia Set Matrix: Z^2 + ({c.real} + {c.imag}i)", use_container_width=True)
