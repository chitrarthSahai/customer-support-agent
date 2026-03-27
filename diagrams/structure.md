/project-root
├── app/
│   ├── core/
│   │   ├── config.py             # Settings, environment configuration, logging
│   │   ├── security.py           # Authentication/authorization logic (JWT, OAuth)
│   │   └── database.py           # Database setup and connection logic (SQLAlchemy, etc.)
│   ├── shared/                   # Truly reusable utilities, global exceptions, constants
│   ├── users/                    # Feature module (group by domain, not type)
│   │   ├── models.py             # Database models (SQLAlchemy ORM models)
│   │   ├── schemas.py            # Data validation/serialization models (Pydantic models)
│   │   ├── repository.py         # Database queries only; data persistence logic
│   │   ├── service.py            # Business logic, validation, orchestrates repositories
│   │   ├── router.py             # API routes/endpoints (FastAPI APIRouter, Flask Blueprints)
│   │   └── dependencies.py       # Feature-specific dependency injection
│   ├── orders/                   # Another feature module
│   │   # ... same structure as 'users'
│   └── main.py                   # Application entry point, wires up routers and middleware
├── tests/
│   ├── unit/                     # Unit tests for services and utilities
│   ├── integration/              # Integration tests (API + DB end-to-end tests)
│   └── conftest.py               # Test configurations and fixtures
├── requirements.txt              # Project dependencies
├── Dockerfile                    # Containerization setup
├── .gitignore                    # Specifies intentionally untracked files
└── README.md                     # Project documentation
