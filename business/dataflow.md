```markdown
# Dataflow Architecture

## External Data Sources
- **GitHub API**: Provides access to user repositories, commits, and activity data.
- **GitHub OAuth**: Used for user authentication and authorization.

## Ingestion Layer
- **GitHub Webhook Listener**: Listens for events from GitHub (e.g., push, commit, pull request).
- **GitHub API Client**: Fetches user data from GitHub API.
- **Auth Service**: Handles OAuth authentication and token management.

## Processing/Transform Layer
- **Activity Parser**: Parses raw GitHub activity data into structured formats.
- **Skill Analyzer**: Analyzes code commits to identify and quantify skills.
- **Visualization Engine**: Generates visual representations of skills and activity.

## Storage Tier
- **User Data Store**: Stores user profiles and authentication tokens.
- **Activity Data Store**: Stores parsed activity data.
- **Skill Data Store**: Stores analyzed skill data.
- **Visualization Cache**: Stores generated visualizations for quick retrieval.

## Query/Serving Layer
- **API Gateway**: Routes incoming requests to appropriate services.
- **Query Service**: Handles queries for user data, activity, and skills.
- **Visualization Service**: Retrieves and serves visualizations to users.

## Egress to User
- **Web Application**: Frontend application for users to view their skills and activity.
- **API Endpoints**: Provides access to skills and activity data for third-party applications.

## Block Diagram
```
+----------------+       +----------------+       +----------------+
|  GitHub API    |<----->|  GitHub API    |       |  GitHub Webhook|
|  (External)    |       |  Client        |<----->|  Listener      |
+----------------+       +----------------+       +----------------+
        |                       |                       |
        v                       v                       v
+----------------+       +----------------+       +----------------+
|  Auth Service  |       |  Activity      |       |  Skill         |
|  (Auth         |       |  Parser        |       |  Analyzer      |
|  Boundary)     |       +----------------+       +----------------+
+----------------+                       |                       |
        |                       v                       v
        +-----------------------+----------------+       +----------------+
                                    |                |       |  Visualization|
                                    v                v       |  Engine       |
                            +----------------+       +----------------+
                            |  User Data     |       |  Activity      |
                            |  Store         |       |  Data Store    |
                            +----------------+       +----------------+
                                    |                |
                                    v                v
                            +----------------+       +----------------+
                            |  Skill Data    |       |  Visualization |
                            |  Store         |       |  Cache         |
                            +----------------+       +----------------+
                                    |                |
                                    v                v
                            +----------------+       +----------------+
                            |  Query Service |       |  Visualization |
                            |  (Auth         |       |  Service       |
                            |  Boundary)     |       +----------------+
                            +----------------+               |
                                    |                       |
                                    v                       v
                            +----------------+       +----------------+
                            |  API Gateway   |       |  Web           |
                            |  (Auth         |       |  Application   |
                            |  Boundary)     |       +----------------+
                            +----------------+               |
                                    |                       |
                                    v                       v
                            +----------------+       +----------------+
                            |  API Endpoints |       |  (User)       |
                            +----------------+       +----------------+
```

## Auth Boundaries
- **Auth Service**: Manages OAuth tokens and user authentication.
- **API Gateway**: Enforces authentication and authorization for API endpoints.
- **Query Service**: Ensures only authenticated users can access their data.
```