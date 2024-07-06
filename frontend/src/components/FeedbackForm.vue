<template>
  <div id="app">
    <!-- Rating Popup Modal -->
    <div v-if="showModal" class="modal">
      <div class="modal-content">
        <!-- <span class="close" @click="closeModal">&times;</span> -->

        <!-- Rating Slider -->
        <div class="mb-6">
          <label for="ratingSlider" class="block text-sm font-medium text-gray-700"></label>
          <input
            type="range"
            id="ratingSlider"
            v-model="selectedRating"
            min="1"
            max="5"
            class="w-full appearance-none bg-gray-200 h-2 rounded-full outline-none"
            @input="setRating(selectedRating)"
            style="background: linear-gradient(to right, blue, blue calc((var(--rating) - 1) * 25% + 1 * 2));"
          >
        </div>

        <h2 class="modal-title text-xl font-semibold mb-4">How would you rate your satisfaction with our product ?</h2>
        
        <!-- Star Rating System -->
        <div class="rating-system">
          <div 
            v-for="star in stars" 
            :key="star.id" 
            class="star-container"
          >
            <span 
              class="star" 
              @click="setRating(star.id)"
              :class="{ 'rated': star.id <= selectedRating }"
            >
              &#9733;
            </span>
          </div>
        </div>

        <!-- Rating Range Labels -->
        <div class="flex items-center justify-between mt-2 text-sm text-gray-600">
          <span>Very Dissatisfied</span>
          <span>Very Satisfied</span>
        </div>
        
        <!-- Submit Button -->
        <button @click="submitFeedback" class="btn-submit mt-4">Submit</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      stars: [
        { id: 1 },
        { id: 2 },
        { id: 3 },
        { id: 4 },
        { id: 5 },
      ],
      selectedRating: null,
      showModal: true, // Set to true to show the modal on page load
    };
  },
  methods: {
    setRating(rating) {
      this.selectedRating = rating;
    },
    async submitFeedback() {
      if (!this.selectedRating) {
        alert('Please select a rating before submitting.');
        return;
      }

      const feedbackData = {
        rating: this.selectedRating,
      };

      try {
        const response = await fetch('/api/feedback/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(feedbackData),
        });

        if (response.ok) {
          this.showModal = false; // Hide modal on successful submission
          alert('Thank you for your feedback!');
        } else {
          throw new Error('Failed to submit feedback');
        }
      } catch (error) {
        console.error('Error submitting feedback:', error);
        // Handle error state in your UI
      }
    },
    closeModal() {
      this.showModal = false;
    },
  },
};
</script>

<style scoped>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  color: #2c3e50;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.modal {
  display: flex;
  justify-content: center;
  align-items: center;
  position: fixed;
  z-index: 1;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgba(185, 185, 185, 0.4);
}

.modal-content {
  background-color: #fefefe;
  padding: 40px;
  border: 1px solid #888;
  width: 100%;
  max-width: 500px;
  text-align: left;
  border-radius: 10px;
  position: relative;
}

.close {
  position: absolute;
  top: 10px;
  right: 10px;
  font-size: 24px;
  cursor: pointer;
  color: #aaa;
}

.modal-title {
  font-size: 1.5em;
  margin-bottom: 20px;
}

#ratingSlider{
  --rating: 0;
  width: 100%;
}

.rating-system {
  display: flex;
  justify-content: space-between;
  position: relative;
  margin-top: 20px;
}

.star-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.star {
  font-size: 4em;
  cursor: pointer;
  transition: color 0.3s;
  color: #a5a5a5; /* Warna bintang putih */
}

.star:hover,
.rated {
  color: #6e7271;
}

.btn-submit {
  background-color: #4caf50;
  color: white;
  border: none;
  padding: 10px 20px;
  cursor: pointer;
  margin-top: 20px;
  border-radius: 5px;
  transition: background-color 0.3s;
}

.btn-submit:hover {
  background-color: #45a049;
}

.flex {
  display: flex;
  margin-top: 20px;
  justify-content: space-between;
}
</style>
