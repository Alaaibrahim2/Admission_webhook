from flask import Flask, request, jsonify

app = Flask(**name**)

@app.route("/validate", methods=["POST"])
def validate():

```
req = request.get_json()

print("\n==============================")
print("Admission Review Received")
print("==============================")
print(req)

uid = req["request"]["uid"]

pod = req["request"]["object"]

containers = pod["spec"].get("containers", [])

for container in containers:

    resources = container.get("resources", {})

    limits = resources.get("limits")

    if not limits:

        return jsonify({
            "apiVersion": "admission.k8s.io/v1",
            "kind": "AdmissionReview",
            "response": {
                "uid": uid,
                "allowed": False,
                "status": {
                    "message": "Resource limits are required"
                }
            }
        })

return jsonify({
    "apiVersion": "admission.k8s.io/v1",
    "kind": "AdmissionReview",
    "response": {
        "uid": uid,
        "allowed": True
    }
})
```

if **name** == "**main**":

```
app.run(
    host="0.0.0.0",
    port=8443,
    ssl_context=("tls.crt", "tls.key")
)
```
