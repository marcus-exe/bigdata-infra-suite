# 🚀 Apache Airflow Docker Compose Setup (Self-Hosted)

This project sets up a **production-like Apache Airflow environment using Docker Compose**, with a CeleryExecutor and all required components.

---

## ✅ What This Includes

- **Airflow Webserver** - Access UI on port **8080**
- **Airflow Scheduler** - Schedules DAGs and tasks
- **Airflow Worker** - Runs tasks (Celery Worker)
- **Redis** - Celery message broker
- **PostgreSQL** - Airflow metadata database
- **Flower** - Celery monitoring UI (port **5555**)

---

## ✅ Folder Structure

| Folder        | Purpose                                   |
|---------------|-------------------------------------------|
| `dags/`       | Place your DAG Python files here          |
| `logs/`       | Task logs will be written here            |
| `plugins/`    | Place custom Airflow plugins here         |
| `docker-compose.yml` | Docker Compose setup                |
| `README.md`   | This project guide                        |

---

## ✅ How to Run It

1. **Start All Airflow Services:**

```bash
docker-compose up
```
_note: This will initialize Airflow Metadata Database_

---

2. **Access Airflow UI:**

* Web UI: [http://localhost:8080](http://localhost:8080)
* Flower UI: [http://localhost:5555](http://localhost:5555)
* Default user:
  **Username:** `admin`
  **Password:** `admin`

---

## ✅ Creating Your First DAG

Put your `.py` DAG file inside the `/dags` folder.
Example DAG path:

```
dags/example_dag.py
```

---

## ✅ Useful Docker Commands

| Task                 | Command                               |
| -------------------- | ------------------------------------- |
| Check container logs | `docker-compose logs -f`              |
| Restart a service    | `docker-compose restart SERVICE_NAME` |
| Stop everything      | `docker-compose down`                 |

---

## ✅ Production Tips

* Set a **strong Fernet Key**
* Move **Postgres and Redis** to managed services for scaling
* Add **volumes for backups**
* Consider using **Airflow Connections and Variables**

---

## ✅ License

This project is licensed under the MIT License.

```
MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```