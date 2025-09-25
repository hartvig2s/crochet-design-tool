# Advanced Crochet Design Tool - Complete HTML implementation with all features
CROCHET_DESIGN_ADVANCED_HTML = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Advanced Crochet Design Tool</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #f5f7fa;
            height: 100vh;
            overflow: hidden;
        }

        .app {
            display: flex;
            flex-direction: column;
            height: 100vh;
        }

        .header {
            background: white;
            padding: 1rem 2rem;
            border-bottom: 1px solid #e0e0e0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .header h1 {
            color: #2c3e50;
            font-size: 1.5rem;
            margin: 0;
        }

        .header-actions {
            display: flex;
            gap: 1rem;
        }

        .main-content {
            flex: 1;
            display: grid;
            grid-template-columns: 300px 1fr 280px;
            gap: 1rem;
            padding: 1rem;
            overflow: hidden;
        }

        .sidebar {
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            display: flex;
            flex-direction: column;
            overflow-y: auto;
        }

        .design-area {
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            display: flex;
            flex-direction: column;
            overflow: hidden;
        }

        .panel-section {
            padding: 1.5rem;
            border-bottom: 1px solid #e0e0e0;
        }

        .panel-section:last-child {
            border-bottom: none;
        }

        .panel-section h3 {
            margin-bottom: 1rem;
            color: #2c3e50;
            font-size: 1.1rem;
        }

        .form-group {
            margin-bottom: 1rem;
        }

        .form-group label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: 500;
            color: #2c3e50;
        }

        .form-group input, .form-group select {
            width: 100%;
            padding: 0.5rem;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 1rem;
        }

        .form-group input:focus, .form-group select:focus {
            outline: none;
            border-color: #3498db;
            box-shadow: 0 0 0 2px rgba(52, 152, 219, 0.2);
        }

        .form-row {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1rem;
        }

        .btn {
            padding: 0.75rem 1.5rem;
            border: none;
            border-radius: 4px;
            font-size: 1rem;
            cursor: pointer;
            font-weight: 500;
            transition: all 0.2s;
            text-align: center;
            display: inline-block;
            text-decoration: none;
        }

        .btn:disabled {
            opacity: 0.6;
            cursor: not-allowed;
        }

        .btn-primary {
            background: #3498db;
            color: white;
        }

        .btn-primary:hover:not(:disabled) {
            background: #2980b9;
            transform: translateY(-2px);
        }

        .btn-secondary {
            background: #95a5a6;
            color: white;
        }

        .btn-secondary:hover:not(:disabled) {
            background: #7f8c8d;
        }

        .btn-success {
            background: #27ae60;
            color: white;
        }

        .btn-success:hover:not(:disabled) {
            background: #219a52;
        }

        .btn-small {
            padding: 0.5rem 1rem;
            font-size: 0.9rem;
        }

        .side-switcher {
            display: flex;
            gap: 0.5rem;
            margin-bottom: 1rem;
        }

        .side-switcher .btn {
            flex: 1;
            padding: 0.5rem;
            font-size: 0.9rem;
        }

        .side-switcher .btn.active {
            background: #3498db;
            color: white;
        }

        .side-switcher .btn:not(.active) {
            background: #ecf0f1;
            color: #7f8c8d;
        }

        .grid-container {
            flex: 1;
            padding: 1rem;
            overflow: auto;
            position: relative;
        }

        .grid-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1rem;
            padding: 0.5rem;
            background: #f8f9fa;
            border-radius: 4px;
        }

        .zoom-controls {
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .zoom-slider {
            width: 100px;
        }

        .grid {
            display: inline-block;
            border: 2px solid #333;
            background: white;
            transform-origin: top left;
        }

        .grid-row {
            display: flex;
        }

        .grid-cell {
            width: 15px;
            height: 15px;
            border: 1px solid #ddd;
            cursor: pointer;
            transition: all 0.1s;
            position: relative;
        }

        .grid-cell:hover {
            border-color: #3498db;
            z-index: 10;
        }

        .grid-cell.filled {
            background: #333;
        }

        .grid-cell.manual-fill {
            background: #e74c3c;
            border-color: #c0392b;
        }

        .grid-cell.has-motif {
            border: 2px solid #3498db;
            background: rgba(52, 152, 219, 0.3);
        }

        .motif-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(80px, 1fr));
            gap: 0.5rem;
        }

        .motif-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 0.25rem;
            padding: 0.75rem;
            border: 2px solid #e0e0e0;
            border-radius: 6px;
            cursor: pointer;
            transition: all 0.2s;
            text-align: center;
            background: white;
        }

        .motif-item:hover {
            border-color: #3498db;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(52, 152, 219, 0.3);
        }

        .motif-item.selected {
            border-color: #3498db;
            background: #f0f8ff;
        }

        .motif-preview {
            font-size: 1.5rem;
            width: 40px;
            height: 40px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: #f8f9fa;
            border-radius: 4px;
        }

        .motif-item span {
            font-size: 0.75rem;
            color: #2c3e50;
            font-weight: 500;
        }

        .tool-group {
            margin-bottom: 1.5rem;
        }

        .tool-group h4 {
            margin-bottom: 0.75rem;
            color: #2c3e50;
            font-size: 1rem;
        }

        .tool-buttons {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
        }

        .tool-btn {
            padding: 0.5rem 1rem;
            border: 1px solid #ddd;
            border-radius: 4px;
            background: white;
            cursor: pointer;
            font-size: 0.9rem;
            transition: all 0.2s;
            flex: 1;
            text-align: center;
        }

        .tool-btn:hover {
            background: #f8f9fa;
            border-color: #3498db;
        }

        .tool-btn.active {
            background: #3498db;
            color: white;
            border-color: #3498db;
        }

        .pattern-stats {
            background: #f8f9fa;
            border-radius: 4px;
            padding: 1rem;
        }

        .stat-row {
            display: flex;
            justify-content: space-between;
            margin-bottom: 0.5rem;
            font-size: 0.9rem;
        }

        .stat-row:last-child {
            margin-bottom: 0;
        }

        .stat-label {
            color: #7f8c8d;
        }

        .stat-value {
            font-weight: 600;
            color: #2c3e50;
        }

        .upload-area {
            border: 2px dashed #bdc3c7;
            border-radius: 4px;
            padding: 2rem;
            text-align: center;
            cursor: pointer;
            transition: all 0.2s;
            margin-bottom: 1rem;
        }

        .upload-area:hover {
            border-color: #3498db;
            background: rgba(52, 152, 219, 0.05);
        }

        .upload-area.dragover {
            border-color: #27ae60;
            background: rgba(39, 174, 96, 0.1);
        }

        .custom-text-input {
            margin-bottom: 1rem;
        }

        .custom-text-input textarea {
            width: 100%;
            min-height: 100px;
            padding: 0.5rem;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 0.9rem;
            resize: vertical;
        }

        .welcome-screen {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100%;
            text-align: center;
            color: #7f8c8d;
        }

        .welcome-screen h2 {
            margin-bottom: 1rem;
            color: #2c3e50;
        }

        .error {
            color: #e74c3c;
            font-size: 0.9rem;
            margin-top: 0.25rem;
        }

        .success {
            color: #27ae60;
            font-size: 0.9rem;
            margin-top: 0.25rem;
        }

        .hidden {
            display: none;
        }

        .export-options {
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
        }

        .placed-motif {
            position: absolute;
            border: 2px solid #3498db;
            background: rgba(52, 152, 219, 0.2);
            pointer-events: none;
            z-index: 20;
        }

        .motif-controls {
            position: absolute;
            top: -30px;
            right: -30px;
            display: flex;
            gap: 2px;
            z-index: 30;
        }

        .motif-control-btn {
            width: 20px;
            height: 20px;
            border-radius: 50%;
            border: 2px solid white;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 12px;
            font-weight: bold;
            color: white;
        }

        .remove-btn {
            background: #e74c3c;
        }

        .resize-btn {
            background: #f39c12;
        }

        .pattern-export {
            background: white;
            border: 1px solid #ddd;
            border-radius: 4px;
            padding: 1rem;
            font-family: monospace;
            font-size: 0.8rem;
            white-space: pre;
            max-height: 200px;
            overflow-y: auto;
            margin-top: 1rem;
        }

        @media (max-width: 1200px) {
            .main-content {
                grid-template-columns: 1fr;
                grid-template-rows: auto 1fr auto;
            }

            .sidebar {
                max-height: 200px;
                overflow-y: auto;
            }
        }
    </style>
</head>
<body>
    <div class="app">
        <div class="header">
            <h1>🧶 Advanced Crochet Design Tool</h1>
            <div class="header-actions">
                <button class="btn btn-secondary btn-small" onclick="newProject()">New Project</button>
                <button class="btn btn-success btn-small" onclick="saveProject()">Save Project</button>
            </div>
        </div>

        <div class="main-content">
            <!-- Left Sidebar: Project Settings & Motifs -->
            <div class="sidebar">
                <div class="panel-section">
                    <h3>Project Settings</h3>
                    <div class="form-group">
                        <label for="project-name">Project Name</label>
                        <input type="text" id="project-name" placeholder="My Crochet Project" value="Tote Bag Design">
                    </div>

                    <div class="form-row">
                        <div class="form-group">
                            <label for="grid-width">Width (cm)</label>
                            <input type="number" id="grid-width" min="8" max="200" value="30">
                        </div>
                        <div class="form-group">
                            <label for="grid-height">Height (cm)</label>
                            <input type="number" id="grid-height" min="8" max="200" value="35">
                        </div>
                    </div>

                    <div id="validation-errors"></div>

                    <button class="btn btn-primary" onclick="createProject()" style="width: 100%; margin-top: 1rem;">
                        Create/Update Project
                    </button>
                </div>

                <div class="panel-section">
                    <h3>Motif Library</h3>

                    <!-- Upload Custom Image -->
                    <div class="upload-area" onclick="document.getElementById('image-upload').click()">
                        <input type="file" id="image-upload" accept="image/*" style="display: none;" onchange="uploadImage(event)">
                        <p>📸 Click to upload image</p>
                        <p style="font-size: 0.8rem; color: #7f8c8d;">JPG, PNG supported</p>
                    </div>

                    <!-- Custom Text Motif -->
                    <div class="custom-text-input">
                        <textarea id="custom-text" placeholder="Enter text for custom motif..."></textarea>
                        <button class="btn btn-success btn-small" onclick="createTextMotif()" style="width: 100%;">Create Text Motif</button>
                    </div>

                    <!-- Pre-built Motifs -->
                    <h4>Quick Motifs</h4>
                    <div class="motif-grid" id="motif-library">
                        <!-- Motifs will be populated by JavaScript -->
                    </div>
                </div>
            </div>

            <!-- Center: Design Canvas -->
            <div class="design-area">
                <div id="welcome-screen" class="welcome-screen">
                    <h2>Welcome to Advanced Crochet Design Tool</h2>
                    <p>Create your project settings and start designing your dual-sided crochet tote bag pattern.</p>
                    <p>✨ Features: Dual-side design, motif library, image upload, pattern export</p>
                </div>

                <div id="design-workspace" class="hidden">
                    <!-- Side Switcher -->
                    <div class="grid-header">
                        <div class="side-switcher">
                            <button class="btn active" onclick="switchSide('front')" data-side="front">Front Side</button>
                            <button class="btn" onclick="switchSide('back')" data-side="back">Back Side</button>
                        </div>

                        <div class="zoom-controls">
                            <label>Zoom:</label>
                            <input type="range" class="zoom-slider" min="0.5" max="2" step="0.1" value="1" onchange="setZoom(this.value)">
                            <span id="zoom-display">100%</span>
                        </div>
                    </div>

                    <div class="grid-container" id="grid-container">
                        <div id="grid" class="grid"></div>
                        <!-- Placed motifs will be added here -->
                    </div>
                </div>
            </div>

            <!-- Right Sidebar: Tools & Stats -->
            <div class="sidebar">
                <div class="panel-section">
                    <h3>Drawing Tools</h3>

                    <div class="tool-group">
                        <h4>Basic Tools</h4>
                        <div class="tool-buttons">
                            <button class="tool-btn active" onclick="setTool('fill')" data-tool="fill">Fill</button>
                            <button class="tool-btn" onclick="setTool('erase')" data-tool="erase">Erase</button>
                        </div>
                    </div>

                    <div class="tool-group">
                        <h4>Manual Fill</h4>
                        <div class="tool-buttons">
                            <button class="tool-btn" onclick="setTool('manual-fill')" data-tool="manual-fill">Manual Fill</button>
                            <button class="tool-btn" onclick="clearManualFills()">Clear Manual</button>
                        </div>
                    </div>

                    <div class="tool-group">
                        <h4>Quick Actions</h4>
                        <div class="tool-buttons">
                            <button class="tool-btn" onclick="clearCurrentSide()">Clear Side</button>
                            <button class="tool-btn" onclick="mirrorSide()">Mirror to Other</button>
                        </div>
                    </div>
                </div>

                <div class="panel-section">
                    <h3>Pattern Statistics</h3>
                    <div class="pattern-stats">
                        <div class="stat-row">
                            <span class="stat-label">Grid Size:</span>
                            <span class="stat-value" id="grid-size">30 × 35</span>
                        </div>
                        <div class="stat-row">
                            <span class="stat-label">Current Side:</span>
                            <span class="stat-value" id="current-side-display">Front</span>
                        </div>
                        <div class="stat-row">
                            <span class="stat-label">Filled Cells:</span>
                            <span class="stat-value" id="filled-count">0</span>
                        </div>
                        <div class="stat-row">
                            <span class="stat-label">Manual Fills:</span>
                            <span class="stat-value" id="manual-count">0</span>
                        </div>
                        <div class="stat-row">
                            <span class="stat-label">Placed Motifs:</span>
                            <span class="stat-value" id="motif-count">0</span>
                        </div>
                        <div class="stat-row">
                            <span class="stat-label">Total Stitches:</span>
                            <span class="stat-value" id="stitch-count">0</span>
                        </div>
                        <div class="stat-row">
                            <span class="stat-label">Yarn Estimate:</span>
                            <span class="stat-value" id="yarn-estimate">1 skein</span>
                        </div>
                    </div>
                </div>

                <div class="panel-section">
                    <h3>Export Pattern</h3>
                    <div class="export-options">
                        <button class="btn btn-primary" onclick="generatePattern()" style="width: 100%;">Generate Pattern</button>
                        <button class="btn btn-secondary" onclick="exportText()" style="width: 100%;">Export as Text</button>
                        <button class="btn btn-success" onclick="exportPDF()" style="width: 100%;">Export as PDF</button>
                    </div>

                    <div id="pattern-preview" class="pattern-export hidden">
                        <!-- Generated pattern will appear here -->
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        // Global state
        let currentTool = 'fill';
        let currentSide = 'front';
        let gridWidth = 30;
        let gridHeight = 35;
        let zoom = 1;
        let isDrawing = false;
        let selectedMotif = null;

        // Grid data for both sides
        let gridData = {
            front: [],
            back: []
        };

        // Manual fill data (red cells)
        let manualFills = {
            front: [],
            back: []
        };

        // Placed motifs
        let placedMotifs = {
            front: [],
            back: []
        };

        // Motif library
        const motifLibrary = [
            { name: 'Heart', symbol: '♥', pattern: [[0,1,0,1,0],[1,1,1,1,1],[1,1,1,1,1],[0,1,1,1,0],[0,0,1,0,0]] },
            { name: 'Star', symbol: '★', pattern: [[0,0,1,0,0],[0,1,1,1,0],[1,1,1,1,1],[0,1,1,1,0],[0,0,1,0,0]] },
            { name: 'Flower', symbol: '🌸', pattern: [[0,1,0,1,0],[1,0,1,0,1],[0,1,1,1,0],[1,0,1,0,1],[0,1,0,1,0]] },
            { name: 'Diamond', symbol: '♦', pattern: [[0,0,1,0,0],[0,1,0,1,0],[1,0,0,0,1],[0,1,0,1,0],[0,0,1,0,0]] },
            { name: 'Arrow', symbol: '→', pattern: [[0,0,1,0,0],[0,0,1,1,0],[1,1,1,1,1],[0,0,1,1,0],[0,0,1,0,0]] },
            { name: 'Cross', symbol: '✚', pattern: [[0,0,1,0,0],[0,0,1,0,0],[1,1,1,1,1],[0,0,1,0,0],[0,0,1,0,0]] }
        ];

        // Initialize the app
        function initializeApp() {
            populateMotifLibrary();
            updateStats();
            updateHeight();
        }

        function populateMotifLibrary() {
            const container = document.getElementById('motif-library');
            container.innerHTML = '';

            motifLibrary.forEach((motif, index) => {
                const motifElement = document.createElement('div');
                motifElement.className = 'motif-item';
                motifElement.onclick = () => selectMotif(motif, index);

                motifElement.innerHTML = `
                    <div class="motif-preview">${motif.symbol}</div>
                    <span>${motif.name}</span>
                `;

                container.appendChild(motifElement);
            });
        }

        function selectMotif(motif, index) {
            // Remove previous selection
            document.querySelectorAll('.motif-item').forEach(item => item.classList.remove('selected'));

            // Select current motif
            document.querySelectorAll('.motif-item')[index].classList.add('selected');
            selectedMotif = motif;

            // Enable motif placement tool
            setTool('place-motif');
        }

        function setTool(tool) {
            currentTool = tool;
            document.querySelectorAll('.tool-btn[data-tool]').forEach(btn => {
                btn.classList.remove('active');
            });
            const toolBtn = document.querySelector(`[data-tool="${tool}"]`);
            if (toolBtn) {
                toolBtn.classList.add('active');
            }
        }

        function switchSide(side) {
            currentSide = side;
            document.querySelectorAll('.side-switcher .btn').forEach(btn => {
                btn.classList.remove('active');
            });
            document.querySelector(`[data-side="${side}"]`).classList.add('active');

            renderGrid();
            updateStats();
        }

        function setZoom(value) {
            zoom = parseFloat(value);
            document.getElementById('zoom-display').textContent = Math.round(zoom * 100) + '%';
            const grid = document.getElementById('grid');
            if (grid) {
                grid.style.transform = `scale(${zoom})`;
            }
        }

        function createProject() {
            const name = document.getElementById('project-name').value.trim();
            const width = parseInt(document.getElementById('grid-width').value);
            const height = parseInt(document.getElementById('grid-height').value);
            const errors = document.getElementById('validation-errors');

            // Clear previous errors
            errors.innerHTML = '';

            // Validate input
            let hasErrors = false;
            if (!name) {
                errors.innerHTML += '<div class="error">Project name is required</div>';
                hasErrors = true;
            }
            if (width < 8 || width > 200) {
                errors.innerHTML += '<div class="error">Width must be between 8 and 200 cm</div>';
                hasErrors = true;
            }
            if (height < 8 || height > 200) {
                errors.innerHTML += '<div class="error">Height must be between 8 and 200 cm</div>';
                hasErrors = true;
            }

            if (hasErrors) return;

            // Update grid dimensions
            gridWidth = width;
            gridHeight = height;

            // Initialize grid data for both sides
            initializeGridData();

            // Show design workspace
            document.getElementById('welcome-screen').classList.add('hidden');
            document.getElementById('design-workspace').classList.remove('hidden');

            // Render the grid
            renderGrid();
            updateStats();

            errors.innerHTML = '<div class="success">Project created successfully!</div>';

            // Send project data to Streamlit
            sendToStreamlit({
                action: 'project_created',
                project: { name, width, height },
                timestamp: new Date().toISOString()
            });
        }

        function initializeGridData() {
            gridData.front = Array(gridHeight).fill().map(() => Array(gridWidth).fill(false));
            gridData.back = Array(gridHeight).fill().map(() => Array(gridWidth).fill(false));
            manualFills.front = Array(gridHeight).fill().map(() => Array(gridWidth).fill(false));
            manualFills.back = Array(gridHeight).fill().map(() => Array(gridWidth).fill(false));
            placedMotifs.front = [];
            placedMotifs.back = [];
        }

        function renderGrid() {
            const gridElement = document.getElementById('grid');
            gridElement.innerHTML = '';

            for (let y = 0; y < gridHeight; y++) {
                const row = document.createElement('div');
                row.className = 'grid-row';

                for (let x = 0; x < gridWidth; x++) {
                    const cell = document.createElement('div');
                    let cellClass = 'grid-cell';

                    if (gridData[currentSide][y][x]) {
                        cellClass += ' filled';
                    }
                    if (manualFills[currentSide][y][x]) {
                        cellClass += ' manual-fill';
                    }

                    cell.className = cellClass;
                    cell.dataset.x = x;
                    cell.dataset.y = y;

                    cell.addEventListener('mousedown', (e) => {
                        isDrawing = true;
                        handleCellInteraction(x, y, e);
                        e.preventDefault();
                    });

                    cell.addEventListener('mouseenter', (e) => {
                        if (isDrawing && (currentTool === 'fill' || currentTool === 'erase' || currentTool === 'manual-fill')) {
                            handleCellInteraction(x, y, e);
                        }
                    });

                    cell.addEventListener('click', (e) => {
                        if (currentTool === 'place-motif' && selectedMotif) {
                            placeMotif(x, y);
                        }
                    });

                    row.appendChild(cell);
                }

                gridElement.appendChild(row);
            }

            // Add global mouse up listener
            document.addEventListener('mouseup', () => {
                isDrawing = false;
            });

            // Apply zoom
            gridElement.style.transform = `scale(${zoom})`;
        }

        function handleCellInteraction(x, y, e) {
            if (currentTool === 'fill') {
                gridData[currentSide][y][x] = true;
                manualFills[currentSide][y][x] = false; // Clear manual fill if present
            } else if (currentTool === 'erase') {
                gridData[currentSide][y][x] = false;
                manualFills[currentSide][y][x] = false;
            } else if (currentTool === 'manual-fill') {
                manualFills[currentSide][y][x] = true;
                gridData[currentSide][y][x] = true; // Manual fill implies filled
            }

            renderGrid();
            updateStats();
        }

        function placeMotif(x, y) {
            if (!selectedMotif) return;

            const motif = {
                id: Date.now(),
                name: selectedMotif.name,
                pattern: selectedMotif.pattern,
                x: x,
                y: y,
                size: 1
            };

            placedMotifs[currentSide].push(motif);
            applyMotifToGrid(motif);
            renderGrid();
            updateStats();

            // Clear selection
            selectedMotif = null;
            document.querySelectorAll('.motif-item').forEach(item => item.classList.remove('selected'));
            setTool('fill');
        }

        function applyMotifToGrid(motif) {
            const pattern = motif.pattern;
            const startX = motif.x;
            const startY = motif.y;

            for (let py = 0; py < pattern.length; py++) {
                for (let px = 0; px < pattern[py].length; px++) {
                    const gridX = startX + px;
                    const gridY = startY + py;

                    if (gridX >= 0 && gridX < gridWidth && gridY >= 0 && gridY < gridHeight) {
                        if (pattern[py][px]) {
                            gridData[currentSide][gridY][gridX] = true;
                        }
                    }
                }
            }
        }

        function clearCurrentSide() {
            gridData[currentSide] = Array(gridHeight).fill().map(() => Array(gridWidth).fill(false));
            manualFills[currentSide] = Array(gridHeight).fill().map(() => Array(gridWidth).fill(false));
            placedMotifs[currentSide] = [];
            renderGrid();
            updateStats();
        }

        function clearManualFills() {
            manualFills[currentSide] = Array(gridHeight).fill().map(() => Array(gridWidth).fill(false));
            renderGrid();
            updateStats();
        }

        function mirrorSide() {
            const otherSide = currentSide === 'front' ? 'back' : 'front';
            gridData[otherSide] = gridData[currentSide].map(row => [...row]);
            manualFills[otherSide] = manualFills[currentSide].map(row => [...row]);
            placedMotifs[otherSide] = [...placedMotifs[currentSide]];
            updateStats();
        }

        function updateStats() {
            const frontFilled = gridData.front.flat().filter(cell => cell).length;
            const backFilled = gridData.back.flat().filter(cell => cell).length;
            const currentFilled = gridData[currentSide].flat().filter(cell => cell).length;

            const frontManual = manualFills.front.flat().filter(cell => cell).length;
            const backManual = manualFills.back.flat().filter(cell => cell).length;
            const currentManual = manualFills[currentSide].flat().filter(cell => cell).length;

            const totalStitches = (frontFilled + backFilled) * 2; // Approximate
            const yarns = Math.ceil(totalStitches / 1000); // Very rough estimate

            document.getElementById('grid-size').textContent = `${gridWidth} × ${gridHeight}`;
            document.getElementById('current-side-display').textContent = currentSide.charAt(0).toUpperCase() + currentSide.slice(1);
            document.getElementById('filled-count').textContent = currentFilled;
            document.getElementById('manual-count').textContent = currentManual;
            document.getElementById('motif-count').textContent = placedMotifs[currentSide].length;
            document.getElementById('stitch-count').textContent = totalStitches;
            document.getElementById('yarn-estimate').textContent = `${yarns} skein${yarns !== 1 ? 's' : ''}`;
        }

        function generatePattern() {
            let pattern = `DUAL-SIDE CROCHET PATTERN\\n`;
            pattern += `Project: ${document.getElementById('project-name').value}\\n`;
            pattern += `Grid: ${gridWidth} × ${gridHeight}\\n\\n`;

            // Front side pattern
            pattern += `FRONT SIDE:\\n`;
            for (let y = 0; y < gridHeight; y++) {
                let row = '';
                for (let x = 0; x < gridWidth; x++) {
                    if (manualFills.front[y][x]) {
                        row += '●'; // Manual fill
                    } else if (gridData.front[y][x]) {
                        row += '█'; // Regular fill
                    } else {
                        row += '·'; // Empty
                    }
                }
                pattern += row + '\\n';
            }

            pattern += '\\nBACK SIDE:\\n';
            for (let y = 0; y < gridHeight; y++) {
                let row = '';
                for (let x = 0; x < gridWidth; x++) {
                    if (manualFills.back[y][x]) {
                        row += '●'; // Manual fill
                    } else if (gridData.back[y][x]) {
                        row += '█'; // Regular fill
                    } else {
                        row += '·'; // Empty
                    }
                }
                pattern += row + '\\n';
            }

            pattern += '\\nLEGEND:\\n█ = Chain space (filled)\\n· = Double crochet (open)\\n● = Manual fill (special stitch)';

            document.getElementById('pattern-preview').classList.remove('hidden');
            document.getElementById('pattern-preview').textContent = pattern;

            sendToStreamlit({
                action: 'pattern_generated',
                pattern: pattern,
                sides: {
                    front: { filled: gridData.front.flat().filter(cell => cell).length, manual: manualFills.front.flat().filter(cell => cell).length },
                    back: { filled: gridData.back.flat().filter(cell => cell).length, manual: manualFills.back.flat().filter(cell => cell).length }
                },
                timestamp: new Date().toISOString()
            });
        }

        function exportText() {
            generatePattern();
            const pattern = document.getElementById('pattern-preview').textContent;
            const blob = new Blob([pattern], { type: 'text/plain' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = `${document.getElementById('project-name').value || 'pattern'}.txt`;
            a.click();
        }

        function exportPDF() {
            alert('PDF export would require additional libraries. Use "Export as Text" for now.');
        }

        function uploadImage(event) {
            const file = event.target.files[0];
            if (!file) return;

            const reader = new FileReader();
            reader.onload = function(e) {
                const img = new Image();
                img.onload = function() {
                    // Convert image to pattern (simplified)
                    const canvas = document.createElement('canvas');
                    const ctx = canvas.getContext('2d');

                    const maxSize = 20; // Limit pattern size
                    const scale = Math.min(maxSize / img.width, maxSize / img.height);
                    const width = Math.floor(img.width * scale);
                    const height = Math.floor(img.height * scale);

                    canvas.width = width;
                    canvas.height = height;

                    ctx.drawImage(img, 0, 0, width, height);
                    const imageData = ctx.getImageData(0, 0, width, height);
                    const pattern = [];

                    for (let y = 0; y < height; y++) {
                        const row = [];
                        for (let x = 0; x < width; x++) {
                            const index = (y * width + x) * 4;
                            const r = imageData.data[index];
                            const g = imageData.data[index + 1];
                            const b = imageData.data[index + 2];
                            const brightness = (r + g + b) / 3;
                            row.push(brightness < 128 ? 1 : 0); // Convert to binary
                        }
                        pattern.push(row);
                    }

                    // Add to motif library
                    const customMotif = {
                        name: `Custom ${motifLibrary.length + 1}`,
                        symbol: '📷',
                        pattern: pattern
                    };
                    motifLibrary.push(customMotif);
                    populateMotifLibrary();
                };
                img.src = e.target.result;
            };
            reader.readAsDataURL(file);
        }

        function createTextMotif() {
            const text = document.getElementById('custom-text').value.trim();
            if (!text) return;

            // Simple text to pattern conversion (very basic)
            const lines = text.split('\\n').slice(0, 10); // Max 10 lines
            const pattern = lines.map(line => {
                return line.split('').slice(0, 20).map(char => char !== ' ' ? 1 : 0);
            });

            const customMotif = {
                name: `Text: ${text.substring(0, 10)}...`,
                symbol: '📝',
                pattern: pattern
            };
            motifLibrary.push(customMotif);
            populateMotifLibrary();
            document.getElementById('custom-text').value = '';
        }

        function newProject() {
            if (confirm('Start a new project? This will clear your current design.')) {
                document.getElementById('project-name').value = 'New Project';
                document.getElementById('grid-width').value = 30;
                document.getElementById('grid-height').value = 35;
                initializeGridData();
                document.getElementById('welcome-screen').classList.remove('hidden');
                document.getElementById('design-workspace').classList.add('hidden');
                updateStats();
            }
        }

        function saveProject() {
            const projectData = {
                name: document.getElementById('project-name').value,
                width: gridWidth,
                height: gridHeight,
                gridData: gridData,
                manualFills: manualFills,
                placedMotifs: placedMotifs
            };

            sendToStreamlit({
                action: 'project_saved',
                project: projectData,
                timestamp: new Date().toISOString()
            });

            alert('Project data sent to Streamlit! Check the component data section below.');
        }

        function sendToStreamlit(data) {
            window.parent.postMessage({
                type: "streamlit:setComponentValue",
                value: data
            }, "*");
        }

        // Set component height
        function updateHeight() {
            const height = Math.max(document.body.scrollHeight, 800);
            window.parent.postMessage({
                type: "streamlit:setFrameHeight",
                height: height
            }, "*");
        }

        // Initialize everything when page loads
        window.addEventListener('load', () => {
            initializeApp();
        });

        window.addEventListener('resize', updateHeight);
    </script>
</body>
</html>
'''