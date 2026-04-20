def is_criticality_balanced(temperature : int | float, neutrons_emitted :int | float) ->bool:
    if temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000:
        return True 
    else: 
        return False 
         

def reactor_efficiency(voltage : int | float , current : int|float, theoretical_max_power : int|float)-> str:
    generated_power = voltage * current 
    percentage_value = (generated_power/theoretical_max_power)*100
    if percentage_value >= 80 :
        return 'green'

    elif percentage_value >= 60:
        return 'orange'

    elif percentage_value >= 30 :
        return 'red' 

    else :
        return 'black'

    


def fail_safe(temperature: int | float, neutrons_produced_per_second: int | float, threshold: int | float) -> str:
    criticality = temperature * neutrons_produced_per_second

    if criticality < 0.9 * threshold:
        return 'LOW'
    elif 0.9 * threshold <= criticality <= 1.1 * threshold:
        return 'NORMAL'
    else:
        return 'DANGER'
       
    
    
  


