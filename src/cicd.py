```python
import os
from git import Repo

def runCICD():
    repo = Repo(os.getcwd())
    git = repo.git

    # Pull latest changes from the repository
    print("Pulling latest changes...")
    git.pull()

    # Run tests
    print("Running tests...")
    os.system("pytest")

    # If tests pass, build the application
    print("Building application...")
    os.system("python setup.py build")

    # If build is successful, deploy the application
    print("Deploying application...")
    os.system("python setup.py install")

    print("CI/CD pipeline completed successfully.")

if __name__ == "__main__":
    runCICD()
```
This is a simple CI/CD script that pulls the latest changes from the repository, runs tests using pytest, builds the application, and deploys it. It uses the GitPython library to interact with the Git repository and the os library to run commands in the system shell. Note that this is a very basic implementation and a real-world CI/CD pipeline would likely be more complex, involving separate environments for testing and deployment, more sophisticated error handling, and possibly other stages such as linting or code review.