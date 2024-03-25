# Building Ontology API

This project provides a REST API to query a building ontology.

## Setup

1. Ensure you have Python 3.10 or later installed.
2. Create a virtual environment and activate it using:

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. Install the required Python packages:

    ```bash
    pip install flask rdflib
    ```

4. Clone the repository and navigate to the project directory:

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

5. Run the Flask server:

    ```bash
    python server.py
    ```

The server will start running at `http://127.0.0.1:5000`.

## Making API Calls

You can make a GET request to the `/api/ontology` endpoint to query the ontology. Here's an example using `curl`:

```bash
curl http://127.0.0.1:5000/api/ontology
```
