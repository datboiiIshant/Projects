class HeatExchanger:
    def __init__(self, inlet_temperature: float, outlet_temperature: float, heat_capacity: float, mass_flow_rate: float):
        # Verifying that none of the parameters are negative or zero.
        if inlet_temperature <= 0 or outlet_temperature <= 0 or heat_capacity <= 0 or mass_flow_rate <= 0:
            raise ValueError("Parameters should be positive and non-zero.")

        # Assigning the parameters to the instance variables.
        self.inlet_temperature = inlet_temperature
        self.outlet_temperature = outlet_temperature
        self.heat_capacity = heat_capacity
        self.mass_flow_rate = mass_flow_rate

    def calculate_heat_transfer(self):
        # Calculate the heat transfer using the formula: Q = m * Cp * (T_outlet - T_inlet)
        heat_transfer = self.mass_flow_rate * self.heat_capacity * (self.outlet_temperature - self.inlet_temperature)

        return heat_transfer

    def optimize_heat_exchanger(self, target_heat_transfer: float):
        # Calculate the required mass flow rate using the formula: m = Q / (Cp * (T_outlet - T_inlet))
        required_mass_flow_rate = target_heat_transfer / (self.heat_capacity * (self.outlet_temperature - self.inlet_temperature))

        return required_mass_flow_rate

# Example usage of the HeatExchanger class:

# Initializing a heat exchanger with given parameters
heat_exchanger = HeatExchanger(100, 200, 4.18, 10)

# Calculating the heat transfer required to achieve the desired outlet temperature
heat_transfer = heat_exchanger.calculate_heat_transfer()
print(f"The heat transfer required in the heat exchanger is {heat_transfer}.")

# Optimizing the heat exchanger to achieve a target heat transfer
target_heat_transfer = 500
required_mass_flow_rate = heat_exchanger.optimize_heat_exchanger(target_heat_transfer)
print(f"The required mass flow rate to achieve a heat transfer of {target_heat_transfer} is {required_mass_flow_rate}.")