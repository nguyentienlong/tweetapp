const path = require('path');

module.exports = {
    outputDir: '../app/tw33t/templates',
    assetsDir: process.env.ASSETS_DIR,
    publicPath: '',
    runtimeCompiler: undefined,
    productionSourceMap: undefined,
    parallel: undefined,
    css: undefined,
    devServer: {
        proxy: {
            '/api': {
                target: 'http://localhost:8000/'
            }
        }
    }
};
