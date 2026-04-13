def eat_ghost(power_pellet_active:bool, touching_ghost:bool)-> bool:
    """
    :param power_pellet_active :bool
    :param touching_ghost :bool
    :return :bool
    """
    return  power_pellet_active and touching_ghost

    
def score(touching_power_pellet: bool, touching_dot:bool):
    """
    :param touching_power_pellet: bool
    :param touching_dot : bool
    :return :bool
    """
    return touching_power_pellet or touching_dot 

def lose(power_pellet_active:bool, touching_ghost:bool)-> bool:
    """
    :param power_pellet_active :bool
    :param touching_ghost : bool
    :return :bool
    """
    return touching_ghost and not power_pellet_active


def win(has_eaten_all_dots, power_pellet_active, touching_ghost)-> bool:
    """
    :param has_eaten_all_dots :bool
    :param power_pellet_active :bool
    :param touching_ghost :bool
    :return :bool 
    """
    return has_eaten_all_dots and not lose(power_pellet_active,touching_ghost)
  
   
  
    
    



