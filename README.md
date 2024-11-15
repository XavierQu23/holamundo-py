# holamundo-py
This is a small program that displays a "Hello World" message from Python.

## Expected Output
Hello from Python

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/XavierQu23/holamundo-py.git

2. Once the project is cloned, open it with Visual Studio Code.

3. Run app.py using the following command:
python app.py

Finally, open your browser and go to localhost on port 8000.

## How to Run in Docker
Pre-requisites
Docker and Docker Desktop installed
DockerHub account
Download Image
Open the Visual Studio Code terminal and enter the following code:

docker pull xavi1920/holaenpy

# Run Image
In the same terminal, enter the following command line:

docker run --name <NEWCONTAINERNAME> -d -p 8000:8000 <IMAGENAME>

# Replace 
NEWCONTAINERNAME with your desired container name and IMAGENAME with the image name.

Example:

docker run -d --name contentpy -p 8000:8000 hola_mundo

# View the Results
Open a new browser window and go to localhost:8000.

# Railway Link
Use this link to see the program running on Railway:

https://holamundo-py-production.up.railway.app/

![alt text](image.png)

