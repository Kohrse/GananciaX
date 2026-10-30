const { app, BrowserWindow, Menu } = require('electron');
const path = require('path');
function create() {
  Menu.setApplicationMenu(null);
  const w = new BrowserWindow({ width: 1100, height: 800, minWidth: 380, backgroundColor: '#17191c' });
  w.loadFile(path.join(__dirname, 'app', 'index.html'));
}
app.whenReady().then(create);
app.on('window-all-closed', () => app.quit());
