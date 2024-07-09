# Fetch-Data-DevOps-Test

# Real-Time Data Pipeline with Kafka and Docker

## Project Setup

### Prerequisites
- Docker
- Python

### Setting Up the Environment
1. Clone the repository to your local machine.
2. Navigate to the project directory.

### Starting Docker Containers
1. Ensure Docker is running on your machine.
2. Run `docker-compose up` to start the Docker containers for Kafka, Zookeeper, and the data generator.

### Installing Python Dependencies
1. Create a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate


Instructions for Running the Project
Prerequisites
Docker installed on your local machine.
Python installed on your local machine (for running the consumer script).
Steps to Run the Project
Set Up Docker Containers:

Save the docker-compose.yml file in your project directory.
Open a terminal and navigate to your project directory.
Run docker-compose up to start the Docker containers for Kafka, Zookeeper, and the data generator.
Install Python Dependencies:

Ensure you have the required Python packages installed. You can create a requirements.txt file with the following content:
Copy code
kafka-python
Run pip install -r requirements.txt to install the dependencies.
Run the Kafka Consumer:

Save the consumer.py script in your project directory.
Open a terminal and navigate to your project directory.
Run python consumer.py to start the Kafka consumer and process messages.

Install dependencies:

pip install -r requirements.txt

Running the Kafka Consumer
Execute the Python script:

python consumer.py


Design Choices
Efficiency: The pipeline uses Kafka's distributed messaging capabilities for high throughput.
Scalability: The pipeline can scale by adding more consumers and producers.
Fault Tolerance: Kafka's distributed architecture ensures resilience and fault tolerance.

Explanation
The Kafka consumer reads messages from the user-login topic.
It processes the messages (e.g., filtering for android device types).
The processed messages are then produced to the processed-user-login topic.