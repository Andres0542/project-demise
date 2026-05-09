"""
Demise Driver - Motor de Ejecucion 3D con Menu Grafico
========================================================

Driver principal con menu grafico que configura Python 3.13
y ejecuta los tests graficos 3D reales con opciones personalizables.
"""

import sys
import os
import subprocess
from pathlib import Path
from typing import List, Optional, Dict
from dataclasses import dataclass
from enum import Enum
import time
import re
import threading
import pygame

class TestMode(Enum):
    FLOORCASTING = "floorcasting_test"
    RAYCASTING = "raycasting_test"
    RAYCASTING_MAZE = "raycasting_maze_test"
    REFLEXING_FLOOR = "reflexing_floor"

@dataclass
class TestExecution:
    name: str
    script_path: str
    working_dir: str
    description: str
    process: Optional[subprocess.Popen] = None
    status: str = "pending"
    window_title: str = ""
    settings: Dict[str, str] = None

    def __post_init__(self):
        if self.settings is None:
            self.settings = {}

class Button:
    """Boton grafico para el menu"""
    def __init__(self, x, y, width, height, text, action_id):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action_id = action_id
        self.hovered = False
        # Colores celestes profesionales
        self.color = (70, 130, 180)      # Celeste oscuro
        self.hover_color = (135, 206, 250)  # Celeste claro
        self.border_color = (176, 224, 230)  # Celeste borde
        self.text_color = (240, 248, 255)  # Blanco azulado
        self.font = None
    
    def draw(self, screen, font):
        """Dibuja el boton"""
        color = self.hover_color if self.hovered else self.color
        pygame.draw.rect(screen, color, self.rect, border_radius=12)
        pygame.draw.rect(screen, self.border_color, self.rect, 3, border_radius=12)
        
        text_surface = font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
    
    def check_hover(self, mouse_pos):
        """Verifica si el mouse esta sobre el boton"""
        self.hovered = self.rect.collidepoint(mouse_pos)
    
    def is_clicked(self, mouse_pos, mouse_pressed):
        """Verifica si el boton fue clickeado"""
        return self.hovered and mouse_pressed[0]

class DemiseDriver:
    def __init__(self, config_file: str):
        self.config_file = Path(config_file)
        self.project_root = self.config_file.parent.parent
        self.test_executions: List[TestExecution] = []
        self.python313_cmd = None
        self.errors: List[str] = []
        self.settings: Dict[str, str] = {}
        self.running = True
        
    def setup_python313(self) -> bool:
        """Configura Python 3.13 con todas las dependencias"""
        print("Configurando Python 3.13...")
        
        try:
            result = subprocess.run(
                ["py", "-3.13", "--version"],
                capture_output=True,
                text=True,
                timeout=10
            )
            
            if result.returncode == 0 and "3.13" in result.stdout:
                self.python313_cmd = "py -3.13"
                print(f"Python 3.13 encontrado: {result.stdout.strip()}")
            else:
                print("Python 3.13 no encontrado")
                return False
                
        except Exception as e:
            print(f"Error verificando Python 3.13: {e}")
            return False
        
        print("Instalando dependencias...")
        
        packages = ["pygame", "numpy", "numba"]
        
        for package in packages:
            print(f"  Instalando {package}...")
            
            try:
                result = subprocess.run(
                    ["py", "-3.13", "-m", "pip", "install", package],
                    capture_output=True,
                    text=True,
                    timeout=180
                )
                
                if result.returncode == 0:
                    print(f"  {package} instalado correctamente")
                else:
                    print(f"  Fallo instalando {package}: {result.stderr[:100]}")
                    return False
                    
            except Exception as e:
                print(f"  Error instalando {package}: {e}")
                return False
        
        print("Verificando importaciones...")
        
        imports = [
            ("pygame", "import pygame; print('pygame:', pygame.version.ver)"),
            ("numpy", "import numpy; print('numpy:', numpy.__version__)"),
            ("numba", "import numba; print('numba:', numba.__version__)")
        ]
        
        for lib_name, import_cmd in imports:
            try:
                result = subprocess.run(
                    ["py", "-3.13", "-c", import_cmd],
                    capture_output=True,
                    text=True,
                    timeout=30
                )
                
                if result.returncode == 0:
                    print(f"  {lib_name}: {result.stdout.strip()}")
                else:
                    print(f"  Fallo verificacion {lib_name}")
                    return False
                    
            except Exception as e:
                print(f"  Error verificacion {lib_name}: {e}")
                return False
        
        print("Configuracion de Python 3.13 completada")
        return True
    
    def parse_settings(self, line: str) -> Dict[str, str]:
        """Parsea configuracion settings(resolucion=..., fov=..., fps=...)"""
        settings = {}
        
        if line.startswith("settings(") and line.endswith(")"):
            content = line[9:-1]
            
            pairs = content.split(",")
            for pair in pairs:
                if "=" in pair:
                    key, value = pair.split("=", 1)
                    key = key.strip()
                    value = value.strip()
                    settings[key] = value
        
        return settings
    
    def validate_settings(self, settings: Dict[str, str]) -> bool:
        """Valida que los settings sean correctos"""
        
        if "resolution" in settings:
            res = settings["resolution"]
            if not re.match(r'^\d+x\d+$', res):
                print(f"Error: Resolucion invalida: {res}. Debe ser formato anchoxalto")
                return False
            
            width, height = map(int, res.split("x"))
            if width < 320 or width > 3840 or height < 240 or height > 2160:
                print(f"Error: Resolucion fuera de rango: {res}")
                return False
        
        if "fov" in settings:
            try:
                fov = int(settings["fov"])
                if fov < 30 or fov > 120:
                    print(f"Error: FOV fuera de rango: {fov}. Debe ser 30-120")
                    return False
            except ValueError:
                print(f"Error: FOV invalido: {settings['fov']}")
                return False
        
        if "fps" in settings:
            try:
                fps = int(settings["fps"])
                if fps < 30 or fps > 120:
                    print(f"Error: FPS fuera de rango: {fps}. Debe ser 30-120")
                    return False
            except ValueError:
                print(f"Error: FPS invalido: {settings['fps']}")
                return False
        
        return True
    
    def parse_configuration(self) -> bool:
        """Parsea configuracion"""
        print(f"\nParseando: {self.config_file.name}")
        
        try:
            with open(self.config_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            test_commands = []
            current_settings = {}
            
            for line in lines:
                line = line.strip()
                if line and not line.startswith('//'):
                    
                    if line.startswith("settings("):
                        settings = self.parse_settings(line)
                        if settings:
                            if self.validate_settings(settings):
                                current_settings = settings
                                print(f"  Configuracion: {settings}")
                            else:
                                return False
                    
                    elif line in ['floorcasting_test', 'raycasting_test', 
                               'raycasting_maze_test', 'reflexing_floor']:
                        test_commands.append((line, current_settings.copy()))
                        print(f"  Test: {line}")
                        current_settings = {}
            
            self._create_test_executions(test_commands)
            print(f"Parseados: {len(test_commands)} test(s)")
            return True
            
        except Exception as e:
            self.errors.append(f"Error parseo: {e}")
            return False
    
    def _create_test_executions(self, test_commands: List):
        """Crea ejecuciones de tests"""
        test_mappings = {
            TestMode.RAYCASTING: ("Ejemplo-2 (RayCasting)/Ejercicio1-beta.py", "Raycasting basico con numba"),
            TestMode.RAYCASTING_MAZE: ("Ejemplo-2 (RayCasting)/Ejercicio2.py", "Raycasting completo con laberinto"),
            TestMode.FLOORCASTING: ("Ejemplo-1 (Floorcasting)/Ejemplo1.py", "Floorcasting basico"),
        }
        
        for test_cmd, settings in test_commands:
            test_mode = TestMode(test_cmd)
            if test_mode in test_mappings:
                script_info = test_mappings[test_mode]
                script_path = self.project_root / script_info[0]
                
                if script_path.exists():
                    self.test_executions.append(TestExecution(
                        name=test_cmd,
                        script_path=str(script_path),
                        working_dir=str(script_path.parent),
                        description=script_info[1],
                        window_title=f"Demise Engine - {test_cmd.replace('_', ' ').title()}",
                        settings=settings
                    ))
                else:
                    print(f"Advertencia: Script no encontrado: {script_path}")
    
    def execute_tests(self) -> bool:
        """Ejecuta los tests 3D"""
        print(f"\nEjecutando {len(self.test_executions)} test(s) 3D...")
        
        success_count = 0
        
        for i, test_exec in enumerate(self.test_executions):
            print(f"\n{'='*70}")
            print(f"TEST 3D {i+1}/{len(self.test_executions)}: {test_exec.name}")
            print(f"{'='*70}")
            
            print(f"Script: {test_exec.script_path}")
            print(f"Directorio: {test_exec.working_dir}")
            print(f"Descripcion: {test_exec.description}")
            print(f"Python: {self.python313_cmd}")
            
            if test_exec.settings:
                print(f"Configuracion:")
                for key, value in test_exec.settings.items():
                    print(f"  {key}: {value}")
            
            try:
                test_exec.process = subprocess.Popen(
                    ["py", "-3.13", test_exec.script_path],
                    cwd=test_exec.working_dir,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                )
                
                test_exec.status = "running"
                print(f"Proceso iniciado (PID: {test_exec.process.pid})")
                print(f"Ventana 3D abriendose...")
                
                if test_exec.settings.get("resolution"):
                    print(f"Resolucion: {test_exec.settings['resolution']}")
                else:
                    print(f"Resolucion: 800x600 (por defecto)")
                
                time.sleep(3)
                
                if test_exec.process.poll() is None:
                    print(f"Renderizado 3D activo!")
                    print(f"Graficos 3D reales ejecutandose!")
                    success_count += 1
                    
                    print(f"\nControles:")
                    print(f"   W/Flecha arriba - Avanzar")
                    print(f"   S/Flecha abajo - Retroceder")
                    print(f"   A/Flecha izquierda - Izquierda")
                    print(f"   D/Flecha derecha - Derecha")
                    print(f"   Mouse - Mirar alrededor")
                    print(f"   ESC - Salir")
                    
                    print(f"\nInteractua con la ventana 3D!")
                    print(f"Ejecutando por 60 segundos...")
                    
                    try:
                        test_exec.process.wait(timeout=60)
                        print(f"Test completado normalmente")
                    except subprocess.TimeoutExpired:
                        print(f"Tiempo agotado, terminando...")
                        test_exec.process.terminate()
                        try:
                            test_exec.process.wait(timeout=10)
                        except subprocess.TimeoutExpired:
                            test_exec.process.kill()
                            test_exec.process.wait(timeout=5)
                        print(f"Test terminado")
                    
                    test_exec.status = "completed"
                else:
                    stdout, stderr = test_exec.process.communicate()
                    print(f"Test fallido:")
                    print(f"   {stderr}")
                    self.errors.append(f"Test {test_exec.name} fallido: {stderr}")
                    test_exec.status = "failed"
                
            except Exception as e:
                print(f"Error ejecucion: {e}")
                self.errors.append(f"Error ejecucion: {e}")
                test_exec.status = "error"
        
        return success_count > 0
    
    def run(self) -> bool:
        """Ejecuta todo el proceso"""
        print("""
========================================================================
                    DEMISE DRIVER v7.0
              Python 3.13 + Ejecucion 3D Completa
========================================================================
        """)
        
        if not self.parse_configuration():
            print("Fallo al parsear configuracion")
            return False
        
        if not self.setup_python313():
            print("Fallo al configurar Python 3.13")
            return False
        
        return self.execute_tests()

def show_graphic_menu(custom_settings: Dict[str, str]) -> Optional[str]:
    """Muestra el menu grafico interactivo con pygame"""
    
    # Inicializar pygame
    pygame.init()
    
    # Configurar ventana
    WIDTH, HEIGHT = 900, 700
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Demise Driver - Menu Principal")
    
    # Configurar fuentes
    try:
        font_large = pygame.font.Font(None, 52)
        font_medium = pygame.font.Font(None, 36)
        font_small = pygame.font.Font(None, 28)
    except:
        font_large = pygame.font.SysFont('Arial', 52)
        font_medium = pygame.font.SysFont('Arial', 36)
        font_small = pygame.font.SysFont('Arial', 28)
    
    # Crear botones con nombres exactos
    button_width = 350
    button_height = 55
    start_x = (WIDTH - button_width) // 2
    start_y = 120
    gap = 75
    
    buttons = [
        Button(start_x, start_y, button_width, button_height, "RayCasting", "1"),
        Button(start_x, start_y + gap, button_width, button_height, "FloorCasting", "2"),
        Button(start_x, start_y + gap * 2, button_width, button_height, "MAZE", "3"),
        Button(start_x, start_y + gap * 3, button_width, button_height, "Cambiar Resolucion", "4"),
        Button(start_x, start_y + gap * 4, button_width, button_height, "Cambiar FOV", "5"),
        Button(start_x, start_y + gap * 5, button_width, button_height, "FPS Cap", "6"),
        Button(start_x, start_y + gap * 6, button_width, button_height, "Salir", "0"),
    ]
    
    # Mostrar configuracion actual
    def show_current_settings():
        y_offset = 640
        if custom_settings:
            text = f"Configuracion: {custom_settings}"
        else:
            text = "Configuracion: Por defecto"
        text_surf = font_small.render(text, True, (176, 224, 230))
        screen.blit(text_surf, (20, y_offset))
    
    clock = pygame.time.Clock()
    running = True
    
    while running:
        # Fondo celeste profesional
        screen.fill((25, 35, 45))
        
        # Manejar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Click izquierdo
                    mouse_pos = pygame.mouse.get_pos()
                    mouse_pressed = pygame.mouse.get_pressed()
                    
                    for button in buttons:
                        if button.is_clicked(mouse_pos, mouse_pressed):
                            pygame.quit()
                            return button.action_id
        
        # Obtener posicion del mouse
        mouse_pos = pygame.mouse.get_pos()
        
        # Actualizar estado hover de botones
        for button in buttons:
            button.check_hover(mouse_pos)
        
        # Dibujar titulo
        title = font_large.render("DEMISE DRIVER", True, (135, 206, 250))
        title_rect = title.get_rect(center=(WIDTH // 2, 50))
        screen.blit(title, title_rect)
        
        subtitle = font_small.render("Selecciona una opcion para ejecutar", True, (176, 224, 230))
        subtitle_rect = subtitle.get_rect(center=(WIDTH // 2, 85))
        screen.blit(subtitle, subtitle_rect)
        
        # Dibujar botones
        for button in buttons:
            button.draw(screen, font_medium)
        
        # Mostrar configuracion actual
        show_current_settings()
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    return None

def show_input_dialog(title: str, prompt: str, default: str = "") -> Optional[str]:
    """Muestra un dialogo de input grafico"""
    pygame.init()
    
    WIDTH, HEIGHT = 600, 350
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(title)
    
    try:
        font_title = pygame.font.Font(None, 40)
        font_prompt = pygame.font.Font(None, 28)
        font_input = pygame.font.Font(None, 32)
        font_help = pygame.font.Font(None, 24)
    except:
        font_title = pygame.font.SysFont('Arial', 40)
        font_prompt = pygame.font.SysFont('Arial', 28)
        font_input = pygame.font.SysFont('Arial', 32)
        font_help = pygame.font.SysFont('Arial', 24)
    
    input_text = default
    active = True
    
    clock = pygame.time.Clock()
    
    while active:
        # Fondo celeste profesional
        screen.fill((25, 35, 45))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.quit()
                    return input_text if input_text else None
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return None
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode
        
        # Dibujar titulo
        title_surf = font_title.render(title, True, (135, 206, 250))
        title_rect = title_surf.get_rect(center=(WIDTH // 2, 60))
        screen.blit(title_surf, title_rect)
        
        # Dibujar prompt
        prompt_surf = font_prompt.render(prompt, True, (176, 224, 230))
        prompt_rect = prompt_surf.get_rect(center=(WIDTH // 2, 120))
        screen.blit(prompt_surf, prompt_rect)
        
        # Dibujar caja de input
        input_rect = pygame.Rect(100, 160, 400, 50)
        pygame.draw.rect(screen, (70, 130, 180), input_rect, border_radius=8)
        pygame.draw.rect(screen, (176, 224, 230), input_rect, 3, border_radius=8)
        
        # Dibujar texto de input
        text_surf = font_input.render(input_text, True, (240, 248, 255))
        text_rect = text_surf.get_rect(center=input_rect.center)
        screen.blit(text_surf, text_rect)
        
        # Dibujar instrucciones
        help_surf = font_help.render("ENTER: Aceptar | ESC: Cancelar", True, (135, 206, 250))
        help_rect = help_surf.get_rect(center=(WIDTH // 2, 260))
        screen.blit(help_surf, help_rect)
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    return None

def modify_resolution_graphic() -> Optional[str]:
    """Dialogo grafico para modificar resolucion"""
    return show_input_dialog("Cambiar Resolucion", "Formato: anchoxalto (ej: 1920x1080)", "1920x1080")

def modify_fov_graphic() -> Optional[str]:
    """Dialogo grafico para modificar FOV"""
    return show_input_dialog("Cambiar FOV", "Campo de vision en grados (30-120)", "90")

def modify_fps_graphic() -> Optional[str]:
    """Dialogo grafico para modificar FPS Cap"""
    return show_input_dialog("FPS Cap", "Limite de FPS (30-120)", "60")

def run_with_menu():
    """Ejecuta el driver con menu grafico"""
    custom_settings = {}
    
    while True:
        choice = show_graphic_menu(custom_settings)
        
        if choice is None or choice == '0':
            print("Saliendo del menu...")
            break
        
        elif choice == '1':
            print("Ejecutando RayCasting...")
            config_file = "../Ejemplo-2 (RayCasting)/Ejercicio1.txt"
            run_test(config_file, custom_settings)
            
        elif choice == '2':
            print("Ejecutando FloorCasting...")
            config_file = "../Ejemplo-1 (Floorcasting)/Ejemplo1.txt"
            run_test(config_file, custom_settings)
            
        elif choice == '3':
            print("Ejecutando MAZE...")
            config_file = "../Ejemplo-2 (RayCasting)/Ejercicio2.txt"
            run_test(config_file, custom_settings)
            
        elif choice == '4':
            res = modify_resolution_graphic()
            if res and re.match(r'^\d+x\d+$', res):
                width, height = map(int, res.split("x"))
                if 320 <= width <= 3840 and 240 <= height <= 2160:
                    custom_settings['resolution'] = res
                    print(f"Resolucion configurada: {res}")
                else:
                    print("Error: Valores fuera de rango")
            elif res:
                print("Error: Formato invalido")
                
        elif choice == '5':
            fov = modify_fov_graphic()
            if fov:
                try:
                    fov_int = int(fov)
                    if 30 <= fov_int <= 120:
                        custom_settings['fov'] = fov
                        print(f"FOV configurado: {fov_int}")
                    else:
                        print("Error: FOV fuera de rango")
                except ValueError:
                    print("Error: Valor invalido")
                    
        elif choice == '6':
            fps = modify_fps_graphic()
            if fps:
                try:
                    fps_int = int(fps)
                    if 30 <= fps_int <= 120:
                        custom_settings['fps'] = fps
                        print(f"FPS Cap configurado: {fps_int}")
                    else:
                        print("Error: FPS fuera de rango")
                except ValueError:
                    print("Error: Valor invalido")
    
    print("Menu cerrado. Adios!")

def run_test(config_file: str, custom_settings: Dict[str, str]):
    """Ejecuta un test con configuracion personalizada"""
    try:
        # Determinar el script correcto basado en el archivo de configuracion
        config_path = Path(config_file)
        config_name = config_path.stem
        
        # Mapeo de archivos de configuracion a scripts
        script_mapping = {
            "Ejercicio1": "Ejercicio1-beta.py",
            "Ejercicio2": "Ejercicio2.py",
            "Ejemplo1": "Ejemplo1.py"
        }
        
        # Determinar el directorio y script
        if "Ejemplo-2" in str(config_path):
            script_dir = config_path.parent
            script_name = script_mapping.get(config_name, "Ejercicio1-beta.py")
        elif "Ejemplo-1" in str(config_path):
            script_dir = config_path.parent
            script_name = script_mapping.get(config_name, "Ejemplo1.py")
        else:
            # Usar el mapeo del driver
            temp_driver = DemiseDriver(config_file)
            if temp_driver.test_executions:
                script_dir = Path(temp_driver.test_executions[0].working_dir)
                script_name = Path(temp_driver.test_executions[0].script_path).name
            else:
                script_dir = config_path.parent
                script_name = "Ejercicio1-beta.py"
        
        script_path = script_dir / script_name
        temp_script_path = None
        
        # Inicializar driver para configuracion de Python
        driver = DemiseDriver(config_file)
        
        if custom_settings:
            driver.settings = custom_settings.copy()
            
            if script_path.exists():
                temp_script_path = script_path.parent / (script_path.stem + "_temp" + script_path.suffix)
                
                try:
                    # Leer script original
                    with open(script_path, 'r', encoding='utf-8') as f:
                        script_content = f.read()
                    
                    # Modificar valores hardcodeados en el script
                    modified_content = script_content
                    
                    if 'resolution' in custom_settings:
                        res = custom_settings['resolution']
                        width, height = map(int, res.split('x'))
                        # Buscar y reemplazar set_mode(800, 600)
                        modified_content = re.sub(r'set_mode\(\s*\d+\s*,\s*\d+\s*\)', f'set_mode({width}, {height})', modified_content)
                        # También buscar otros patrones comunes
                        modified_content = re.sub(r'800\s*,\s*600', f'{width}, {height}', modified_content)
                        modified_content = re.sub(r'120\s*,\s*200', f'{width//6}, {height//3}', modified_content)
                    
                    if 'fov' in custom_settings:
                        fov = custom_settings['fov']
                        # Buscar y reemplazar FOV/fov/field_of_view
                        modified_content = re.sub(r'fov\s*=\s*\d+\.?\d*', f'fov = {fov}', modified_content)
                        modified_content = re.sub(r'FOV\s*=\s*\d+\.?\d*', f'FOV = {fov}', modified_content)
                        # Buscar valor de FOV en grados (comunmente 60)
                        modified_content = re.sub(r'np\.deg2rad\(60\)', f'np.deg2rad({fov})', modified_content)
                        modified_content = re.sub(r'np\.deg2rad\(90\)', f'np.deg2rad({fov})', modified_content)
                    
                    if 'fps' in custom_settings:
                        fps = custom_settings['fps']
                        # Buscar y reemplazar clock.tick(60)
                        modified_content = re.sub(r'clock\.tick\(\s*\d+\s*\)', f'clock.tick({fps})', modified_content)
                    
                    # Escribir script temporal
                    with open(temp_script_path, 'w', encoding='utf-8') as f:
                        f.write(modified_content)
                    
                    # Usar script temporal
                    script_path = temp_script_path
                    print(f"Configuracion personalizada aplicada al script")
                    
                except Exception as e:
                    print(f"Error aplicando configuracion al script: {e}")
        
        # Ejecutar con el script modificado
        if temp_script_path:
            # Usar el script temporal directamente
            try:
                test_exec = TestExecution(
                    name="custom_test",
                    script_path=str(script_path),
                    working_dir=str(script_path.parent),
                    description="Test con configuracion personalizada",
                    window_title="Demise Engine - Custom Config",
                    settings=custom_settings.copy()
                )
                
                # Configurar Python 3.13
                if not driver.setup_python313():
                    print("Fallo al configurar Python 3.13")
                    return False
                
                # Ejecutar directamente
                test_exec.process = subprocess.Popen(
                    ["py", "-3.13", script_path],
                    cwd=str(script_path.parent),
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                )
                
                test_exec.status = "running"
                print(f"Proceso iniciado (PID: {test_exec.process.pid})")
                print(f"Ventana 3D abriendose...")
                
                if custom_settings.get("resolution"):
                    print(f"Resolucion: {custom_settings['resolution']}")
                if custom_settings.get("fov"):
                    print(f"FOV: {custom_settings['fov']} grados")
                if custom_settings.get("fps"):
                    print(f"FPS Cap: {custom_settings['fps']}")
                
                time.sleep(3)
                
                if test_exec.process.poll() is None:
                    print(f"Renderizado 3D activo con configuracion personalizada!")
                    
                    print(f"\nControles:")
                    print(f"   W/Flecha arriba - Avanzar")
                    print(f"   S/Flecha abajo - Retroceder")
                    print(f"   A/Flecha izquierda - Izquierda")
                    print(f"   D/Flecha derecha - Derecha")
                    print(f"   Mouse - Mirar alrededor")
                    print(f"   ESC - Salir")
                    
                    print(f"\nEjecutando por 60 segundos...")
                    
                    try:
                        test_exec.process.wait(timeout=60)
                        print(f"Test completado normalmente")
                    except subprocess.TimeoutExpired:
                        print(f"Tiempo agotado, terminando...")
                        test_exec.process.terminate()
                        try:
                            test_exec.process.wait(timeout=10)
                        except subprocess.TimeoutExpired:
                            test_exec.process.kill()
                            test_exec.process.wait(timeout=5)
                        print(f"Test terminado")
                    
                    test_exec.status = "completed"
                    print("EXITO! Test completado con configuracion personalizada")
                else:
                    stdout, stderr = test_exec.process.communicate()
                    print(f"Test fallido:")
                    print(f"   {stderr}")
                    
            except Exception as e:
                print(f"Error ejecucion: {e}")
        else:
            # Ejecutar normal sin configuracion
            driver = DemiseDriver(config_file)
            success = driver.run()
            
            if success:
                print("EXITO! Test completado")
            else:
                print("Fallo en el test")
        
        # Limpiar archivo temporal si existe
        if temp_script_path and temp_script_path.exists():
            try:
                temp_script_path.unlink()
            except:
                pass
            
    except Exception as e:
        print(f"Error: {e}")

def main():
    """Funcion principal con menu interactivo"""
    print("""
========================================================================
                    DEMISE DRIVER v7.0
              Python 3.13 + Menu Interactivo + Ejecucion 3D
========================================================================
    """)
    
    # Si se pasa argumento, ejecutar directamente
    if len(sys.argv) >= 2:
        config_file = sys.argv[1]
        try:
            driver = DemiseDriver(config_file)
            success = driver.run()
            
            print(f"\n{'='*70}")
            print("RESUMEN FINAL")
            print(f"{'='*70}")
            print(f"Python: 3.13.13")
            print(f"Paquetes: pygame, numpy, numba")
            print(f"Modo: EJECUCION 3D REAL")
            print(f"Tests: {len(driver.test_executions)}")
            print(f"Graficos: VENTANAS 3D REALES")
            
            if success:
                print(f"\nGraficos 3D ejecutados")
            else:
                print(f"\nFallo de ejecucion!")
                if driver.errors:
                    print(f"Errores:")
                    for error in driver.errors:
                        print(f"  - {error}")
                sys.exit(1)
                
        except Exception as e:
            print(f"Error fatal: {e}")
            import traceback
            traceback.print_exc()
            sys.exit(1)
    else:
        # Si no hay argumentos, mostrar menu interactivo
        run_with_menu()

if __name__ == "__main__":
    main()
