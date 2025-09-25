import streamlit as st
import os

# Test basic Streamlit functionality
st.title("Component Test")

# Check if component files exist
component_dir = "crochet_component/frontend"
index_path = os.path.join(component_dir, "index.html")
assets_dir = os.path.join(component_dir, "assets")

st.write("## File Check")
st.write(f"Index file exists: {os.path.exists(index_path)}")
st.write(f"Assets dir exists: {os.path.exists(assets_dir)}")

if os.path.exists(assets_dir):
    assets = os.listdir(assets_dir)
    st.write(f"Assets: {assets}")

if os.path.exists(index_path):
    with open(index_path, 'r') as f:
        content = f.read()
    st.write("## Index.html content:")
    st.code(content, language="html")

# Try to import the component
try:
    from crochet_component import crochet_design_tool
    st.write("✅ Component import successful")

    # Try to use the component
    st.write("## Component Test")
    result = crochet_design_tool(key="test")
    st.write(f"Component result: {result}")

except Exception as e:
    st.write(f"❌ Component import failed: {e}")
    import traceback
    st.code(traceback.format_exc())