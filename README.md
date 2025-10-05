Perfecto, Jokabel 🌱💚 — te dejo **el README completo, en formato Markdown profesional**, listo para copiar y pegar directamente en tu archivo `README.md` (en VSCode o GitHub).

Solo reemplaza **TODO el contenido actual** del archivo por este texto👇

---

````markdown
# 🌿 BioAI Backend

### 🤖 Proyecto desarrollado por:
**Jokabel Rojas Morales**  
Astrocoders Lab 🌌 | SENATI — Ingeniería de Software con IA  
> Sistema Inteligente de Gestión de Residuos Sólidos con Inteligencia Artificial  

---

## 🚀 Descripción del proyecto

**BioAI** es un backend desarrollado en **FastAPI (Python)** que simula y gestiona procesos de biodegradación de residuos sólidos mediante Inteligencia Artificial.  
El sistema permite registrar usuarios, ejecutar simulaciones, entrenar modelos de IA, visualizar dashboards y exportar resultados a Excel.

---

## 🧩 Tecnologías principales

- **Python 3.12+**
- **FastAPI + Uvicorn**
- **MongoDB Atlas (PyMongo)**
- **scikit-learn + pandas + matplotlib**
- **openpyxl (para exportar resultados a Excel)**

---

## 🧠 Estructura del proyecto

```bash
bioai-backend/
│
├── app/
│   ├── main.py                # Punto de inicio FastAPI
│   ├── config.py              # Configuración (Mongo URI y variables)
│   │
│   ├── database/
│   │   └── connection.py      # Conexión a MongoDB Atlas
│   │
│   ├── models/                # Lógica de base de datos
│   │   ├── usuario_model.py
│   │   ├── simulacion_model.py
│   │   └── resultado_model.py
│   │
│   ├── routes/                # Rutas (endpoints)
│   │   ├── usuario_routes.py
│   │   ├── simulacion_routes.py
│   │   ├── resultado_routes.py
│   │   ├── dashboard_routes.py
│   │   └── export_routes.py
│   │
│   ├── schemas/               # Esquemas Pydantic (validación)
│   │   └── usuario_schema.py
│   │
│   └── services/              # Lógica avanzada
│       ├── bioai_engine.py
│       ├── dashboard_bioai.py
│       └── export_bioai.py
│
├── .env                       # Variables de entorno (Mongo URI, DB)
├── requirements.txt            # Dependencias
└── README.md                   # Documentación
````

---

## ⚙️ Instalación

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/JokabelRojas/BIOIA_backend.git
cd BIOIA_backend
```

---

### 2️⃣ Crear entorno virtual

```bash
python -m venv venv
source venv/Scripts/activate
```

---

### 3️⃣ Instalar dependencias

```bash
python -m pip install -r requirements.txt
```

---

### 4️⃣ Configurar variables de entorno

Crea un archivo `.env` en la raíz del proyecto con:

```ini
MONGO_URI = "mongodb+srv://bioai_admin:<tu_password>@usuarios.axw6ks1.mongodb.net/bioai_db?retryWrites=true&w=majority"
DB_NAME = "bioai_db"
```

> ⚠️ Sustituye `<tu_password>` por la contraseña real del usuario `bioai_admin`.

---

## ▶️ Ejecución

Inicia el servidor con:

```bash
uvicorn app.main:app --reload
```

Abre en el navegador:
👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

Ahí verás toda la documentación **Swagger UI** con los endpoints del sistema.

---

## 📘 Endpoints principales

| Método | Endpoint                   | Descripción            |
| ------ | -------------------------- | ---------------------- |
| GET    | `/`                        | Mensaje de bienvenida  |
| POST   | `/usuarios/`               | Crear usuario          |
| GET    | `/simular/`                | Listar simulaciones    |
| POST   | `/simular/`                | Crear simulación       |
| GET    | `/dashboard/`              | Ver dashboard de IA    |
| GET    | `/exportar/?formato=excel` | Exportar datos a Excel |

---

## 📊 Dashboard BioAI

El endpoint `/dashboard/` genera métricas y gráficos (codificados en base64):

* Degradación promedio por bacteria
* Energía usada por entorno
* Eficiencia final del sistema

---

## 💾 Exportación de datos

Puedes exportar todas las simulaciones y resultados a Excel con:

```bash
GET /exportar/?formato=excel
```

---

## 👩‍💻 Conexión con el Frontend

El frontend puede consumir esta API desde:

```bash
http://127.0.0.1:8000
```

Ejemplo de uso (Fetch API o Axios):

```javascript
fetch("http://127.0.0.1:8000/simular/")
  .then(res => res.json())
  .then(data => console.log(data));
```

---

## 🌍 Compartir la base de datos MongoDB Atlas

### 🔹 Crear un usuario de lectura/escritura

1. Entra a [https://cloud.mongodb.com](https://cloud.mongodb.com)
2. Abre tu proyecto → *Database Access*
3. Crea un usuario nuevo, por ejemplo:

   * Usuario: `bioai_front`
   * Contraseña: `Front2025!`
   * Privilegios: *Read and write to any database*
4. Copia su URI de conexión:

   ```bash
   mongodb+srv://bioai_front:Front2025!@usuarios.axw6ks1.mongodb.net/bioai_db?retryWrites=true&w=majority
   ```
5. Agrega esta URI en el archivo `.env` del frontend.

---

### 🔹 Compartir el proyecto completo en Atlas (opcional)

1. En MongoDB Atlas → **Project Settings → Project Access**
2. Clic en **Add Member**
3. Ingresa el correo de tu compañero
4. Asigna el rol:

   * `Project Data Access ReadWrite`
     o solo lectura:
   * `Project Data Access ReadOnly`
5. Guarda cambios ✅

Tu compañero podrá acceder a los datos directamente desde su cuenta Atlas.

---

## 📄 Licencia

Proyecto educativo — Astrocoders Lab © 2025
Desarrollado por **Jokabel Rojas Morales**

---

# 💚 BioAI: Ciencia, código e impacto ambiental.

````

---

## ✅ Luego, guarda y súbelo a GitHub

```bash
git add README.md
git commit -m "README actualizado con guía completa y acceso Mongo"
git push origin main
````
