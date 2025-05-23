# Token Info API

Enterprise-grade Flask microservice to fetch and serve EVM token metadata via the Dune Sim API, optimized for the Base blockchain (chain ID: 8453).

## Overview

This API enables real-time retrieval of token details such as name, symbol, decimals, total supply, and verification status for any ERC-20 token on the Base chain. It abstracts the complexity of direct API interactions, offering a clean, standardized interface for integration in analytics, wallets, dashboards, and backend workflows.

---

## Features

- **Base Chain Native:** Defaults to Base blockchain (`chain_id = 8453`), with extensibility for other EVM-compatible networks.
- **Secure:** API key management via environment variables.
- **Scalable:** Containerized with Docker, ready for cloud deployments.
- **CI/CD Integrated:** Automated linting, testing, building, and deployment via `boomchainlab-ci`.
- **Robust Error Handling:** Graceful API failure responses.

---

## Getting Started

### Prerequisites

- Python 3.11+
- Docker (for containerized deployment)
- Valid Dune Sim API key

### Installation

```bash
git clone https://github.com/Boomchainlab/token-info-api.git
cd token-info-api
pip install -r requirements.txt

export DUNE_API_KEY="your_sim_api_key_here"

Running Locally
python app.py

Usage

Query token info via HTTP GET:
curl "http://localhost:8080/api/token-info?address=0x233dF63325933fA3f2dac8E695Cd84bb2f91aB07"

Response example:
{
  "data": {
    "name": "slerf",
    "symbol": "$lerf",
    "decimals": 18,
    "total_supply": "1000000000000000000000000",
    "address": "0x233dF63325933fA3f2dac8E695Cd84bb2f91aB07",
    "chain_id": 8453,
    "is_verified": true
  }
}
https://twitter.com/slerf00

Docker Deployment

Build and run the Docker container locally:
docker build -t token-info-api .
docker run -p 8080:8080 token-info-api


CI/CD Pipeline

This project integrates with boomchainlab-ci for:
	•	Automated code linting and formatting
	•	Docker image build and push
	•	Deployment orchestration to cloud providers (e.g., Render)

⸻

Contributing

Contributions are welcome. Please adhere to coding standards and submit pull requests with descriptive messages.

⸻

License

This project is licensed under the MIT License.

⸻

Contact

Boomchainlab Dev Team – boomchainlabgravatar.link
