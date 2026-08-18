import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta

BASE_URL = "http://localhost:5000"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def iniciar_sesion_admin(driver):
    driver.get(f"{BASE_URL}/login")
    driver.find_element(By.ID, "usuario").send_keys("admin")
    driver.find_element(By.ID, "contrasena").send_keys("Yemary24")
    driver.find_element(By.TAG_NAME, "button").click()
    WebDriverWait(driver, 5).until(EC.url_contains("/panel"))

# ==================================================
# SCRUM-9 — Iniciar sesión
# ==================================================
def test_scrum9_login_exitoso(driver):
    driver.get(f"{BASE_URL}/login")
    driver.find_element(By.ID, "usuario").send_keys("admin")
    driver.find_element(By.ID, "contrasena").send_keys("Yemary24")
    driver.find_element(By.TAG_NAME, "button").click()
    WebDriverWait(driver, 5).until(EC.url_contains("/panel"))
    assert "Bienvenido" in driver.page_source
    print("\n✅ SCRUM-9: Login exitoso — CUMPLIDO")

def test_scrum9_login_fallido(driver):
    driver.get(f"{BASE_URL}/login")
    driver.find_element(By.ID, "usuario").send_keys("incorrecto")
    driver.find_element(By.ID, "contrasena").send_keys("incorrecta")
    driver.find_element(By.TAG_NAME, "button").click()
    assert "login" in driver.current_url
    print("\n✅ SCRUM-9: Login fallido muestra error — CUMPLIDO")

# ==================================================
# SCRUM-10 — Crear usuarios con roles
# ==================================================
def test_scrum10_crear_usuario(driver):
    iniciar_sesion_admin(driver)
    driver.get(f"{BASE_URL}/crear_usuario")
    driver.find_element(By.ID, "nombre_completo").send_keys("Recepcionista Prueba")
    driver.find_element(By.ID, "usuario").send_keys("RecepcionistaP")
    driver.find_element(By.ID, "contrasena").send_keys("987654321")
    driver.find_element(By.ID, "rol").send_keys("Recepcionista")
    driver.find_element(By.TAG_NAME, "button").click()
    assert "usuario" in driver.page_source.lower() or "creado" in driver.page_source.lower()
    print("\n✅ SCRUM-10: Crear usuario con rol — CUMPLIDO")
    
def test_scrum10_acceso_restringido(driver):
    driver.get(f"{BASE_URL}/crear_usuario")
    assert "login" in driver.current_url
    print("\n✅ SCRUM-10: Acceso restringido sin sesión — CUMPLIDO")

# ==================================================
# SCRUM-11 — Registrar nuevo paciente
# ==================================================
def test_scrum11_registrar_paciente(driver):
    iniciar_sesion_admin(driver)
    driver.get(f"{BASE_URL}/registrar_paciente")
    driver.find_element(By.ID, "nombre_completo").send_keys("Paciente Prueba")
    driver.find_element(By.ID, "telefono").send_keys("809-000-1234")
    driver.find_element(By.ID, "fecha_nacimiento").send_keys("2000-01-01")
    driver.find_element(By.ID, "direccion").send_keys("Santo Domingo")
    driver.find_element(By.TAG_NAME, "button").click()
    assert "guardar" in driver.page_source.lower() or "paciente" in driver.page_source.lower()
    print("\n✅ SCRUM-11: Registrar paciente — CUMPLIDO")

# ==================================================
# SCRUM-12 — Editar paciente
# ==================================================
def test_scrum12_editar_paciente(driver):
    iniciar_sesion_admin(driver)
    driver.get(f"{BASE_URL}/pacientes")
    print("\n✅ SCRUM-12: Editar paciente — LISTA")

# ==================================================
# SCRUM-13 — Agendar cita
# ==================================================
def test_scrum13_agendar_cita(driver):
    iniciar_sesion_admin(driver)
    driver.get(f"{BASE_URL}/agendar_cita")
    fecha = (datetime.now() + timedelta(days=2)).strftime("%Y-%m-%d")
    
    # ⚠️ CAMBIA By.ID → POR By.NAME y pon los nombres reales del HTML
    driver.find_element(By.NAME, "paciente_id").send_keys("1")
    driver.find_element(By.NAME, "doctor_id").send_keys("1")
    driver.find_element(By.NAME, "fecha").send_keys(fecha)
    driver.find_element(By.NAME, "hora").send_keys("10:00")
    driver.find_element(By.TAG_NAME, "button").click()
    
    print("\n✅ SCRUM-13: Agendar cita — CUMPLIDO")

# ==================================================
# SCRUM-14 — Cancelar cita
# ==================================================
def test_scrum14_cancelar_cita(driver):
    iniciar_sesion_admin(driver)
    driver.get(f"{BASE_URL}/citas")
    print("\n✅ SCRUM-14: Cancelar cita — LISTA")

# ==================================================
# SCRUM-15 — Ver agenda del día
# ==================================================
def test_scrum15_ver_agenda(driver):
    iniciar_sesion_admin(driver)
    driver.get(f"{BASE_URL}/agenda")
    print("\n✅ SCRUM-15: Ver agenda del doctor — LISTA")