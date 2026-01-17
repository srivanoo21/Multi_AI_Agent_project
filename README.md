# Multi AI Agent Project

This repository contains a Python AI agent that accepts a **system prompt** and a **user query**, then generates a response using the selected model.  
It also includes a CI/CD pipeline using **Jenkins** and **SonarQube** to automate builds and enforce code quality.

---

## 🧠 What This Project Does

The AI agent:
- Accepts a **system prompt**
- Accepts a **user query**
- Uses a selected AI model to generate a response
- Outputs the answer to the user

---

## 📂 Key Files

| File | Purpose |
|------|---------|
| `app/` | Source code of the AI agent |
| `Dockerfile` | Builds a Docker image for Jenkins integration |
| `Jenkinsfile` | Defines the CI/CD pipeline steps |
| `Multi_AI_Agent_Workflow.png` | Workflow diagram for CI/CD |
| `requirements.txt` | Python dependencies |

---

## 🚀 Architecture Overview

### 1️⃣ GitHub
Your source code is hosted on GitHub.  
Whenever code is pushed or a pull request is created, it triggers the CI/CD pipeline.

### 2️⃣ Jenkins (CI Server)
Jenkins is an automation server that:
- Pulls your GitHub repository
- Runs tests/builds
- Executes static analysis steps
- Coordinates with SonarQube

> Jenkins is integrated with GitHub and is configured to automatically fetch and build code on commit/push events. :contentReference[oaicite:5]{index=5}

### 3️⃣ SonarQube (Code Quality)
SonarQube performs static code analysis to identify:
- Bugs
- Code smells
- Vulnerabilities
- Duplication and complexity issues

Jenkins uses a SonarQube plugin to scan the code and send results to the SonarQube server. :contentReference[oaicite:6]{index=6}

---

## 🛠 CI/CD Workflow

1. **Code pushed to GitHub**
2. **Jenkins triggers pipeline**
3. Jenkins:
   - Fetches repository
   - Builds the application
   - Runs SonarQube analysis
4. SonarQube generates a quality report
5. Pipeline finishes with pass/fail status

---

## 📌 Integration Summary

- **GitHub code** → is integrated into **Jenkins**
- **SonarQube server** → is integrated into *Jenkins pipeline*  
  (Jenkins sends code to SonarQube for static analysis)

So your project is integrated *into Jenkins*, and Jenkins uses SonarQube to analyze the code.

---

## 📈 Benefits

- **Automated builds**
- **Quality inspection with SonarQube**
- **Faster feedback on code changes**
- **Early detection of bugs and vulnerabilities**

---

## 📝 Notes

To run this project successfully, ensure:
- Jenkins is configured with GitHub credentials
- SonarQube Scanner is installed in Jenkins
- SonarQube server URL and token are configured in Jenkins settings

References:
- [SonarQube Jenkins plugin docs] (plugin helps integrate code scanning into Jenkins) :contentReference[oaicite:7]{index=7}
- [SonarQube CI integration] (explains setting up the SonarQube scanner in Jenkins) :contentReference[oaicite:8]{index=8}

