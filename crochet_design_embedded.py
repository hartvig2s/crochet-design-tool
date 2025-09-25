# Embedded Crochet Design Tool - Complete HTML implementation
CROCHET_DESIGN_HTML = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Crochet Design Tool</title>
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
            padding: 1rem;
            border-bottom: 1px solid #e0e0e0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }

        .header h1 {
            color: #2c3e50;
            font-size: 1.5rem;
            margin: 0;
        }

        .main-content {
            flex: 1;
            display: flex;
            overflow: hidden;
        }

        .sidebar {
            width: 280px;
            background: white;
            border-right: 1px solid #e0e0e0;
            display: flex;
            flex-direction: column;
            overflow-y: auto;
        }

        .design-area {
            flex: 1;
            background: white;
            display: flex;
            flex-direction: column;
            overflow: hidden;
        }

        .project-form {
            padding: 1.5rem;
            border-bottom: 1px solid #e0e0e0;
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

        .form-group input {
            width: 100%;
            padding: 0.5rem;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 1rem;
        }

        .form-group input:focus {
            outline: none;
            border-color: #3498db;
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
            transition: background-color 0.2s;
        }

        .btn-primary {
            background: #3498db;
            color: white;
        }

        .btn-primary:hover {
            background: #2980b9;
        }

        .btn-secondary {
            background: #95a5a6;
            color: white;
        }

        .btn-secondary:hover {
            background: #7f8c8d;
        }

        .grid-container {
            flex: 1;
            padding: 1rem;
            overflow: auto;
        }

        .grid {
            display: inline-block;
            border: 2px solid #333;
            background: white;
        }

        .grid-row {
            display: flex;
        }

        .grid-cell {
            width: 20px;
            height: 20px;
            border: 1px solid #ddd;
            cursor: pointer;
            transition: background-color 0.1s;
        }

        .grid-cell:hover {
            background: #e3f2fd;
        }

        .grid-cell.filled {
            background: #333;
        }

        .grid-cell.preview {
            background: #ffeb3b;
        }

        .tools {
            padding: 1rem;
            border-bottom: 1px solid #e0e0e0;
        }

        .tool-group {
            margin-bottom: 1rem;
        }

        .tool-group h3 {
            margin-bottom: 0.5rem;
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

        .pattern-info {
            padding: 1rem;
            background: #f8f9fa;
        }

        .pattern-info h3 {
            margin-bottom: 1rem;
            color: #2c3e50;
        }

        .stat {
            display: flex;
            justify-content: space-between;
            margin-bottom: 0.5rem;
            font-size: 0.9rem;
        }

        .stat-label {
            color: #7f8c8d;
        }

        .stat-value {
            font-weight: 600;
            color: #2c3e50;
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

        .hidden {
            display: none;
        }
    </style>
</head>
<body>
    <div class="app">
        <div class="header">
            <h1>🧶 Crochet Design Tool</h1>
        </div>

        <div class="main-content">
            <div class="sidebar">
                <div class="project-form">
                    <h2 style="margin-bottom: 1rem; color: #2c3e50;">Project Settings</h2>

                    <div class="form-group">
                        <label for="project-name">Project Name</label>
                        <input type="text" id="project-name" placeholder="My Crochet Project" value="My Tote Bag">
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
                        Create Project
                    </button>
                </div>

                <div class="tools">
                    <div class="tool-group">
                        <h3>Drawing Tools</h3>
                        <div class="tool-buttons">
                            <button class="tool-btn active" onclick="setTool('fill')" data-tool="fill">Fill</button>
                            <button class="tool-btn" onclick="setTool('erase')" data-tool="erase">Erase</button>
                            <button class="tool-btn" onclick="clearGrid()" data-tool="clear">Clear All</button>
                        </div>
                    </div>

                    <div class="tool-group">
                        <h3>Quick Shapes</h3>
                        <div class="tool-buttons">
                            <button class="tool-btn" onclick="drawShape('rectangle')">Rectangle</button>
                            <button class="tool-btn" onclick="drawShape('circle')">Circle</button>
                            <button class="tool-btn" onclick="drawShape('heart')">Heart</button>
                        </div>
                    </div>
                </div>

                <div class="pattern-info">
                    <h3>Pattern Stats</h3>
                    <div class="stat">
                        <span class="stat-label">Grid Size:</span>
                        <span class="stat-value" id="grid-size">30 × 35</span>
                    </div>
                    <div class="stat">
                        <span class="stat-label">Filled Cells:</span>
                        <span class="stat-value" id="filled-count">0</span>
                    </div>
                    <div class="stat">
                        <span class="stat-label">Total Stitches:</span>
                        <span class="stat-value" id="stitch-count">0</span>
                    </div>
                    <div class="stat">
                        <span class="stat-label">Est. Yarn:</span>
                        <span class="stat-value" id="yarn-estimate">1 skein</span>
                    </div>

                    <button class="btn btn-secondary" onclick="exportPattern()" style="width: 100%; margin-top: 1rem;">
                        Export Pattern
                    </button>
                </div>
            </div>

            <div class="design-area">
                <div id="welcome-screen" class="welcome-screen">
                    <h2>Welcome to Crochet Design Tool</h2>
                    <p>Set your project dimensions and click "Create Project" to start designing your crochet pattern.</p>
                </div>

                <div id="grid-container" class="grid-container hidden">
                    <div id="grid" class="grid"></div>
                </div>
            </div>
        </div>
    </div>

    <script>
        let currentTool = 'fill';
        let gridData = [];
        let gridWidth = 30;
        let gridHeight = 35;
        let isDrawing = false;

        function setTool(tool) {
            currentTool = tool;
            document.querySelectorAll('.tool-btn[data-tool]').forEach(btn => {
                btn.classList.remove('active');
            });
            document.querySelector(`[data-tool="${tool}"]`).classList.add('active');
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

            // Create the grid
            gridWidth = width;
            gridHeight = height;
            initializeGrid();

            // Show grid area
            document.getElementById('welcome-screen').classList.add('hidden');
            document.getElementById('grid-container').classList.remove('hidden');

            // Update stats
            updateStats();

            // Send project data to Streamlit
            sendToStreamlit({
                action: 'project_created',
                project: { name, width, height },
                timestamp: new Date().toISOString()
            });
        }

        function initializeGrid() {
            gridData = Array(gridHeight).fill().map(() => Array(gridWidth).fill(false));
            renderGrid();
        }

        function renderGrid() {
            const gridElement = document.getElementById('grid');
            gridElement.innerHTML = '';

            for (let y = 0; y < gridHeight; y++) {
                const row = document.createElement('div');
                row.className = 'grid-row';

                for (let x = 0; x < gridWidth; x++) {
                    const cell = document.createElement('div');
                    cell.className = `grid-cell ${gridData[y][x] ? 'filled' : ''}`;
                    cell.dataset.x = x;
                    cell.dataset.y = y;

                    cell.addEventListener('mousedown', (e) => {
                        isDrawing = true;
                        toggleCell(x, y);
                        e.preventDefault();
                    });

                    cell.addEventListener('mouseenter', (e) => {
                        if (isDrawing) {
                            toggleCell(x, y);
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
        }

        function toggleCell(x, y) {
            if (currentTool === 'fill') {
                gridData[y][x] = true;
            } else if (currentTool === 'erase') {
                gridData[y][x] = false;
            }

            const cell = document.querySelector(`[data-x="${x}"][data-y="${y}"]`);
            cell.className = `grid-cell ${gridData[y][x] ? 'filled' : ''}`;

            updateStats();
        }

        function clearGrid() {
            gridData = Array(gridHeight).fill().map(() => Array(gridWidth).fill(false));
            renderGrid();
            updateStats();
        }

        function drawShape(shape) {
            const centerX = Math.floor(gridWidth / 2);
            const centerY = Math.floor(gridHeight / 2);

            if (shape === 'rectangle') {
                const width = Math.min(10, gridWidth - 2);
                const height = Math.min(8, gridHeight - 2);
                const startX = centerX - Math.floor(width / 2);
                const startY = centerY - Math.floor(height / 2);

                for (let y = startY; y < startY + height; y++) {
                    for (let x = startX; x < startX + width; x++) {
                        if (x >= 0 && x < gridWidth && y >= 0 && y < gridHeight) {
                            if (x === startX || x === startX + width - 1 || y === startY || y === startY + height - 1) {
                                gridData[y][x] = true;
                            }
                        }
                    }
                }
            } else if (shape === 'circle') {
                const radius = Math.min(5, Math.floor(Math.min(gridWidth, gridHeight) / 4));
                for (let y = 0; y < gridHeight; y++) {
                    for (let x = 0; x < gridWidth; x++) {
                        const dist = Math.sqrt((x - centerX) ** 2 + (y - centerY) ** 2);
                        if (Math.abs(dist - radius) < 1.5) {
                            gridData[y][x] = true;
                        }
                    }
                }
            } else if (shape === 'heart') {
                // Simple heart shape
                const scale = Math.min(gridWidth, gridHeight) / 20;
                for (let y = 0; y < gridHeight; y++) {
                    for (let x = 0; x < gridWidth; x++) {
                        const dx = (x - centerX) / scale;
                        const dy = (y - centerY + 3) / scale;
                        if (Math.pow(dx * dx + dy * dy - 1, 3) - dx * dx * dy * dy * dy <= 0 && dy <= 1) {
                            gridData[y][x] = true;
                        }
                    }
                }
            }

            renderGrid();
            updateStats();
        }

        function updateStats() {
            const filledCount = gridData.flat().filter(cell => cell).length;
            const totalCells = gridWidth * gridHeight;
            const stitches = filledCount * 2; // Approximate
            const yarns = Math.ceil(stitches / 1000); // Very rough estimate

            document.getElementById('grid-size').textContent = `${gridWidth} × ${gridHeight}`;
            document.getElementById('filled-count').textContent = filledCount;
            document.getElementById('stitch-count').textContent = stitches;
            document.getElementById('yarn-estimate').textContent = `${yarns} skein${yarns !== 1 ? 's' : ''}`;
        }

        function exportPattern() {
            const projectName = document.getElementById('project-name').value || 'Untitled';
            const filledCount = gridData.flat().filter(cell => cell).length;

            let pattern = `CROCHET PATTERN: ${projectName}\\n`;
            pattern += `Grid: ${gridWidth} × ${gridHeight} (${filledCount} filled squares)\\n\\n`;
            pattern += `PATTERN CHART:\\n`;

            for (let y = 0; y < gridHeight; y++) {
                let row = '';
                for (let x = 0; x < gridWidth; x++) {
                    row += gridData[y][x] ? '█' : '·';
                }
                pattern += row + '\\n';
            }

            pattern += `\\nLEGEND:\\n█ = Chain space (filled square)\\n· = Double crochet (open square)`;

            sendToStreamlit({
                action: 'pattern_exported',
                pattern: pattern,
                stats: {
                    width: gridWidth,
                    height: gridHeight,
                    filled: filledCount,
                    stitches: filledCount * 2
                },
                timestamp: new Date().toISOString()
            });

            alert('Pattern exported! Check the Streamlit app for details.');
        }

        function sendToStreamlit(data) {
            window.parent.postMessage({
                type: "streamlit:setComponentValue",
                value: data
            }, "*");
        }

        // Set component height
        function updateHeight() {
            const height = Math.max(document.body.scrollHeight, 600);
            window.parent.postMessage({
                type: "streamlit:setFrameHeight",
                height: height
            }, "*");
        }

        // Initialize
        window.addEventListener('load', () => {
            updateHeight();
            updateStats();
        });

        window.addEventListener('resize', updateHeight);
    </script>
</body>
</html>
'''