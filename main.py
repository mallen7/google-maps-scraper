import sys
from src.gmaps import Gmaps


# Check if a command-line argument is provided
if len(sys.argv) > 1:
    query = sys.argv[1]
else:
    print("Please provide a query as a command-line argument.")
    sys.exit(1)

# Use the provided query
queries = [query]
Gmaps.places(queries, has_website=True, has_phone=True, max=5)