import json

with open('_bulk.json', 'r', encoding='utf-8') as f:
    docs = json.load(f)

with open('bulk.ndjson', 'w', encoding='utf-8') as f:
    for i, doc in enumerate(docs, start=1):
        doc_id = doc.get("id", f"auto-{i}")
        f.write(json.dumps({ "index": { "_index": "employee", "_id": doc_id } }) + "\n")
        f.write(json.dumps(doc) + "\n")
    f.write("\n")
