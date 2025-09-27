
# RentEzy - A Scalable Property Management Platform 🏡

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white) ![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB) ![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white) ![Kafka](https://img.shields.io/badge/Apache%20Kafka-231F20?style=for-the-badge&logo=apache-kafka&logoColor=white) ![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)

[cite_start]RentEzy is a comprehensive, microservices-based web application designed to streamline the entire property rental lifecycle[cite: 24]. [cite_start]It connects property owners, managers, and tenants through a seamless, real-time platform, automating everything from property listings and visit scheduling to rent collection and communication[cite: 24].

![RentEzy Landing Page](https://i.imgur.com/your-image-url.jpg)

## 🚀 Live Demo & Links

* **Live Application:** `your-live-link.com`
* **GitHub Repository:** `github.com/your-username/rentezy`

***

## 🏛️ Architectural Philosophy & Design Principles

The architecture of RentEzy is heavily inspired by the robust, event-driven patterns of large-scale platforms like Airbnb and Booking.com. The primary goal was to build a system that is not only feature-rich but also inherently scalable, resilient, and maintainable. This was achieved by adhering to several core principles:

### Microservices First

Instead of a single monolithic application, the system is decomposed into over 10 independent, single-purpose services[cite: 25].
* **Why?** This approach allows for **independent scaling** (e.g., scaling the `search_service` during peak hours without touching other services), **fault isolation** (an issue in the `notification_service` won't bring down bookings), and **technological flexibility**.

### Event-Driven & Asynchronously Communicating

Services do not communicate directly. [cite_start]Instead, they publish events to an **Apache Kafka** message bus and subscribe to the events they are interested in[cite: 25].
* **Why?** Kafka acts as the system's central nervous system, creating a **decoupled architecture**. This ensures **resilience**—if a service is temporarily down, messages are queued in Kafka and processed once the service recovers. It also allows for new services to be easily added to consume existing event streams without modifying the original producers.

### Decentralized Data Management (Polyglot Persistence)

Each microservice owns its data and uses the database technology best suited for its needs.
* **Why?** This "right tool for the job" approach maximizes performance. [cite_start]We use **PostgreSQL** for reliable transactional data [cite: 13, 19, 38][cite_start], **Elasticsearch** for complex, high-performance text search queries [cite: 13, 28, 31][cite_start], and **Redis** for caching and managing our high-throughput task queue[cite: 12, 27, 31].

### Centralized API Gateway

[cite_start]All client requests are routed through a single **API Gateway**[cite: 29].
* **Why?** The gateway is responsible for crucial cross-cutting concerns like **authentication, authorization, and rate limiting**[cite: 29]. It provides a unified and secure entry point to the system, simplifying the client-side application and protecting the internal services.

***

## 🏗️ System Architecture & Data Flow

The following diagram illustrates these principles in action, showing the flow of information from the client to the various backend services.

```mermaid
graph TD
    subgraph Client
        A[React Frontend]
    end

    subgraph API Layer
        B[API Gateway (Django)]
    end

    subgraph Core Services
        C[Auth Service]
        D[Property Service]
        E[Booking Service]
        F[Rent Service]
        G[Chat Service (WebSockets)]
        H[Notification Service]
    end

    subgraph Data & Search
        I[PostgreSQL Cluster]
        J[Elasticsearch Cluster]
        K[Search Consumer]
    end

    subgraph Asynchronous Backbone
        L[Apache Kafka Bus]
    end

    A -- HTTPS Requests --> B
    B -- Authenticates & Routes --> C & D & E & F & H
    B -- WebSocket Connection --> G

    D -- Publishes Events (e.g., PropertyUpdated) --> L
    E -- Publishes Events (e.g., BookingCreated) --> L

    L -- Events --> K[Consumes Property Events]
    L -- Events --> H[Consumes Booking/Payment Events]

    K -- Updates Search Index --> J
    B -- Delegates Search Queries --> J

    C & D & E & F -- CRUD Operations --> I
