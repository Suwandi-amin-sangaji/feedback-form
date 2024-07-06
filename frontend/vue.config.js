// vue.config.js

module.exports = {
  devServer: {
    proxy: {
      '/api': {
        target: 'http://localhost:8000',  // Sesuaikan dengan URL backend FastAPI
        ws: true,
        changeOrigin: true
      }
    }
  }
};

