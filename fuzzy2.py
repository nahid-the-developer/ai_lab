import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# import skfuzzy as fuzz
# from skfuzzy import control as ctrl

# create fuzzy variables and their ranges
quality = ctrl.Antecedent(np.arange(0, 11, 1), 'quality')
service = ctrl.Antecedent(np.arange(0, 11, 1), 'service')
tip = ctrl.Consequent(np.arange(0, 26, 1), 'tip')

# define membership function for quality and service
quality['poor'] = fuzz.trimf(quality.universe, [0, 0, 5])
quality['average'] = fuzz.trimf(quality.universe, [0, 5, 10])
quality['excellent'] = fuzz.trimf(quality.universe, [5, 10, 10])

service['poor'] = fuzz.trimf(service.universe, [0, 0, 5])
service['average'] = fuzz.trimf(service.universe, [0, 5, 10])
service['excellent'] = fuzz.trimf(service.universe, [5, 10, 10])

# define membership function for tip
tip['low'] = fuzz.trimf(tip.universe, [0, 0, 13])
tip['medium'] = fuzz.trimf(tip.universe, [0, 13, 25])
tip['high'] = fuzz.trimf(tip.universe, [13, 25, 25])

# define fuzzy rules
rule1 = ctrl.Rule(quality['poor'] | service['poor'], tip['low'])
rule2 = ctrl.Rule(service['average'], tip['medium'])
rule3 = ctrl.Rule(quality['excellent'] | service['excellent'], tip['high'])

# create fuzzy control system
tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])

# create a simulation
tipping = ctrl.ControlSystemSimulation(tipping_ctrl)

# Input values
tipping.input['quality'] = 6.5
tipping.input['service'] = 9.8

# compute the tipping result
tipping.compute()

# Output tip
print("Recommended Tip:", tipping.output['tip'])

# visualize membership function and the output
quality.view()
service.view()
tip.view()
