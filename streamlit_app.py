import streamlit as st
import streamlit.components.v1 as components
import base64

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

# Create the component using embedded HTML
st.write("### Crochet Design Tool")

# Embed the HTML directly as a string to avoid file system issues
html_content = '''
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <title>Crochet Component</title>
</head>
<body>
  <div style="padding: 20px; font-family: sans-serif;">
    <h2 style="color: #262730;">🧶 Crochet Design Tool Component</h2>
    <div style="background: #f0f2f6; padding: 15px; border-radius: 8px; margin: 10px 0;">
      <p><strong>Status:</strong> ✅ Component loaded successfully!</p>
      <p><strong>Time:</strong> <span id="current-time"></span></p>
      <button onclick="sendTestData()" style="background: #ff4b4b; color: white; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer;">
        Send Test Data
      </button>
    </div>
    <div id="message" style="margin-top: 15px;"></div>
  </div>

  <script>
    // Update time
    document.getElementById('current-time').textContent = new Date().toLocaleString();

    function sendTestData() {
      const data = {
        action: "test_button_clicked",
        timestamp: new Date().toISOString(),
        status: "working"
      };

      // Send to Streamlit
      window.parent.postMessage({
        type: "streamlit:setComponentValue",
        value: data
      }, "*");

      document.getElementById('message').innerHTML =
        '<p style="color: green;">✅ Test data sent to Streamlit!</p>';
    }

    // Set component height
    function updateHeight() {
      const height = Math.max(document.body.scrollHeight, 250);
      window.parent.postMessage({
        type: "streamlit:setFrameHeight",
        height: height
      }, "*");
    }

    // Initialize
    window.addEventListener('load', updateHeight);
    window.addEventListener('resize', updateHeight);
  </script>
</body>
</html>
'''

# Use Streamlit's built-in HTML component with embedded content
component_data = components.html(html_content, height=300, scrolling=False)

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