from flask import Flask
from flask import jsonify
from rdflib import Graph

# Initialize Flask
app = Flask(__name__)

# Load the ontology
g = Graph()
g.parse("building.owl", format="xml")


# Define the API endpoint
@app.route("/api/ontology", methods=["GET"])
def get_ontology():
    # Query the ontology for top level elements
    qres = g.query(
        """
        SELECT DISTINCT ?s ?p ?o
        WHERE {
            ?s ?p ?o .
        }
        LIMIT 10
        """
    )

    # Convert the results to a list of dictionaries
    results = []
    for row in qres:
        results.append(
            {"subject": str(row[0]), "predicate": str(row[1]), "object": str(row[2])}
        )

    # Return the results as JSON
    return jsonify(results)


# Run the server
if __name__ == "__main__":
    app.run(debug=True)
