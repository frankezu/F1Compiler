# casos_prueba.py
from src.tools.herramientas_lexer import mostrar_tokens

# ── Prueba 1: Tipos de Datos y Setup (Cumple B1 y B5)
prueba_1 = """
green_light
    // Demostrando el uso de los 4 tipos de datos
    compound current_tyre = "Hard";
    telemetry fuel_load = 105.5;
    laps remaining = 50;
    steward_decision is_wet = red_flag;
    
    engineer_says(current_tyre);
    engineer_says(fuel_load);
chequered_flag
"""

# ── Prueba 2: Estrategia Lógica y Ciclo While (Cumple B4 y parte de B2)
prueba_2 = """
green_light
    laps sector = 1;
    steward_decision safety_car = track_clear;

    // Uso de múltiples operadores lógicos (AND / OR)
    if_pitwall_says (sector matched_delta 1 or_box_opposite safety_car matched_delta track_clear) {
        engineer_says("Caution in Sector 1. Delta positive.");
    } otherwise_box {
        engineer_says("Push hard, track is green.");
    }

    keep_pushing_while (sector slower_than 3) {
        sector = sector throttle 1;
    }
chequered_flag
"""

# ── Prueba 3: Stint de Carrera, Precedencia y Funciones (Cumple B2, B3 y B6)
prueba_3 = """
green_light
    telemetry base_pace = 85.5;
    
    // Demostrando precedencia matemática: la multiplicación y división se calculan antes
    // Equivalente a: 85.5 + (2.0 * 1.5)
    telemetry expected_pace = base_pace throttle 2.0 catch_slipstream 1.5; 
    
    // Uso de la 4ta función matemática
    telemetry undercut_time = calculate_undercut_delta(expected_pace);
    engineer_says(undercut_time);

    // Demostrando la 2da estructura repetitiva (Equivalente a FOR)
    start_new_stint (laps current_lap = 1 up_to_lap 5) {
        // Simulando quema de combustible (división / resta)
        base_pace = base_pace brake 0.2; 
    }
chequered_flag
"""

if __name__ == "__main__":
    pruebas = [
        ("Prueba 1 — Tipos de Datos y Setup",              prueba_1),
        ("Prueba 2 — Estrategia Lógica (OR/AND) y WHILE",  prueba_2),
        ("Prueba 3 — Ciclo FOR, Precedencia y Funciones",  prueba_3),
    ]

    for nombre, codigo in pruebas:
        print("\n" + "=" * 90)
        print(f"  {nombre}")
        print("=" * 90)
        mostrar_tokens(codigo)