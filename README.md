# UCV-SI-lab9

Travel ADK Multiagent — Laboratorio UCV

Laboratorio académico que implementa un asistente de viaje multiagente sobre Google ADK. Este repositorio demuestra una arquitectura modular donde un agente coordinador delega tareas a subagentes especializados en búsqueda web, planificación de itinerarios, presupuesto, riesgos y cultura local.

---

## 📌 Propósito

Este proyecto implementa un asistente conversacional multiagente para planificación de viajes, diseñado como un laboratorio universitario para explorar patrones de diseño de agentes con Google ADK, pruebas con `pytest`, análisis estático con `ruff` y calidad/telemetría con SonarCloud.

## 🧠 Descripción funcional

El sistema centra su entrada en el `travel_coordinator_agent` que recibe la petición del usuario y orquesta a los subagentes para producir una respuesta consolidada. Los subagentes son responsables de tareas especializadas (búsqueda, itinerario, presupuesto, riesgo y cultura local) y pueden usar herramientas internas para cálculos o datos estructurados.

Flujo básico:

- El usuario envía una petición al coordinador.
- El coordinador decide qué subagentes invocar y en qué orden.
- Cada subagente utiliza herramientas puras cuando aplica (`tools/*.py`).
- El coordinador agrega y formatea la respuesta final.

## 🏗️ Arquitectura general

La arquitectura es modular y se organiza en capas:

1. Paquete `travel_assistant`: núcleo del proyecto.
2. Módulo `agent.py`: define el agente raíz (`travel_coordinator_agent`).
3. Carpeta `agents/`: agentes especializados (cada uno es una instancia de `google.adk.agents.Agent`).
4. Carpeta `tools/`: funciones utilitarias y calculadoras usadas por los agentes.
5. Tests unitarios en `tests/` con `pytest`.

La integración con Google ADK permite ejecutar estos agentes en la plataforma ADK/AI Studio usando el modelo `gemini-2.5-flash` según la configuración presente en los agentes.

---

## ✨ Características principales

- Orquestación multiagente con un `travel_coordinator_agent`.
- Subagentes para: búsqueda web, itinerario, presupuesto, revisión de riesgos y cultura local.
- Herramientas reutilizables: estimación de presupuesto, información cultural y evaluación de riesgos.
- Pruebas unitarias (`pytest`) y reporte de cobertura (`pytest-cov`).
- Análisis estático con `ruff`.
- Pipeline CI/CD con GitHub Actions y análisis SonarCloud.

## 🧰 Tecnologías utilizadas

| Categoría | Herramienta |
|---|---|
| Lenguaje | Python 3.11 |
| SDK de agentes | google-adk |
| Gestión de dependencias | Poetry |
| Variables de entorno | python-dotenv |
| Tests | pytest, pytest-cov |
| Lint/Formatter | ruff |
| CI | GitHub Actions |
| Calidad | SonarCloud |

---

## 📁 Estructura del proyecto

```text
.
├── .adk/
│   └── artifacts/
├── .github/
│   └── workflows/
│       └── ci.yml
├── travel_assistant/
│   ├── agent.py
│   ├── __init__.py
│   ├── agents/
│   │   ├── budget.py
│   │   ├── coordinator.py
│   │   ├── itinerary.py
│   │   ├── local_culture.py
│   │   ├── risk.py
│   │   └── web_search.py
│   └── tools/
│       ├── budget_tools.py
│       ├── culture_tools.py
│       └── risk_tools.py
├── tests/
│   ├── test_agent_structure.py
│   ├── test_budget_tools.py
│   ├── test_culture_tools.py
│   └── test_risk_tools.py
├── .env.example
├── pyproject.toml
├── poetry.lock
├── sonar-project.properties
├── coverage.xml
└── htmlcov/
```

---

## 🤖 Agentes y responsabilidades

- `travel_coordinator_agent` (coordinador): recibe la solicitud, orquesta subagentes y consolida la respuesta en secciones: resumen, hallazgos, itinerario, presupuesto, riesgos y cultura local. Usa la herramienta `transfer_to_local_culture` para delegar consultas culturales.

- `web_search_agent`: obtiene información actual y fiable (atracciones, horarios, restricciones, clima). Preferir fuentes oficiales.

- `itinerary_agent`: genera itinerarios día-a-día (mañana/tarde/noche), priorizando realismo y tiempos de descanso.

- `budget_agent`: estima presupuesto referencial usando `estimate_trip_budget(destination, days, daily_budget_usd)` y recomienda revisión de precios.

- `risk_reviewer_agent`: evalúa riesgos básicos (altura, clima, transporte, alta temporada, salud) mediante `assess_basic_travel_risks(destination, season)`.

- `local_culture_agent`: devuelve platos típicos, costumbres y frases útiles; utiliza `get_local_culture_info(destination)` para datos estructurados.

---

## 🛠️ Herramientas personalizadas

- `travel_assistant.tools.budget_tools.estimate_trip_budget(destination, days, daily_budget_usd)` — valida entradas y devuelve un diccionario con el total estimado.
- `travel_assistant.tools.culture_tools.get_local_culture_info(destination)` — retorna platos, costumbres y frases para destinos conocidos (Cusco, Buenos Aires, Arequipa, París) y un caso por defecto.
- `travel_assistant.tools.risk_tools.assess_basic_travel_risks(destination, season)` — lista riesgos simples y recomendaciones.

---

## ⚙️ Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/<usuario>/UCV-SI-lab9.git
cd UCV-SI-lab9
```

2. Instalar dependencias con Poetry:

```bash
poetry install
```

3. Copiar el ejemplo de variables de entorno y configurar:

```bash
cp .env.example .env
# Edita .env y añade tu clave
```

4. Edita `.env` y añade `GOOGLE_API_KEY`:

```env
GOOGLE_API_KEY="TU_API_KEY_DE_GOOGLE_AI_STUDIO"
```

---

## 🔧 Variables de entorno

| Variable | Descripción |
|---|---|
| `GOOGLE_API_KEY` | Clave para usar Google ADK / AI Studio. |
| `SONAR_TOKEN` | Token secret para enviar análisis a SonarCloud (configurar en GitHub Secrets). |

---

## ▶️ Ejecutar desde consola

No hay un CLI dedicado en el repositorio; se expone el agente raíz `travel_assistant.agent.root_agent`.

Comprobación rápida:

```bash
poetry run python -c "from travel_assistant.agent import root_agent; print(root_agent.name)"
```

Probar una herramienta directamente:

```bash
poetry run python - <<'PY'
from travel_assistant.tools.budget_tools import estimate_trip_budget
print(estimate_trip_budget('Cusco', 5, 80))
PY
```

---

## 🌐 Ejecutar la interfaz web de Google ADK

Este proyecto no incluye un front-end local. Para usarlo en una interfaz web de Google ADK / AI Studio:

1. Configurar `GOOGLE_API_KEY` en `.env`.
2. Registrar o importar `travel_assistant` como paquete o módulo en tu proyecto ADK.
3. Configurar un entrypoint que invoque `travel_coordinator_agent` desde la consola de ADK o tu aplicación.

Si desea, puedo ayudar a añadir un pequeño servidor Flask/CLI para ejecutar un front-end local.

---

## 🧪 Ejecutar pruebas unitarias

```bash
poetry run pytest
```

La configuración de `pyproject.toml` ya incluye cobertura y rutas de prueba. El pipeline genera además `coverage.xml`.

---

## 🧹 Análisis estático con Ruff

```bash
poetry run ruff check .
```

Configuración en `pyproject.toml`:
- `line-length = 100`
- `target-version = "py311"`
- `select = ["E", "F", "I", "UP", "B"]`

---

## 🚀 Pipeline CI/CD

Definido en `.github/workflows/ci.yml`. Eventos que disparan el pipeline:

- `push` a `develop` o `main`.
- `pull_request` hacia `develop` o `main`.

Pasos principales:
1. Checkout del repositorio.
2. Setup Python 3.11.
3. Instalar Poetry e dependencias.
4. Ejecutar `ruff`.
5. Ejecutar `pytest` con `--cov` y generar `coverage.xml`.
6. Ejecutar SonarCloud Scan (requiere `SONAR_TOKEN`).

---

## ☁️ Integración SonarCloud

Configuración en `sonar-project.properties`:

- `sonar.projectKey=joshiel123_UCV-SI-lab9`
- `sonar.organization=joshiel123`
- `sonar.sources=travel_assistant`
- `sonar.tests=tests`
- `sonar.python.coverage.reportPaths=coverage.xml`

El job en GitHub Actions ejecuta el escaneo y envía resultados a SonarCloud usando `SONAR_TOKEN` desde los secretos del repositorio.

---

## 💡 Ejemplos de uso reales

1. "Planifícame un viaje de 5 días a Cusco con presupuesto limitado y riesgos de altura."
2. "Sugiere un itinerario de 3 días en París e indícame platos típicos y frases útiles."
3. "Evalúa riesgos para Machu Picchu en temporada de lluvias y dame recomendaciones."

---

## 🗣️ Ejemplos de prompts recomendados

- "Organiza un itinerario para un viaje de 4 días a Arequipa."
- "¿Qué presupuesto referencial necesito para 7 días en Buenos Aires?"
- "¿Qué riesgos debo considerar al viajar a Cusco en temporada alta?"
- "Recomiéndame costumbres y frases útiles para visitar París."

---

## 🎯 Resultados esperados

Respuestas estructuradas y educativas que incluyan:

- Resumen de la petición.
- Hallazgos actualizados (si hubo búsqueda web).
- Itinerario día a día.
- Estimación de presupuesto referencial.
- Riesgos y recomendaciones preventivas.
- Información de cultura local y frases.
- Consejo final con recomendación de verificar fuentes oficiales.

---

## 🚧 Futuras mejoras

- Añadir un CLI o API REST para invocar agents localmente.
- Implementar acceso real a APIs de búsqueda para `web_search_agent`.
- Ampliar la base de datos de cultura local.
- Añadir manejo de errores en el coordinador y validaciones más robustas.
- Incrementar cobertura de pruebas y crear tests de integración.

---

## 👤 Autor

Josias Eliel Alfageme Neyra

---