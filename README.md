# Python ML Template

## Overview

This repository provides a robust template for building and testing Python Machine Learning (ML) projects. It's designed to streamline the development process and ensure consistency across different environments.

### Key Features

1. **Dev Container Setup**: Utilizes Docker to create a containerized development environment, ensuring consistency across different machines.

2. **Pre-commit Configuration**: Automatically formats and checks your code on commit, maintaining code quality and consistency.

3. **Logging Utilities**: Includes a comprehensive logging setup for easy debugging and monitoring.

4. **Configuration Management**: Provides a YAML-based configuration system for easy project customization.

5. **VSCode Integration**: Includes settings for a smooth development experience in Visual Studio Code.

6. **Git Credential Management**: Ensures secure and easy authentication with Git repositories.

7. **Python Environment**: Sets up a virtual environment with essential ML libraries pre-installed.

8. **Google Cloud SDK**: Includes setup for Google Cloud CLI, facilitating cloud-based development and deployment.

## Project Structure

- `src/`: Main source code directory
  - `utils/`: Utility functions, including logging setup
  - `config.yaml`: Configuration file for project settings
- `.devcontainer/`: Dev container configuration
- `.pre-commit-config.yaml`: Pre-commit hook configurations
- `Dockerfile`: Docker configuration for the development environment
- `requirements.txt`: Python dependencies

## Setup Instructions

### Prerequisites

- Git
- Visual Studio Code with Remote - Containers extension

### Mac Setup

1. Make sure you have [Homebrew](https://brew.sh/) installed.

2. Install and start [Colima](https://github.com/abiosoft/colima):
```bash
brew install colima
colima start --cpu 2 --memory 8
```

3. Install the Docker client:
```bash
brew install docker
```

4. Install Git Credential Manager:
```bash
brew install --cask git-credential-manager
```

5. Clone the repo using `https` (do not use `ssh`). You will be prompted to login to GitHub:
```bash
git clone https://github.com/hdrwilkinson/ml-template.git
```

6. Open VSCode and install the [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension.

7. Open the cloned `ml-template` directory in VSCode.

8. Open the Command Palette (typically `fn` + `F1`) and search for and run `Dev Containers: Open Folder in Container`.

### Linux Setup

1. Install Docker:
   ```bash
   sudo apt-get update
   sudo apt-get install docker.io
   ```

2. Start Docker service:
   ```bash
   sudo systemctl start docker
   sudo systemctl enable docker
   ```

3. Install Visual Studio Code:
   Download and install from [VS Code website](https://code.visualstudio.com/)

4. Install Git:
   ```bash
   sudo apt-get install git
   ```

5. Clone the repository:
   ```bash
   git clone https://github.com/hdrwilkinson/ml-template.git
   ```

6. Open the cloned directory in VS Code and follow steps 6-8 from the Mac setup.

### Windows Setup

1. Install Docker Desktop for Windows:
   Download and install from [Docker website](https://www.docker.com/products/docker-desktop)

2. Install Visual Studio Code:
   Download and install from [VS Code website](https://code.visualstudio.com/)

3. Install Git for Windows:
   Download and install from [Git website](https://git-scm.com/download/win)

4. Clone the repository:
   ```bash
   git clone https://github.com/hdrwilkinson/ml-template.git
   ```

5. Open the cloned directory in VS Code and follow steps 6-8 from the Mac setup.

## Usage

After setting up the development environment:

1. The dev container will automatically set up the Python environment with all required dependencies.

2. Use the pre-configured logging utility in your Python scripts:

   ```python
   from src.utils.logging import setup_logging
   
   config = {...}  # Your configuration
   logger = setup_logging(config)
   logger.info("Your log message here")
   ```

3. Customize the `src/config.yaml` file for your project-specific settings.

4. Write your ML code in the `src/` directory, utilizing the provided structure and utilities.

5. Run the main script using:
   ```bash
   python3 src/main.py src/config.yaml
   ```
   This command executes the main script with the specified configuration file.

6. Use pre-commit hooks to maintain code quality:
   ```bash
   git add .
   git commit -m "Your commit message"
   ```
   The pre-commit hooks will automatically run, formatting and checking your code.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Acknowledgments

- Thanks to all contributors who have helped shape this template.
- Special thanks to the open-source community for the tools and libraries used in this project.

Happy developing!

