# Tech Spec: github-skills-map
## Stack
- **Language**: TypeScript
- **Framework**: Express.js
- **Runtime**: Node.js (14.x)
- **Database**: MongoDB (Atlas)
- **Storage**: AWS S3 (for static assets)

## Hosting
- **Platform**: AWS Elastic Beanstalk (free-tier)
- **Region**: us-west-2 (Oregon)
- **Environment**: Node.js 14.x (64bit)
- **Instance type**: t2.micro

## Data Model
- **Collections**:
  - **users**: stores user metadata (GitHub ID, username, email)
  - **activities**: stores user coding activity (repo, branch, commit hash, timestamp)
  - **skills**: stores user skills (language, framework, runtime)
- **Key fields**:
  - **users**: `github_id`, `username`, `email`
  - **activities**: `github_id`, `repo`, `branch`, `commit_hash`, `timestamp`
  - **skills**: `github_id`, `language`, `framework`, `runtime`

## API Surface
- **Endpoints**:
  1. **GET /users/{github_id}**: retrieve user metadata
  2. **GET /activities/{github_id}**: retrieve user coding activity
  3. **GET /skills/{github_id}**: retrieve user skills
  4. **POST /users**: create new user
  5. **POST /activities**: create new coding activity
  6. **POST /skills**: create new skill
  7. **PUT /users/{github_id}**: update user metadata
  8. **PUT /activities/{github_id}**: update coding activity
  9. **PUT /skills/{github_id}**: update skill
  10. **DELETE /users/{github_id}**: delete user

## Security Model
- **Authentication**: GitHub OAuth 2.0
- **Authorization**: IAM roles ( AWS Cognito User Pools)
- **Secrets**: encrypted using AWS Key Management Service (KMS)
- **Data encryption**: at rest using MongoDB encryption at rest

## Observability
- **Logs**: AWS CloudWatch Logs
- **Metrics**: AWS CloudWatch Metrics
- **Traces**: AWS X-Ray

## Build/CI
- **CI/CD tool**: GitHub Actions
- **Build script**: `npm run build`
- **Test script**: `npm run test`
- **Deployment script**: `npm run deploy`
- **Environment variables**: stored in AWS System Manager Parameter Store