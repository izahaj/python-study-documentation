
#TODO: define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2



#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time:int) -> int:
    """Calculate bake_time_remaining.
    :param elapsed_bake_time :int - the time which has passed in baking
    :return :int - time left in baking
    
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time
 


#TODO: Define the 'preparation_time_in_minutes()' function below.
def preparation_time_in_minutes(layers:int) -> int:
    """Calculate preparation_time_in_minutes.
    :param layers :int
    :return :int
    
    """
    return layers * PREPARATION_TIME



#TODO: define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(layers:int,elapsed_bake_time:int)-> int:
    """Calculate elapsed_time_in_minutes.
    :param layers :int
    :param elapased_bake_time :int
    :return :int
    """
    return preparation_time_in_minutes(layers) + elapsed_bake_time




# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
