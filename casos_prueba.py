# casos_prueba.py
from herramientas_lexer import mostrar_tokens

# ── Prueba 1: Setup Básico (Declaraciones e Impresión)
prueba_1 = """
green_light
    laps remaining = 10;
    telemetry fuel_load = 105.5;
    engineer_says(remaining);
    engineer_says(fuel_load);
chequered_flag
"""

# ── Prueba 2: Estrategia de Control (Condicionales y Ciclos)
prueba_2 = """
green_light
    laps sector = 1;
    if_pitwall_says (sector matched_delta 1) {
        engineer_says("Push in Sector 1");
    } otherwise_box {
        engineer_says("Save tyres in Sector 2");
    }

    keep_pushing_while (sector slower_than 3) {
        sector = sector throttle 1;
    }
chequered_flag
"""

# ── Prueba 3: Cálculo de Telemetría (Matemáticas y Lógica)
prueba_3 = """
green_light
    telemetry speed = 320.5;
    telemetry speed_sqrt = tyre_wear_calc(speed);
    steward_decision safety_car = track_clear and_drs_open red_flag;
    steward_decision penalty = telemetry_denies track_clear;
    engineer_says(speed_sqrt);
chequered_flag
"""

if __name__ == "__main__":
    pruebas = [
        ("Prueba 1 — Setup Básico",                        prueba_1),
        ("Prueba 2 — Estrategia de Control",               prueba_2),
        ("Prueba 3 — Telemetría y Decisiones",             prueba_3),
    ]

    for nombre, codigo in pruebas:
        print("\n" + "=" * 80)
        print(f"  {nombre}")
        print("=" * 80)
        mostrar_tokens(codigo)