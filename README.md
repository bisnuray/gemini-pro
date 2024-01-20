<h1 align="center">Gemini Pro Python Script</h1>

<p align="center">
  <em>Gemini is a powerful artificial intelligence (AI) system that demonstrates the capability to understand and intelligently respond to a wide range of prompts. It can handle various types of inputs, including pictures, text, speech, music, and computer code, making it a versatile and advanced AI system.</em>
</p>

### Getting Started

To use Gemini Pro, you need to set up your environment by providing the required API key and service account credentials. Follow the steps below to get started:

## Prerequisites

- Python 3.9 or higher
- Libraries: `google-generativeai`
- `GOOGLE_API_KEY` and `GOOGLE_APPLICATION_CREDENTIALS`

1. Install the required dependencies, ensuring Python 3.9 or higher:

    ```bash
    pip install google-generativeai
    ```

2. Set the Google API key as an environment variable:

    ```bash
    set GOOGLE_API_KEY=<your-api-key>
    ```

   Make sure to replace `<your-api-key>` with your actual Google API key.

3. Set the path to the service account credentials as an environment variable:

    ```bash
    set GOOGLE_APPLICATION_CREDENTIALS=/path/to/serviceaccount.json
    ```

   Replace `/path/to/serviceaccount.json` with the actual path to your service account JSON file.

4. Create a Google Cloud Platform (GCP) service account and download the JSON key file. Follow these steps:
   - Go to [Google Cloud Console](https://console.cloud.google.com/).
   - Navigate to the project where you want to create a service account.
   - In the left sidebar, click on the hamburger menu and select "IAM & Admin" > "Service accounts."
   - Click on "Create Service Account" at the top of the page.
   - Enter a name for the service account, choose a role (e.g., Project > Editor), and click "Continue."
   - Skip the "Grant users access to this service account" section and click "Done."
   - Locate the newly created service account in the list and click on the pencil icon to the right.
   - Navigate to the "Add Key" tab, choose JSON as the key type, and click "Create." Save the downloaded JSON file to a secure location.

5. Obtain a Google API key by following the link [here](https://makersuite.google.com/app/apikey).

## Usage

Explore the capabilities of Gemini Pro by running the provided script. It demonstrates how to configure the API key, list available models, and generate content based on text input.

  ```bash
python gemini.py
  ```

## Author

- Name: Bisnu Ray
- Telegram: [@SmartBisnuBio](https://t.me/SmartBisnuBio)

Feel free to reach out if you have any questions or feedback.

