// api.test.js

const axios = require('axios');

describe('API Feedback Endpoint', () => {
  const baseURL = 'http://localhost:8000'; // Sesuaikan dengan URL base API Anda

  const feedbackData = {
    rating: 5,
  };

  test('submit feedback', async () => {
    try {
      const response = await axios.post(`${baseURL}/api/feedback/`, feedbackData);

      // Menguji status response
      expect(response.status).toBe(200);
      expect(response.data.success).toBeTruthy();
    } catch (error) {
      // Tangani kesalahan atau kegagalan pengujian
      console.error('Gagal mengirim feedback:', error);
      throw error;
    }
  });
});
