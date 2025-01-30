# Project Title

## Description
This is a Django project that can be deployed on Vercel.

## Deployment Instructions

1. **Set Up Environment Variables**:
   - Create a `.env` file in the root of your project and add the following line:
     ```
     DATABASE_URL=your-database-url
     ```

2. **Update `settings.py`**:
   - Ensure that `ALLOWED_HOSTS` includes your Vercel domain:
     ```python
     ALLOWED_HOSTS = ['your-vercel-domain.vercel.app']
     ```
   - Set `DEBUG` to `False`:
     ```python
     DEBUG = False
     ```

3. **Install Dependencies**:
   - Make sure all dependencies are listed in `requirements.txt`. You can install them using:
     ```
     pip install -r requirements.txt
     ```

4. **Deploy to Vercel**:
   - Install the Vercel CLI if you haven't already:
     ```
     npm i -g vercel
     ```
   - Run the following command to deploy:
     ```
     vercel
     ```

5. **Follow the Prompts**:
   - Follow the prompts in the terminal to complete the deployment process.

## API Endpoints
- **GET** `/get/`: Returns basic information.

## Note on npm Installation
If you encounter issues while installing npm packages, such as `getaddrinfo ENOTFOUND`, please check your internet connection and DNS settings. Ensure that your network configuration allows access to GitHub and other necessary resources.

## License
This project is licensed under the MIT License.
