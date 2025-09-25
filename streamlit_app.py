import streamlit as st
import streamlit.components.v1 as components

# Set page config
st.set_page_config(
    page_title="Crochet Tote Bag Design Tool",
    page_icon="🧶",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS to remove default Streamlit padding and margins for full-width component
st.markdown("""
<style>
    .main .block-container {
        padding-top: 1rem;
        padding-right: 1rem;
        padding-left: 1rem;
        padding-bottom: 1rem;
        max-width: none;
    }

    /* Hide Streamlit header and footer */
    header[data-testid="stHeader"] {
        height: 0;
        display: none;
    }

    footer {
        display: none;
    }

    /* Full height for the component */
    .element-container iframe {
        height: 100vh !important;
    }
</style>
""", unsafe_allow_html=True)

# App title and description
st.title("🧶 Crochet Tote Bag Design Tool")
st.markdown("""
**Create custom filet crochet patterns for tote bags**

- 🎨 Custom Grid Design: 20-200cm with 1cm resolution
- 🎯 Drag & Drop Interface: Place motifs and images
- 📐 Automatic Pattern Generation: Filet crochet charts
- 🧶 Yarn Calculator: Precise skein requirements
- 📄 Export Options: PDF patterns and text files
""")

st.markdown("---")

# Create the component using direct HTML
st.write("### Crochet Design Tool")

# Read the HTML content directly
import os
html_path = os.path.join("crochet_component", "frontend", "index.html")

if os.path.exists(html_path):
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Use Streamlit's built-in HTML component
    component_data = components.html(html_content, height=400, scrolling=True)

else:
    st.error(f"HTML file not found at: {html_path}")
    component_data = None

# Display any data returned from the component
if component_data is not None:
    st.subheader("Component Data")
    st.json(component_data)

# Sidebar with additional information
with st.sidebar:
    st.header("About")
    st.markdown("""
    This tool helps you create custom crochet tote bag patterns using filet crochet technique.

    **How to use:**
    1. Click "New Project" to start
    2. Set your bag dimensions
    3. Upload images or create text motifs
    4. Drag and drop onto the grid
    5. Use manual fill tool for details
    6. Export your pattern

    **Features:**
    - Dual-side design (front & back)
    - Manual cell filling
    - Automatic yarn calculations
    - Pattern export (text format)
    """)

    st.header("Tips")
    st.markdown("""
    - Use 125% grid zoom for optimal viewing
    - Click between sides to switch active area
    - Red borders indicate manual fills
    - Blue borders show placed motifs
    - Overlapping motifs merge automatically
    """)