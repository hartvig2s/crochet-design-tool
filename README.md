# Crochet Design Tool - Streamlit App

A Streamlit application wrapping the React-based Crochet Tote Bag Design Tool.

## 🚀 Quick Start

### Local Development

1. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the app**:
   ```bash
   streamlit run streamlit_app.py
   ```

3. **Open in browser**:
   - The app will open at `http://localhost:8501`

### Deploy to Streamlit Cloud

1. **Push to GitHub**:
   - Create a new repository
   - Upload the `streamlit_app/` folder contents

2. **Deploy on Streamlit Cloud**:
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Connect your GitHub repository
   - Set the main file path to `streamlit_app.py`
   - Deploy!

## 📁 Project Structure

```
streamlit_app/
├── streamlit_app.py          # Main Streamlit application
├── requirements.txt          # Python dependencies
├── README.md                # This file
└── crochet_component/       # Custom Streamlit component
    ├── __init__.py         # Component wrapper
    └── frontend/           # Built React app
        ├── index.html
        ├── assets/
        └── ...
```

## 🎯 Features

- **Full React App**: Complete crochet design functionality
- **Streamlit Integration**: Native Streamlit sidebar and styling
- **Responsive Design**: Works on desktop and mobile
- **Easy Deployment**: One-click Streamlit Cloud deployment

## 🛠 Development

### Updating the React Component

If you make changes to the React app:

1. **Rebuild React app**:
   ```bash
   cd /path/to/react/app
   npm run build
   ```

2. **Copy to component**:
   ```bash
   cp -r dist/* ../streamlit_app/crochet_component/frontend/
   ```

3. **Restart Streamlit**:
   ```bash
   streamlit run streamlit_app.py
   ```

### Component Communication

The React component can communicate with Streamlit by calling:
```javascript
window.parent.postMessage({ type: "streamlit:setComponentValue", value: data }, "*");
```

## 📝 Notes

- The component runs in production mode (static files)
- All React functionality is preserved
- Streamlit handles authentication, sharing, and deployment
- Component data can be accessed in Python for further processing