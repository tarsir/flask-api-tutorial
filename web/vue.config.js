let path = require('path');

module.exports = {
    configureWebpack: {
        resolve: {
            extensions: ['.vue', '.js', '.ts'],
            alias: {
                '@': path.resolve(__dirname, 'src')
            }
        }
    }
};
