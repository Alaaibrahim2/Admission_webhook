# Kubernetes Validating Admission Webhook

## Overview

This project demonstrates how to build a custom Kubernetes Validating Admission Webhook using Python and Flask.

The webhook validates Pod creation requests and rejects any Pod that does not define resource limits.

---

## Architecture

kubectl apply
↓
API Server
↓
Validating Admission Webhook
↓
Python Flask Server
↓
Allow / Deny

---

## Features

* Custom Kubernetes Admission Webhook
* HTTPS communication using TLS certificates
* ValidatingWebhookConfiguration
* Reject Pods without resource limits
* External webhook running outside the Kubernetes cluster

---

## Technologies Used

* Kubernetes
* Python
* Flask
* Admission Controllers
* TLS / SSL Certificates
* kubeadm

---

## Validation Logic

The webhook inspects incoming Pod specifications.

If a container does not contain:

```yaml
resources:
  limits:
```

the request is rejected.

Example response:

```json
{
  "allowed": false,
  "status": {
    "message": "Resource limits are required"
  }
}
```

---

## Generate TLS Certificates

```bash
openssl req \
-x509 \
-nodes \
-days 365 \
-newkey rsa:2048 \
-keyout tls.key \
-out tls.crt \
-config san.cnf
```

---

## Run Webhook Server

```bash
python3 app.py
```

---

## Apply Webhook Configuration

```bash
kubectl apply -f validating-webhook.yaml
```

---

## Test Rejected Pod

```bash
kubectl apply -f bad-pod.yaml
```

Expected:

```text
admission webhook denied the request
```

---

## Test Accepted Pod

```bash
kubectl apply -f good-pod.yaml
```

Expected:

```text
pod/nginx-good created
```

---

## Kubernetes Flow

Authentication
↓
Authorization
↓
Admission Controllers
↓
Validating Webhook
↓
etcd

---

## Learning Outcomes

Through this project you will learn:

* Kubernetes Admission Controllers
* AdmissionReview objects
* TLS certificates and SANs
* Kubernetes API Server integrations
* Custom policy enforcement
* Kubernetes security concepts
