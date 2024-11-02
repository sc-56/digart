function build_application(port) {
    const express = require('express');
    const path = require('path');
    const app = express();
    app.use((req, res, next) => {
        express.static(path.join(__dirname, 'public'))
    });
    app.get('/', (req, res) => {
        res.sendFile(path.join(__dirname, 'public', index.html))
    });
    
    return app;
};

port = 3000;
app = build_application(port);
app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});

