import json

arber_json = json.loads("""{"name": "Ski resort Krylya Sovetov", "neighbouring_towns": []}""")
print(json.dumps(arber_json, indent=4))
print(len(arber_json))