"""
Configuración del Sistema de Monitoreo de Ocupación
"""

UPDATE_INTERVAL_MINUTES = 15
DEFAULT_SITE_NAME = "Sótano 1"
DEFAULT_MAX_CAPACITY = 90
CONFIDENCE_THRESHOLD = 0.25

CAPTURES_FOLDER = "captures"
PROCESSED_FOLDER = "processed"
MODELS_FOLDER = "models"

CAMERA_INDEX = 0

# Umbrales basados en conteo ABSOLUTO de personas
# Vacío:              0 – 9 personas
# Parcialmente lleno: 10 – 19 personas
# Lleno:              20 o más personas
PEOPLE_THRESHOLDS = {
    "empty_max": 20,
    "partial_max": 49,
}

STATUS_LABELS = {
    "empty": "Vacío",
    "partial": "Parcialmente lleno",
    "full": "Lleno",
}

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "bmp", "webp"}

REPORTS_FOLDER = "reports"
REPORTS_FILE = "reports/history.json"

DATASET_FOLDER = "../dataset"

MONITORED_SITES = [
    {"id": 1, "name": "Sótano 1", "max_capacity": 90},
    {"id": 2, "name": "Sótano 2", "max_capacity": 80},
    {"id": 3, "name": "Biblioteca", "max_capacity": 150},
    {"id": 4, "name": "Cafetería", "max_capacity": 100},
]
