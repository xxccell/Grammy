## Grammy: Your Recipe Measurement Converter 

**Tired of manually converting cups to grams in your recipes?** 

Use this for recipes that gives ingredients in cups instead of grams. Avoid having to manually search the conversion of cups to grams for each ingredient!

**How to Use Grammy:**

1. Copy and paste the recipe you want to use into the text area.

2. Click "Convert" and your recipe will be analyzed and all measurements will be converted to grams.

3. Get back the list of ingredients and recipe with all measurements converted to grams.


**Use Grammy Now!**

➡️ [Grammy](https://grammy.streamlit.app)



      
**Note:** Grammy assumes standard ingredient densities unless otherwise specified in the recipe.

---

## Running Grammy locally with Docker

To run the Grammy app on your local machine using Docker, follow these steps:

### Prerequisites

- Ensure you have Docker installed on your machine. You can download it from [here](https://www.docker.com/products/docker-desktop).

### Steps to Run

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/xxccell/Grammy.git
    ```

2. **Build the Docker Image**:
    Navigate into the project directory and run the following command to build the Docker image for the Grammy:
    ```bash
    cd Grammy
    docker build -t grammy .
    ```

3. **Run the Docker Container**:
    After the build is complete, you can run the Docker container:
    ```bash
    docker run -p 8501:8501 --env GEMINI_API_KEY=<your_api_key> grammy
    ```

    - Replace `your_api_key` with your own [Gemini API key](https://aistudio.google.com/app/apikey).
    - The app will now be accessible at `http://localhost:8501` in your browser.

**Note:** `GEMINI_API_KEY` can either be passed in the `docker run` command as shown above or set up in your environment as a variable. If no key is provided, the app will prompt users to enter their API key upon launching.

