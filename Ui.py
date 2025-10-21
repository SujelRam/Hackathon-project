# app.py
import streamlit as st
import base64
import textwrap
from pathlib import Path

st.set_page_config(page_title="HoloLearn Player", layout="wide", page_icon="🔮")

# --- CSS / UI styling (YouTube-like header + hologram area) ---
st.markdown(
    """
    <style>
    /* page */
    .stApp { background-color: #000; color: #dff; }

    /* header */
    .header {
      display:flex;
      align-items:center;
      gap:12px;
      padding:10px 16px;
      border-bottom: 1px solid rgba(0,255,255,0.08);
    }
    .logo {
      font-weight:800;
      color: #00f6ff;
      font-size:20px;
      text-shadow: 0 0 8px rgba(0,255,255,0.12);
    }
    .search {
      flex:1;
      display:flex;
      justify-content:center;
    }
    .search input{
      width:70%;
      padding:10px 14px;
      border-radius:24px;
      border: 1px solid rgba(0,255,255,0.2);
      background: rgba(255,255,255,0.02);
      color: #dff;
    }

    /* gallery */
    .gallery { padding: 12px; display:flex; gap:12px; flex-wrap:wrap; }
    .thumb {
      width:220px;
      background: rgba(0,255,255,0.03);
      border-radius:8px;
      padding:8px;
      text-align:left;
      cursor:pointer;
    }
    .thumb:hover { transform: scale(1.02); box-shadow: 0 6px 18px rgba(0,255,255,0.05); }

    .thumb-title { color:#cfffff; font-weight:600; font-size:14px; margin-top:6px; }

    /* hologram projection area (4-panel) */
    .holo-wrap {
      display:flex;
      justify-content:center;
      padding:18px;
    }
    .holo-container {
      background: radial-gradient(circle at 50% 20%, rgba(0,255,255,0.04), rgba(0,0,0,0.6));
      border-radius:12px;
      padding:18px;
      border: 1px solid rgba(0,255,255,0.06);
      width:880px;
      max-width:95%;
    }
    .cross {
      display:grid;
      grid-template-columns: 1fr 1fr;
      gap:6px;
      align-items:center;
      justify-items:center;
    }
    video.holo {
      width:100%;
      height:240px;
      object-fit:cover;
      background: transparent;
      opacity:0.92;
      filter: drop-shadow(0 10px 20px rgba(0,255,255,0.04)) contrast(1.05) saturate(1.1);
      border-radius:6px;
      transform-origin:center;
    }
    /* small projection look */
    .projector-instructions { color: #9ff; font-size:13px; margin-top:10px; text-align:center; }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Header (YouTube-like) ---
st.markdown(
    f"""
    <div class="header">
      <div class="logo">HoloLearn</div>
      <div class="search">
        <input id="searchBox" placeholder="Search topics (e.g. 'Human heart', 'Solar system')" />
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")  # spacing

# --- Catalog ---
catalog = [
    {"id": "demo_cell", "title": "Cell Structure", "description": "Transparent cell layers with labels."},
    {"id": "demo_solar", "title": "Solar System (Hologram)", "description": "Mini solar system orbit model."},
    {"id": "demo_dna", "title": "DNA Structure", "description": "3D rotating double-helix DNA model."}
]

# --- Display catalog as gallery ---
st.markdown("<div class='gallery'>", unsafe_allow_html=True)
cols = st.columns([1,1,1])

for i, item in enumerate(catalog):
    with cols[i % 3]:
        if st.button(item["title"], key=item["id"]):
            st.session_state["selected"] = item["id"]
        st.markdown(
            f"""<div class="thumb">
                <div style="height:110px; display:flex; align-items:center; justify-content:center;">
                  <svg width="96" height="72" viewBox="0 0 96 72" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <rect x="0" y="0" width="96" height="72" rx="6" fill="rgba(0,255,255,0.06)"/>
                    <polygon points="36,18 36,54 62,36" fill="rgba(0,255,255,0.18)"/>
                  </svg>
                </div>
                <div class="thumb-title">{item['title']}</div>
                <div style="color:#aef; font-size:12px; margin-top:6px;">{item['description']}</div>
            </div>""",
            unsafe_allow_html=True,
        )
st.markdown("</div>", unsafe_allow_html=True)

# --- Upload area for user's video (mp4) ---
st.markdown("---")
st.markdown("### Upload or pick a video for hologram projection")
uploaded = st.file_uploader("Upload an MP4/WebM video (best if short and centered), or pick a demo below", type=["mp4","webm"])

# if user picks a catalog demo, use placeholder demo files (we do not ship sample mp4 here)
if "selected" in st.session_state and not uploaded:
    st.info("You selected a demo. Upload a video to preview on device, or pick a local holographic file.")
    # The app can't ship sample video bytes in this example; user should upload their mp4.
    st.write("Tip: You can find free hologram-ready demo videos on YouTube (search 'hologram pyramid video') and download one for testing.")

# --- Button to build hologram preview ---
build = st.button("🔮 Build Hologram Preview")

def make_data_url(file_bytes: bytes, mime="video/mp4"):
    b64 = base64.b64encode(file_bytes).decode()
    return f"data:{mime};base64,{b64}"

if build:
    if not uploaded and "selected" not in st.session_state:
        st.error("Please upload a video first (MP4 or WebM) or select a demo.")
    elif uploaded:
        # read bytes and prepare data URL
        data = uploaded.read()
        data_url = make_data_url(data, mime=uploaded.type or "video/mp4")

        # Create HTML for 4-view (2x2) layout suitable for hologram pyramid.
        # Many hologram pyramid videos use a cross layout; phones commonly play this and pyramid reflects each quadrant.
        html = textwrap.dedent(f"""
        <div class="holo-wrap">
          <div class="holo-container">
            <div style="text-align:center; color:#9ff; font-weight:600; margin-bottom:8px;">Hologram Preview — place pyramid at center of phone to project</div>
            <div class="cross">
              <!-- Top-left -->
              <video class="holo" src="{data_url}" autoplay loop muted playsinline controls></video>
              <!-- Top-right -->
              <video class="holo" src="{data_url}" autoplay loop muted playsinline controls style="transform: scaleX(-1);"></video>
              <!-- Bottom-left -->
              <video class="holo" src="{data_url}" autoplay loop muted playsinline controls style="transform: scaleY(-1);"></video>
              <!-- Bottom-right -->
              <video class="holo" src="{data_url}" autoplay loop muted playsinline controls style="transform: scaleX(-1) scaleY(-1);"></video>
            </div>
            <div class="projector-instructions">
              Place a transparent pyramid (made from acetate/plastic) at the center where the 4 corners meet.
              Then hold the phone face-up — the reflections create a floating hologram in the pyramid.
            </div>
          </div>
        </div>
        """)
        st.components.v1.html(html, height=700, scrolling=True)
    elif "selected" in st.session_state:
        # Use Atom.mp4 for Human Heart and Cell Structure demos
        if st.session_state["selected"] in ["demo_heart", "demo_cell"]:
            video_path = "Videos/Atom.mp4"
            try:
                with open(video_path, "rb") as f:
                    data = f.read()
                data_url = make_data_url(data, mime="video/mp4")

                # Create HTML for 4-view (2x2) layout
                html = textwrap.dedent(f"""
                <div class="holo-wrap">
                  <div class="holo-container">
                    <div style="text-align:center; color:#9ff; font-weight:600; margin-bottom:8px;">Hologram Preview — place pyramid at center of phone to project</div>
                    <div class="cross">
                      <!-- Top-left -->
                      <video class="holo" src="{data_url}" autoplay loop muted playsinline controls></video>
                      <!-- Top-right -->
                      <video class="holo" src="{data_url}" autoplay loop muted playsinline controls style="transform: scaleX(-1);"></video>
                      <!-- Bottom-left -->
                      <video class="holo" src="{data_url}" autoplay loop muted playsinline controls style="transform: scaleY(-1);"></video>
                      <!-- Bottom-right -->
                      <video class="holo" src="{data_url}" autoplay loop muted playsinline controls style="transform: scaleX(-1) scaleY(-1);"></video>
                    </div>
                    <div class="projector-instructions">
                      Place a transparent pyramid (made from acetate/plastic) at the center where the 4 corners meet.
                      Then hold the phone face-up — the reflections create a floating hologram in the pyramid.
                    </div>
                  </div>
                </div>
                """)
                st.components.v1.html(html, height=700, scrolling=True)
            except FileNotFoundError:
                st.error(f"Video file not found at {video_path}. Please ensure the file exists.")
            except Exception as e:
                st.error(f"Error loading video: {str(e)}")
        else:
            st.error("Demo video not available for this selection. Please upload a video.")

# --- Footer + short help + citation ---
st.markdown("---")
st.markdown(
    """
    **How this maps to a real pyramid projector**
    - The app displays the same video in four quadrants (mirrored), which is the format typical hologram pyramid videos use.
    - To view the hologram: make a small transparent pyramid (search "DIY hologram pyramid"), place it on the phone screen where the four videos meet, and dim lights.
    """
)


