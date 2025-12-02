# Flask Web Application with Docker and CI/CD

This project is a simple Flask web application that has been containerized using Docker and has a CI/CD pipeline set up with GitHub Actions to build, test, and deploy the application to Azure Web Apps.

## Project Structure

The project has a nested structure, with the main application code located in the `FlaskWebApp-main` directory.

```
.
├── .github/workflows/cicd.yml
└── FlaskWebApp-main/
    ├── Dockerfile
    ├── requirements.txt
    ├── FlaskWebProject1/
    │   ├── __init__.py
    │   └── ...
    └── ...
```

## Docker Setup

The `Dockerfile` in the `FlaskWebApp-main` directory is used to containerize the Flask application.

### Building the Docker Image

To build the Docker image, run the following command from the `FlaskWebApp-main` directory:

```sh
docker build -t your-docker-username/devops .
```

### Running the Docker Container

To run the Docker container, use the following command:

```sh
docker run -p 5000:5000 your-docker-username/devops
```

The application will be accessible at `http://localhost:5000`.

## CI/CD Pipeline

The CI/CD pipeline is defined in the `.github/workflows/cicd.yml` file. It uses GitHub Actions to automate the build and deployment process.

The pipeline consists of two main jobs: `build` and `deploy`.

### Build Job

The `build` job performs the following steps:
1.  Checks out the code from the repository.
2.  Sets up a Python 3.9 environment.
3.  Installs the project dependencies from `requirements.txt`.
4.  Runs a lint check using `flake8`.

### Deploy Job

The `deploy` job is triggered after the `build` job completes successfully. It performs the following steps:
1.  Logs in to Docker Hub using credentials stored in GitHub secrets.
2.  Builds the Docker image and tags it with the Git commit SHA.
3.  Pushes the Docker image to Docker Hub.
4.  Deploys the new image to an Azure Web App.

### `working-directory`

A key aspect of this pipeline is the use of the `working-directory: ./FlaskWebApp-main` attribute in several steps. This is necessary because the `Dockerfile`, `requirements.txt`, and application code are located in a subdirectory. This setting ensures that the commands are run from the correct directory.

## Azure Deployment

The pipeline is configured to deploy the application to an Azure Web App. This is handled by the `azure/webapps-deploy@v2` action. The deployment requires the following GitHub secret to be configured:

*   `AZURE_WEBAPP_PUBLISH_PROFILE`: The publish profile for the Azure Web App.

This secret allows the pipeline to securely authenticate with Azure and deploy the containerized application.
