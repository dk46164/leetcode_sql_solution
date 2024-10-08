``` mermaid 
graph TD
    subgraph "User Access Flow"
        A[User] -->|Sends request with API key| B(API Gateway)
        B -->|Validates API key| C{Authorized?}
        C -->|Yes| D[Generate Snowflake Token]
        D --> E[Access Granted to Snowflake DWH]
        C -->|No| F[Access Denied]
    end

    subgraph "Snowflake"
        G[Auth Schema]
        H[DWH Schema]
        E -->|Query with Token| H
    end

    subgraph "Admin Approval Flow"
        I[Admin] -->|Logs in| J(Admin Dashboard)
        J -->|Views pending requests| K{Approve?}
        K -->|Yes| L[Update Auth Schema]
        K -->|No| M[Reject Request]
        L --> N[Notify User of Approval]
        M --> O[Notify User of Rejection]
        L -->|Update| G
    end

    subgraph "User Request Flow"
        P[User] -->|Logs in| Q(User Portal)
        Q -->|Requests access to DWH| R[Submit Request]
        R --> S[Store Request in Auth Schema]
        S -->|Store| G
        S --> T[Notify Admin of New Request]
    end

    subgraph "Data Model"
        U[users]
        V[endpoints]
        W[endpoint_versions]
        X[api_keys]
        Y[audit_trail]

        U --> X
        V --> W
        U --> Y
        V --> Y
        W --> Y
        X --> Y
    end

    B -->|Validate against| G
    R -->|Store in| G
    L -->|Update| G
```
