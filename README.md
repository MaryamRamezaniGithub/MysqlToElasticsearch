# Airflow DAGs for MySQL to Elasticsearch Data Transfer
This project defines an Apache Airflow Directed Acyclic Graph (DAG) designed to automate the process of transferring data from a MySQL database to an Elasticsearch index. The DAG leverages custom plugins and operators to streamline the data transfer process and includes basic task orchestration.As a data scientist looking to transition into this field, I created this project to learn and apply different data engineering concepts, techniques, and tools. I’m sharing my experiences here, and I hope you find them helpful.

## Introduction
This project sets up a comprehensive environment for orchestrating and monitoring data pipelines using Apache Airflow. It leverages Docker Compose to define and manage various services required for running Airflow in a distributed manner with CeleryExecutor, enabling scalable and reliable task execution.

## Technologies
**1- Apache Airflow**
 is an excellent open-source tool for orchestrating complex data pipelines. By defining Directed Acyclic Graphs (DAGs) that outline the sequence of tasks and their dependencies, I was able to automate data simulations and reliably execute tasks at scale. Leveraging Airflow's scheduling features, I efficiently managed data processing tasks, ensuring timely execution and seamless handling of dependencies across different components of the pipeline. The DAGs used in this project can be found in the "dags" directory.
### Key Components
- Webserver: The Airflow web interface is exposed on port 8080, allowing users to manage and monitor DAGs (Directed Acyclic Graphs) and tasks.
- Scheduler: Handles scheduling tasks to be executed according to the defined DAGs.
- Workers (Celery): Two Celery workers are set up to execute tasks in parallel, improving the system's ability to handle a large number of tasks.
- Flower: A real-time monitoring tool for Celery workers, available on port 5555, providing insights into task execution and worker performance.
- PostgreSQL: Serves as the backend database for Airflow, storing metadata and task logs. It is configured with default credentials (airflow/airflow) and runs on port 5432.
- Redis: Acts as the message broker for Celery, facilitating communication between the scheduler and workers, and runs on port 6379

  **2- Elasticsearch & Kibana **
   is a powerful open-source search and analytics engine designed for fast and scalable full-text search and Kibana is designed to work seamlessly with Elasticsearch, allowing users to visualize, search, and analyze data stored in Elasticsearch indices. By creating and customize dashboards in Kibana to display multiple visualizations on a single screen. In this project,  Elasticsearch runs on port 9200, and Kibana on port 5601.


** 3- MariaDB** 
   is designed to be compatible with MySQL, meaning that applications developed for MySQL can often be used with MariaDB without modification, it actually is a free version of MySQL database service. In this project is set up with default credentials (admin/admin) and running on port 3306.

** 4. DBeaver**
   is a popular, open-source database management tool and SQL client that provides a user-friendly interface for working with a wide variety of databases including relational databases like MySQL, PostgreSQL, MariaDB, Oracle, SQL Server, and SQLite, as well as NoSQL databases like MongoDB, Cassandra, and Redis. In this project we utilize DBeaver that provides a graphical user interface (GUI) that makes it easy to explore and manage MariaDB for browsing tables, running queries, viewing execution plans, and managing database objects.

** 5. Docker **
   I utilized a docker-compose configuration that optimizes the management of the project's tech stack, fosters streamlined development, deployment, and operation processes.

## Running the Project
#### Step 1: Clone the Repository
1. Open your terminal.
2. Clone the project repository from GitHub to your local machine using the following command:

   ```
   git clone https://github.com/MaryamRamezaniGithub/MysqlToElasticsearch.git
   ```
#### Step 2: Navigate to Project Directory
1. Use the command line to navigate to the root directory of the project:

   ```
   cd MysqlToElasticsearch
   ```
   #### Step 3: Start Docker Containers
1. Execute the following command to start all services defined in the docker-compose file:
   
   ```
   docker-compose up -d
   ```
   This command will build and start the Docker containers for various services in your project.
  #### Step 4: Monitor Service Initialization
 Pay attention to the initialization tasks performed by the `airflow-init` container.
   - The `airflow-init` container initializes Airflow and performs necessary setup tasks. After completing its initialization, this container will stop automatically.

 #### Step 5: Install DBeaver locally
 ou should install DBeaver database tool from [**HERE**](https://dbeaver.io/download/) and connect Mariadb in container with the following credentials: db: Mariadb, Database: test, username: root, password: admin( make sure that docker container is still running). We careate the following demo table in DBeaver GUI:
 ![1](https://github.com/user-attachments/assets/53e80a5c-ef1b-4984-a229-5d18d031a31e)
