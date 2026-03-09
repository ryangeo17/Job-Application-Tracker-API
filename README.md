# Job Application Tracker API

A RESTful API built with Flask for tracking job applications throughout the hiring process. Manage your job search by recording applications, updating their status, and querying your application history.

## Features

- **Create Applications**: Add new job applications with company name, role, and status
- **Track Status**: Monitor application progress through different stages (applied, interview, offer, rejected)
- **Query & Filter**: Search applications by status with sorting and pagination support
- **Update Progress**: Modify application status as you move through the hiring pipeline
- **Bulk Operations**: Delete multiple applications by status
- **RESTful Design**: Clean, intuitive API endpoints following REST principles

## Tech Stack

- **Framework**: Flask 3.1.3
- **Database**: SQLite with SQLAlchemy ORM
- **ORM**: Flask-SQLAlchemy 3.1.1
- **Server**: Gunicorn 25.1.0 (production-ready)
- **Language**: Python 3.x

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd <project-directory>
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python run.py
```

The API will be available at `http://localhost:5000`

## API Endpoints

### Get All Applications
```http
GET /applications
```

**Query Parameters:**
- `status` - Filter by status (applied, interview, offer, rejected)
- `sort` - Sort by date (`applied_at` or `-applied_at` for descending)
- `limit` - Limit number of results
- `offset` - Offset for pagination

**Example:**
```bash
curl http://localhost:5000/applications?status=interview&sort=-applied_at&limit=10
```

### Get Single Application
```http
GET /applications/<id>
```

**Example:**
```bash
curl http://localhost:5000/applications/1
```

### Create Application
```http
POST /applications
```

**Request Body:**
```json
{
  "company": "Tech Corp",
  "role": "Software Engineer",
  "status": "applied"
}
```

**Example:**
```bash
curl -X POST http://localhost:5000/applications \
  -H "Content-Type: application/json" \
  -d '{"company":"Tech Corp","role":"Software Engineer","status":"applied"}'
```

### Update Application Status
```http
PUT /applications/<id>
```

**Request Body:**
```json
{
  "status": "interview"
}
```

**Example:**
```bash
curl -X PUT http://localhost:5000/applications/1 \
  -H "Content-Type: application/json" \
  -d '{"status":"interview"}'
```

### Delete Application
```http
DELETE /applications/<id>
```

**Example:**
```bash
curl -X DELETE http://localhost:5000/applications/1
```

### Bulk Delete by Status
```http
DELETE /applications?status=<status>
```

**Example:**
```bash
curl -X DELETE "http://localhost:5000/applications?status=rejected"
```

## Application Status Values

- `applied` - Initial application submitted
- `interview` - Interview stage
- `offer` - Offer received
- `rejected` - Application rejected

## Database Schema

### Application Model

| Field | Type | Description |
|-------|------|-------------|
| id | Integer | Primary key (auto-generated) |
| company | String(100) | Company name (required) |
| role | String(100) | Job role/title (required) |
| status | String(20) | Application status (default: "applied") |
| applied_at | DateTime | Timestamp of application (auto-generated) |

## Project Structure

```
.
├── app/
│   ├── __init__.py      # Application factory
│   ├── db.py            # Database initialization
│   ├── models.py        # SQLAlchemy models
│   └── routes.py        # API endpoints
├── instance/
│   └── jobtracker.db    # SQLite database (auto-created)
├── requirements.txt     # Python dependencies
├── run.py              # Application entry point
└── README.md           # This file
```


## Error Handling

The API returns appropriate HTTP status codes:
- `200` - Success
- `201` - Created
- `400` - Bad Request (invalid input)
- `404` - Not Found
- `500` - Internal Server Error

Error responses include a JSON body with an `error` field describing the issue.

