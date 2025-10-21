# HoloLearn

## Project Description
HoloLearn is an innovative educational software designed to simulate 3D holographic projections, making learning more immersive and interactive. The platform allows users to browse and view holographic models of educational subjects, including biology (e.g., human heart, cell structure, DNA) and astronomy (e.g., solar system). By leveraging video-based simulations, HoloLearn transforms traditional learning into an engaging experience where users can visualize complex concepts in a three-dimensional, floating hologram format using a simple DIY pyramid projector.

The application provides a catalog of pre-built demos and supports user-uploaded videos to create custom hologram previews. It aims to enhance educational outcomes by combining technology with hands-on visualization, suitable for students, educators, and enthusiasts interested in interactive science education.

## Technical Stack
- **Programming Language**: Python
- **Framework**: Streamlit (for building the web-based user interface)
- **Frontend Styling**: HTML and CSS (embedded within Streamlit for custom UI components like headers, galleries, and hologram projection areas)
- **Video Handling**: Base64 encoding for embedding MP4/WebM videos directly into the app
- **Libraries**: 
  - `streamlit` for the core app functionality
  - `pathlib` for file path management
  - `base64` for video data encoding
  - `textwrap` for HTML string formatting
- **Deployment**: Runs as a local Streamlit app, with potential for cloud deployment (e.g., via Streamlit Cloud or Heroku)

## Prototype
The current prototype is a fully functional Streamlit web application that serves as a proof-of-concept for HoloLearn.Link : https://hololearn.streamlit.app/ 
It includes:
- A YouTube-like header with a search bar for topic exploration.
- A gallery of educational demos (e.g., Human Heart, Cell Structure, Solar System, DNA Structure).
- An upload feature for users to provide their own MP4/WebM videos.
- A hologram preview generator that displays videos in a 4-panel (2x2) grid layout, optimized for pyramid projection. This simulates the hologram effect by mirroring and flipping video quadrants.
- Interactive elements such as buttons for selecting demos and building previews.

The prototype demonstrates the core functionality of browsing, uploading, and viewing holographic simulations. It uses placeholder videos (e.g., Atom.mp4) for demos and provides instructions for creating real holograms with a transparent pyramid. Future iterations could integrate 3D modeling libraries like Three.js or AR/VR frameworks for more advanced projections.

## Sample Display
<image src="Videos/hologramdisplay.jpg">
<image src="Videos/hh.jpg">
