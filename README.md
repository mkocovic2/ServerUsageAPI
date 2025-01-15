# System Monitoring API

A Flask-based REST API that provides system monitoring capabilities including CPU, memory, disk, and network information. The API is secured using Bearer token authentication.

## Features

- Real-time system metrics monitoring
- Secure API authentication using Bearer tokens
- Metrics available:
  - CPU count and usage
  - Memory utilization
  - Disk usage
  - Network I/O statistics
  - Network interface information

## Prerequisites

- Python 3.x
- pip (Python package manager)

## Installation

1. Clone the repository
2. Install the required dependencies:
```bash
pip install flask psutil python-dotenv
```

## Configuration

1. Generate an API key by running:
```bash
python key.py
```
This will:
- Generate a secure API key
- Hash the key using SHA-256
- Save the hashed key to `keys.env`
- Display the original API key (save this for authentication)

## Usage

1. Start the server:
```bash
python system.py
```
The API will be available at `http://localhost:2000/system_api`

2. Make requests using your API key:
```bash
curl -H "Authorization: Bearer YOUR_API_KEY" http://localhost:2000/system_api
```

## API Response

Successful requests return a JSON object with the following structure:

```json
{
    "CPU_Count": <number>,
    "CPU_Usage": <percentage>,
    "Memory": <percentage>,
    "Disk_Usage": <percentage>,
    "Network": {
        "bytes_sent": <number>,
        "bytes_recv": <number>,
        "packets_sent": <number>,
        "packets_recv": <number>,
        "errin": <number>,
        "errout": <number>,
        "dropin": <number>,
        "dropout": <number>
    },
    "Network_Interface": {
        <interface_details>
    }
}
```

## Security

- API keys are securely generated using `secrets.token_urlsafe()`
- Keys are hashed using SHA-256 before storage
- All API endpoints require Bearer token authentication

## Error Responses

- `{"message": "Authorization Error"}` - No Bearer token provided
- `{"message": "Invalid Bearer Token"}` - Invalid API key

## File Structure

- `system.py` - Main API server implementation
- `key.py` - API key generation and management
- `keys.env` - Environment file storing the hashed API key

## Notes

- The server runs in debug mode by default (not recommended for production)
- The API listens on all interfaces (0.0.0.0)
- Default port is 2000

## Security Recommendations

1. Use HTTPS in production
2. Disable debug mode in production
3. Implement rate limiting
4. Regular API key rotation
5. Monitor for suspicious activities

