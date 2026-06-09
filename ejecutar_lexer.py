# ejecutar_lexer.py
from herramientas_lexer import mostrar_tokens, contar_tokens_por_tipo

programa_ejemplo = """
green_light

    // 1. Setup de la carrera y telemetría inicial
    laps current_lap = 1;
    laps total_laps = 5;
    telemetry tyre_temp = 90.5;
    steward_decision drs_enabled = red_flag; // Falso al inicio (DRS desactivado)
    compound neumatico = "Soft";

    engineer_says("Lights out and away we go!");

    // 2. Ciclo principal de la carrera
    keep_pushing_while (current_lap slower_than total_laps) {

        engineer_says("Lap number:");
        engineer_says(current_lap);

        // Activación de DRS después de la vuelta 2
        if_pitwall_says (current_lap faster_than 2) {
            drs_enabled = track_clear;
        }

        // Simulamos degradación de temperatura
        tyre_temp = tyre_temp throttle 4.5;

        // Estrategia condicional basada en telemetría
        if_pitwall_says (tyre_temp faster_than 100.0 and_drs_open drs_enabled matched_delta track_clear) {
            engineer_says("Box, box. Tyres overheating and DRS is active.");
            tyre_temp = tyre_temp brake 15.0; // Refrescamos neumáticos
        } otherwise_box {
            engineer_says("Pace is good. Keep pushing.");
        }

        // Avanzamos de vuelta
        current_lap = current_lap throttle 1;
    }

    // 3. Análisis Post-Carrera (Funciones matemáticas)
    telemetry delta_time = tyre_wear_calc(16);
    telemetry steering_angle = calc_steering(45.0);
    telemetry ers_battery = deploy_ers(2, 3);

    engineer_says("Race finished. Final ERS deployment level:");
    engineer_says(ers_battery);

chequered_flag
"""

if __name__ == "__main__":
    print(f"Programa de ejemplo definido ({len(programa_ejemplo)} caracteres).")
    print("=" * 80)
    print("ANÁLISIS LÉXICO — Lista completa de tokens")
    print("=" * 80)
    mostrar_tokens(programa_ejemplo)

    print("\n" + "=" * 80)
    print("RESUMEN DE TOKENS POR TIPO")
    print("=" * 80)
    contar_tokens_por_tipo(programa_ejemplo)