import numpy as np
from skfuzzy import membership
import skfuzzy as fuzz


def fuzzy_logic(car_type_val, engine_val, price_val):
    # Define the taste variable
    car_type = np.arange(0, 101, 1)
    car_type_sport = membership.trapmf(car_type, [0, 20, 25, 34])
    car_type_comfort = membership.trapmf(car_type, [40, 50, 55, 67])
    car_type_off_road = membership.trapmf(car_type, [66, 70, 75, 100])
    car_type_fit_sport = fuzz.interp_membership(car_type, car_type_sport, car_type_val)
    car_type_fit_comfort = fuzz.interp_membership(car_type, car_type_comfort, car_type_val)
    car_type_fit_off_road = fuzz.interp_membership(car_type, car_type_off_road, car_type_val)

    # Define the cheese variable
    engine = np.arange(0, 11, 1)
    engine_petrol = fuzz.trimf(engine, [0, 2, 3])
    engine_electro = fuzz.trimf(engine, [2.5, 4, 6])
    engine_hybrid = fuzz.trimf(engine, [5.5, 8, 10])
    engine_fit_petrol = fuzz.interp_membership(engine, engine_petrol, engine_val)
    engine_fit_electro = fuzz.interp_membership(engine, engine_electro, engine_val)
    engine_fit_hybrid = fuzz.interp_membership(engine, engine_hybrid, engine_val)

    # Define the price variable
    price = np.arange(0, 101, 1)
    price_low = fuzz.trimf(price, [0, 25, 33])
    price_mid = fuzz.trimf(price, [32, 56, 66])
    price_high = fuzz.trimf(price, [65, 87, 100])
    price_fit_low = fuzz.interp_membership(price, price_low, price_val)
    price_fit_mid = fuzz.interp_membership(price, price_mid, price_val)
    price_fit_high = fuzz.interp_membership(price, price_high, price_val)

    car = np.arange(0, 1, 0.01)
    # Electric
    car_nissan_leaf = membership.trimf(car, [0, 0.05, 0.11])
    car_tesla_model_x = membership.trimf(car, [0.09, 0.20, 0.22])
    car_hyundai_kona = membership.trimf(car, [0.21, 0.30, 0.33])

    # Petrol
    car_ford_bronco = membership.trimf(car, [0.31, 0.40, 0.44])
    car_ford_mustang_2000 = membership.trimf(car, [0.43, 0.51, 0.55])
    car_kia_rio = membership.trimf(car, [0.54, 0.61, 0.66])

    # Hybrid
    car_kia_sportage = membership.trimf(car, [0.65, 0.71, 0.77])
    car_lexus_es = membership.trimf(car, [0.76, 0.84, 0.88])
    car_toyota_prius = membership.trimf(car, [0.87, 0.9, 1])

    rule1 = np.fmin(np.fmin(np.fmin(car_type_fit_sport, engine_fit_petrol), price_fit_mid), car_ford_mustang_2000)
    rule2 = np.fmin(np.fmin(np.fmin(car_type_fit_sport, engine_fit_petrol), price_fit_high), car_kia_rio)
    rule3 = np.fmin(np.fmin(np.fmin(car_type_fit_sport, engine_fit_petrol), price_fit_low), car_ford_mustang_2000)

    rule4 = np.fmin(np.fmin(np.fmin(car_type_fit_sport, engine_fit_electro), price_fit_low), car_hyundai_kona)
    rule5 = np.fmin(np.fmin(np.fmin(car_type_fit_sport, engine_fit_electro), price_fit_mid), car_hyundai_kona)
    rule6 = np.fmin(np.fmin(np.fmin(car_type_fit_sport, engine_fit_electro), price_fit_high), car_tesla_model_x)

    rule7 = np.fmin(np.fmin(np.fmin(car_type_fit_sport, engine_fit_hybrid), price_fit_low), car_toyota_prius)
    rule8 = np.fmin(np.fmin(np.fmin(car_type_fit_sport, engine_fit_hybrid), price_fit_mid), car_lexus_es)
    rule9 = np.fmin(np.fmin(np.fmin(car_type_fit_sport, engine_fit_hybrid), price_fit_high), car_lexus_es)

    rule10 = np.fmin(np.fmin(np.fmin(car_type_fit_comfort, engine_fit_petrol), price_fit_low), car_ford_mustang_2000)
    rule11 = np.fmin(np.fmin(np.fmin(car_type_fit_comfort, engine_fit_petrol), price_fit_mid), car_kia_rio)
    rule12 = np.fmin(np.fmin(np.fmin(car_type_fit_comfort, engine_fit_petrol), price_fit_high), car_kia_rio)

    rule13 = np.fmin(np.fmin(np.fmin(car_type_fit_comfort, engine_fit_electro), price_fit_low), car_nissan_leaf)
    rule14 = np.fmin(np.fmin(np.fmin(car_type_fit_comfort, engine_fit_electro), price_fit_mid), car_hyundai_kona)
    rule15 = np.fmin(np.fmin(np.fmin(car_type_fit_comfort, engine_fit_electro), price_fit_high), car_tesla_model_x)

    rule16 = np.fmin(np.fmin(np.fmin(car_type_fit_comfort, engine_fit_hybrid), price_fit_low), car_toyota_prius)
    rule17 = np.fmin(np.fmin(np.fmin(car_type_fit_comfort, engine_fit_hybrid), price_fit_mid), car_kia_sportage)
    rule18 = np.fmin(np.fmin(np.fmin(car_type_fit_comfort, engine_fit_hybrid), price_fit_high), car_lexus_es)

    rule19 = np.fmin(np.fmin(np.fmin(car_type_fit_off_road, engine_fit_petrol), price_fit_low), car_ford_mustang_2000)
    rule20 = np.fmin(np.fmin(np.fmin(car_type_fit_off_road, engine_fit_petrol), price_fit_mid), car_ford_bronco)
    rule21 = np.fmin(np.fmin(np.fmin(car_type_fit_off_road, engine_fit_petrol), price_fit_high), car_ford_bronco)

    rule22 = np.fmin(np.fmin(np.fmin(car_type_fit_off_road, engine_fit_electro), price_fit_low), car_nissan_leaf)
    rule23 = np.fmin(np.fmin(np.fmin(car_type_fit_off_road, engine_fit_electro), price_fit_mid), car_hyundai_kona)
    rule24 = np.fmin(np.fmin(np.fmin(car_type_fit_off_road, engine_fit_electro), price_fit_high), car_tesla_model_x)

    rule25 = np.fmin(np.fmin(np.fmin(car_type_fit_off_road, engine_fit_hybrid), price_fit_low), car_toyota_prius)
    rule26 = np.fmin(np.fmin(np.fmin(car_type_fit_off_road, engine_fit_hybrid), price_fit_mid), car_kia_sportage)
    rule27 = np.fmin(np.fmin(np.fmin(car_type_fit_off_road, engine_fit_hybrid), price_fit_high), car_kia_sportage)

    out_nissan_leaf = np.fmax(rule13, rule22)
    out_tesla_model_x = np.fmax(np.fmax(rule6, rule15), rule24)
    out_hyundai_kona = np.fmax(np.fmax(np.fmax(rule23, rule14), rule5), rule4)
    out_ford_bronco = np.fmax(rule20, rule21)
    out_ford_mustang_2000 = np.fmax(np.fmax(np.fmax(rule19, rule10), rule1), rule3)
    out_kia_rio = np.fmax(np.fmax(rule11, rule12), rule2)
    out_kia_sportage = np.fmax(np.fmax(rule26, rule27), rule17)
    out_lexus_es = np.fmax(np.fmax(rule18, rule9), rule8)
    out_toyota_prius = np.fmax(np.fmax(rule7, rule16), rule25)

    out_car = np.fmax(np.fmax(
        np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(out_ford_mustang_2000, out_hyundai_kona),
                                                out_kia_rio), out_kia_sportage),
                                out_lexus_es), out_toyota_prius), out_ford_bronco), out_nissan_leaf),
        out_tesla_model_x)

    defuz = fuzz.defuzz(car, out_car, 'centroid')

    if 0 < defuz <= 0.1:
        return "Nissan Leaf"
    elif 0.1 < defuz <= 0.22:
        return "Tesla model X"
    elif 0.22 < defuz <= 0.33:
        return "Hyundai Kona"
    elif 0.33 < defuz <= 0.44:
        return "Ford Bronco"
    elif 0.44 < defuz <= 0.55:
        return "Ford Mustang 2000"
    elif 0.55 < defuz <= 0.66:
        return "Kia Rio"
    elif 0.66 < defuz <= 0.77:
        return "Kia Sportage"
    elif 0.77 < defuz <= 0.88:
        return "Lexus ES"
    elif 0.88 < defuz <= 1:
        return "Toyota Prius"
