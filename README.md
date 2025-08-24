# 🔐 Password Hardening Lab

## Objective

In this project, I built a cybersecurity lab to monitor and analyze security events using Wazuh. The goal was to detect suspicious activity on a managed endpoint, configure alerts, and visualize findings through the Wazuh dashboard, while documenting all steps in a reproducible format suitable for portfolio presentation.

---

### 🧠 Skills Learned

* Installed and configured Wazuh manager on an Ubuntu Server VM (UTM).
* Connected a Wazuh agent running on macOS to the manager.
* Navigated and interpreted the Wazuh dashboard for real-time monitoring.
* Detected vulnerabilities, failed sudo attempts, and other suspicious activity.
* Configured alert notifications via Microsoft Teams webhook.
* Documented the lab setup, configuration, and log interpretation for reproducibility.

---

### 🛠️ Tools Used

* **Wazuh 4.12** – security monitoring, SIEM, and alerting.
* **Ubuntu Server 24.04 (UTM VM)** – host for Wazuh manager.
* **macOS (local machine)** – Wazuh agent.
* **Microsoft Teams** – communication channel for alerts via webhook.
* **Vulnerable test commands** – e.g., failed `sudo` attempts to generate SIEM events.

---

## 🧩 Steps

### Step 1: Prepare Environment

* Created an Ubuntu Server VM using UTM on macOS.
* Installed Wazuh manager following official instructions:

  ```bash
  curl -sO https://packages.wazuh.com/4.12/wazuh-install.sh && sudo bash ./wazuh-install.sh -a
  ```
<img width="1470" height="956" alt="wazuh install" src="https://github.com/user-attachments/assets/e3766898-9a94-4a1f-9d33-9198658edc3e" />

<img width="1470" height="956" alt="wazuh dashboard" src="https://github.com/user-attachments/assets/0952a765-bfa9-408f-a528-d8f4dc09a1b8" />


---

### Step 2: Connect macOS Agent

* Installed Wazuh agent on macOS. For this step, I simply downloaded the official pkg file, and then ran the following code to start:

  ```bash
  launchctl bootstrap system /Library/LaunchDaemons/com.wazuh.agent.plist
  ```
* Agent was enrolled via configuration. I edited the Wazuh agent config using nano, and added the Wazuh Manager IP address in the corresponding line.
* Verified agent status from Wazuh manager and dashboard.

<img width="1470" height="956" alt="connected mac" src="https://github.com/user-attachments/assets/146c119a-bca7-4017-9dba-d8e61251ad64" />

---

### Step 3: Access the Dashboard

* Logged in and confirmed agent connection and system status.

<img width="1470" height="956" alt="mac dashboard" src="https://github.com/user-attachments/assets/5c0c0fea-6e67-4671-b548-8a80a1b52194" />


---

### Step 4: Generate Test Security Events

* Triggered vulnerability alerts via Wazuh rules.
* Simulated failed `sudo` attempts to generate events:

  ```bash
  sudo -i
  ```
* Observed alerts in near real-time on the Wazuh dashboard.

<img width="309" height="165" alt="sudo attempt" src="https://github.com/user-attachments/assets/b4cd229e-9c60-4cd1-9f97-14f135c66b78" />

<img width="1470" height="834" alt="logs for sudo" src="https://github.com/user-attachments/assets/57e3fba8-e88f-4bc0-8041-561deaefbb4d" />

---

### Step 5: Configure Alert Notifications

* Set up a test Microsoft Teams channel and webhook.
* Configured Wazuh to send alerts via webhook in `/var/ossec/etc/ossec.conf` or rules:

  ```xml
  <command>
    <name>teams-webhook</name>
    <executable>curl</executable>
    <arguments>-H "Content-Type: application/json" -d '{"text":"Alert from Wazuh"}' https://outlook.office.com/webhook/...</arguments>
  </command>
  ```
* Verified that alerts were able t be delivered to Teams when suspicious activity occurred via a test message.

<img width="1470" height="838" alt="test message webhook to teams" src="https://github.com/user-attachments/assets/3dbace69-a4cc-43f2-8336-f021332d97d2" />


---

### Step 6: Document Findings

* Monitored dashboard for:

  * Agent connectivity
  * Vulnerability alerts
  * Failed login attempts
  * System changes
* Mapped alerts to MITRE ATT\&CK techniques (e.g., T1110: Brute Force, T1078: Valid Accounts).

---

### Step 7: Final Report

* Summarized lab setup, agent-manager connection, and detection events.
* Included dashboard screenshots, alert notifications, and configuration files.
* Published to GitHub with clear README and reproducibility instructions.

### Conclusion

This lab provided valuable hands-on experience in setting up and managing a cybersecurity monitoring environment using Wazuh. Attempting to install Wazuh manually without guided instructions highlighted several challenges, including configuration errors and SSL certificate management, which reinforced the importance of careful documentation and troubleshooting. Working with a virtual machine environment helped solidify understanding of networked systems, agent-manager relationships, and endpoint monitoring. Through interacting with the SIEM dashboard, generating test security events, and configuring alert channels, I gained practical exposure to detection, logging, and alerting workflows. Overall, this project strengthened skills in threat monitoring, log analysis, and incident response while providing a reproducible lab setup suitable for a portfolio.
