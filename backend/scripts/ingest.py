import os
import sys
import json

# Ensure parent directory is in path so we can import app modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.rag.vector_store import add_resources, collection

def ingest():
    json_path = os.path.join(os.path.dirname(__file__), 'resources.json')
    if not os.path.exists(json_path):
        print(f"Error: {json_path} does not exist.")
        return
        
    with open(json_path, 'r', encoding='utf-8') as f:
        resources = json.load(f)
        
    print(f"Found {len(resources)} total resources inside {json_path}.")
    
    # Check for existing IDs to ensure idempotency
    existing_ids = set()
    try:
        # ChromaDB get() yields elements by ID
        existing = collection.get()
        if existing and 'ids' in existing:
            existing_ids = set(existing['ids'])
    except Exception as e:
        print(f"Warning checking existing IDs: {e}. Attempting batch ingestion.")
        
    to_ingest = [r for r in resources if str(r['id']) not in existing_ids]
    
    if not to_ingest:
        print("All resources are already fully indexed! Skipping.")
        return
        
    print(f"Ingesting {len(to_ingest)} new resources into ChromaDB...")
    
    # Process in batches to monitor progress
    batch_size = 5
    for i in range(0, len(to_ingest), batch_size):
        batch = to_ingest[i:i+batch_size]
        add_resources(batch)
        print(f"Indexed {min(i + batch_size, len(to_ingest))}/{len(to_ingest)} new resources...")
        
    print("Successfully completed knowledge base ingestion!")

if __name__ == '__main__':
    ingest()
