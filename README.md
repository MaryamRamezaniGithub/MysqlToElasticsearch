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

  ** 2- Elasticsearch & Kibana **
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
   docker-compose -f airflow-elasticsearch-mariadb.yml up -d
   ```
   This command will build and start the Docker containers for various services in your project.
  #### Step 4: Monitor Service Initialization
 Pay attention to the initialization tasks performed by the `airflow-init` container.
   - The `airflow-init` container initializes Airflow and performs necessary setup tasks. After completing its initialization, this container will stop automatically.

 ![4](https://github.com/user-attachments/assets/384f619d-47af-433a-98d4-cae03cb161b5)

 #### Step 5: Install DBeaver locally
 ou should install DBeaver database tool from [**HERE**](https://dbeaver.io/download/) and connect Mariadb in container with the following credentials: host: localhost, Database: test, username: root, password:
admin( make sure that docker container is still running)

 ![5](https://github.com/user-attachments/assets/203e06bb-f69e-42ed-9008-dd9ec5add119)

 We careate the following demo table in DBeaver GUI:
 
 ![1](https://github.com/user-attachments/assets/53e80a5c-ef1b-4984-a229-5d18d031a31e)

 #### Step 6: Make connection between Mariadb and Elasticsearch
If you navigate in 'plugin/hooks' and 'plugin/operators' directory you can see all code requiered for making connection between Mariadb and Elasticsearch. I Wrote 

- 'plugin/hooks' : This Python code defines a custom hook class, ElasticsearchHook, which is used to interact with an Elasticsearch cluster within the Apache Airflow framework. Hooks in Airflow are abstractions for connecting to external systems, allowing tasks to interact with mariadb.

  ![2](https://github.com/user-attachments/assets/447f09a6-11c1-45b8-b7f3-0f09c398cdea)

the method (__init__) accepts a connection ID (elasticsearch_conn_id) that defaults to 'elasticsearch_default'. This ID is used to retrieve connection details from Airflow's connection management system. So in your Airflow webserver, you should go to 'admin/connection'

![7](https://github.com/user-attachments/assets/d703e23e-0e44-4e57-8539-216bb5d31cd5)
  
- 'plugin/operators': This code defines a custom Airflow operator named MySqlToElasticsearchTransfer, which is designed to transfer data from a MySQL database to an Elasticsearch index. This operator extends Airflow's BaseOperator class, allowing it to be used as a task within an Airflow Directed Acyclic Graph (DAG).

  ![3](https://github.com/user-attachments/assets/e9411683-baab-4d49-993e-8444793e8617)

the mysql_conn_id is set to "mysql_default", we should retrive  Airflow connection ID for the Mariadb database as the following

 ![6](https://github.com/user-attachments/assets/2ad6c3c5-7e23-454a-9244-314a64b32421)

 #### Step 7: Monitor Airflow DAGs from Airflow Web Server

 If every thing goes well you can see the following pipeline in Graph tab of your Airflow We Server

 ![8](https://github.com/user-attachments/assets/312f0396-42fe-4683-8ec3-ab82d2aad87b)

 To see the results in Elasticsearch, you should go to 'Kibana' with ip address 'http://localhost:5601' and write the following search query in console:

 ![9](https://github.com/user-attachments/assets/5d483344-d995-416f-b0cb-4e108f8d9399)

You can see the reults are successfully transfered into Elasticsearch. 

Hope you Enjoy...
