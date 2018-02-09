"""
Cookie Clicker Simulator
"""

import simpleplot
import math

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

import poc_clicker_provided as provided

# Constants
SIM_TIME = 10000000000.0

class ClickerState:
    """
    Simple class to keep track of the game state.
    """
    
    def __init__(self):
        self._history_cookies_produced = 0.0
        self._current_cookies = 0.0
        self._cps = 1.0
        self._time = 0.0
        self._history_events = [(0.0, None, 0.0, 0.0)]
        
    def __str__(self):
        """
        Return human readable state
        """
        return "Time: " + str(self._time) + " Current Cookies: " + str(self._current_cookies) + " CPS: " + str(self._cps) + "Total Cookies: " + str(self._history_cookies_produced) + " History (length: " + str(len(self._history_events)) + "): " + str(self._history_events)
        
    def get_cookies(self):
        """
        Return current number of cookies 
        (not total number of cookies)
        
        Should return a float
        """
        return self._current_cookies
    
    def get_cps(self):
        """
        Get current CPS
        Should return a float
        """
        return self._cps
    
    def get_time(self):
        """
        Get current time
        Should return a float
        """
        return self._time
    
    def get_history(self):
        """
        Return history list
        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)
        For example: [(0.0, None, 0.0, 0.0)]
        Should return a copy of any internal data structures,
        so that they will not be modified outside of the class.
        """
        return self._history_events[:]

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0.0 if you already have enough cookies)
        Should return a float with no fractional part
        """
        if cookies < self._current_cookies:
            return 0.0
        else:
            cookies_required = cookies - self._current_cookies
            time_required = cookies_required / self._cps
            return time_required
    
    def wait(self, time):
        """
        Wait for given amount of time and update state
        Should do nothing if time <= 0.0
        """
        if time > 0.0:
            cookies_produced = time * self._cps
            self._current_cookies += cookies_produced
            self._history_cookies_produced += cookies_produced
            self._time += time

    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state
        Should do nothing if you cannot afford the item
        """
        if self._current_cookies >= cost:
            self._history_events.append((self._time, item_name, cost, self._history_cookies_produced))
            self._cps += additional_cps
            self._current_cookies -= cost

def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to the final state of the game.
    """
    #pdb.set_trace()
    game_state = ClickerState()
    game_information = build_info.clone()

    while game_state.get_time() <= duration:
        production_method_to_buy = strategy(game_state.get_cookies(), game_state.get_cps(), game_state.get_history(), duration - game_state.get_time(), game_information)
        if production_method_to_buy == None:
            break
        necessary_cookies = game_information.get_cost(production_method_to_buy) #- game_state.get_cookies()
        if necessary_cookies - game_state.get_cookies() > 0.0:
            # don't have necessary cookies. get them
            necessary_time = math.ceil(game_state.time_until(necessary_cookies))
            #necessary_time = math.ceil(game_state.get_time() + necessary_time) - game_state.get_time()
            if duration < game_state.get_time() + necessary_time:
                break
            game_state.wait(necessary_time)
        # have necessary cookies. update state
        game_state.buy_item(production_method_to_buy, game_information.get_cost(production_method_to_buy), game_information.get_cps(production_method_to_buy))
        game_information.update_item(production_method_to_buy)


    # go to end of time and buy everything you can with the remaining cookies
    remaining_time = duration - game_state.get_time()
    game_state.wait(math.ceil(remaining_time))

    return game_state


def strategy_cursor_broken(cookies, cps, history, time_left, build_info):
    """
    Always pick Cursor!
    Note that this simplistic (and broken) strategy does not properly
    check whether it can actually buy a Cursor in the time left.  Your
    simulate_clicker function must be able to deal with such broken
    strategies.  Further, your strategy functions must correctly check
    if you can buy the item in the time left and return None if you
    can't.
    """
    return "Cursor"

def strategy_none(cookies, cps, history, time_left, build_info):
    """
    Always return None
    This is a pointless strategy that will never buy anything, but
    that you can use to help debug your simulate_clicker function.
    """
    return None


def strategy_cheap(cookies, cps, history, time_left, build_info):
    """
    Always buy the cheapest item you can afford in the time left.
    """
    methods = []
    for method in build_info.build_items():
        methods.append((method, build_info.get_cost(method)))
    methods_by_cost = sorted(methods, key=lambda x:x[1])
    cheapest_method = methods_by_cost[0]
    if cheapest_method[1] <= cookies + cps * time_left:
        return cheapest_method[0]

def strategy_expensive(cookies, cps, history, time_left, build_info):
    """
    Always buy the most expensive item you can afford in the time left.
    """
    methods = []
    for method in build_info.build_items():
        methods.append((method, build_info.get_cost(method)))
    methods_by_value = sorted(methods, key=lambda x:x[1], reverse=True)
    for method in methods_by_value:
        if method[1] <= cookies + cps * time_left:
            return method[0]

def strategy_best(cookies, cps, history, time_left, build_info):
    """
    The best strategy that you are able to implement.
    """
    methods = []
    for method in build_info.build_items():
        method_cps = build_info.get_cps(method)
        method_cost = build_info.get_cost(method)
        methods.append((method, method_cps, method_cost, method_cps/method_cost))
    methods_by_opt_ratio = sorted(methods, key=lambda x: x[3], reverse= True)
    for method in methods_by_opt_ratio:
        method_cost = method[2]
        if method_cost <= cookies + cps * time_left:
            return method[0]

def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation for the given time with one strategy.
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print strategy_name, ":", state

    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    # history = state.get_history()
    # history = [(item[0], item[3]) for item in history]
    # simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)

def run():
    """
    Run the simulator.
    """    
    #run_strategy("Cursor", SIM_TIME, strategy_cursor_broken)
    #state = simulate_clicker(BuildInfo({'Cursor': [15.0, 0.10000000000000001]}, 1.15), 500.0, strategy_cursor_broken)
    simulate_clicker(provided.BuildInfo({'Cursor': [15.0, 50.0]}, 1.15), 16.0, strategy_cursor_broken)
    #print state.get_cps()
    #print state._history_cookies_produced
    # Add calls to run_strategy to run additional strategies
    # run_strategy("Cheap", SIM_TIME, strategy_cheap)
    # run_strategy("Expensive", SIM_TIME, strategy_expensive)
    # run_strategy("Best", SIM_TIME, strategy_best)
    
#run()
