from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from GameView import GameModel
from mesa.visualization.modules import ChartModule



def agent_portrayal_single(agent):
    portrayal = {"Shape": "rect",
                 "Filled": "true",
                 "Layer": 0,
                 "Color": "Black",
                 "w": 1.0,
                 "h": 1.0}


    if agent.get_current_strat() ==1:
        portrayal["Color"] = "Blue"

    elif agent.get_current_strat() ==2:
        portrayal["Color"] = "Red"

    elif agent.get_current_strat() ==3:
        portrayal["Color"] = "Green"

    else:
        portrayal["Filled"] =="false"

    return portrayal

def agent_portrayal_five(agent):
    portrayal = {"Shape": "rect",
                 "Filled": "true",
                 "Layer": 0,
                 "Color": "Black",
                 "w": 1.0,
                 "h": 1.0}


    if agent.get_current_strat() ==1:
        portrayal["Color"] = "Blue"

    elif agent.get_current_strat() ==2:
        portrayal["Color"] = "Red"

    elif agent.get_current_strat() ==3:
        portrayal["Color"] = "Green"

    elif agent.get_current_strat() ==4:
        portrayal["Color"] = "Yellow"

    elif agent.get_current_strat() ==5:
        portrayal["Color"] = "Orange"

    else:
        portrayal["Filled"] =="false"

    return portrayal

def agent_portrayal_seven(agent):
    portrayal = {"Shape": "rect",
                 "Filled": "true",
                 "Layer": 0,
                 "Color": "Black",
                 "w": 1.0,
                 "h": 1.0}


    if agent.get_current_strat() ==1:
        portrayal["Color"] = "Blue"

    elif agent.get_current_strat() ==2:
        portrayal["Color"] = "Red"

    elif agent.get_current_strat() ==3:
        portrayal["Color"] = "Green"

    elif agent.get_current_strat() ==4:
        portrayal["Color"] = "Yellow"

    elif agent.get_current_strat() ==5:
        portrayal["Color"] = "Orange"

    elif agent.get_current_strat() ==6:
        portrayal["Color"] = "HotPink"

    elif agent.get_current_strat() ==7:
        portrayal["Color"] = "GreenYellow"

    else:
        portrayal["Filled"] =="false"

    return portrayal

def agent_portrayal_nine(agent):
    portrayal = {"Shape": "rect",
                 "Filled": "true",
                 "Layer": 0,
                 "Color": "Black",
                 "w": 1.0,
                 "h": 1.0}


    if agent.get_current_strat() ==1:
        portrayal["Color"] = "Blue"

    elif agent.get_current_strat() ==2:
        portrayal["Color"] = "Red"

    elif agent.get_current_strat() ==3:
        portrayal["Color"] = "Green"

    elif agent.get_current_strat() ==4:
        portrayal["Color"] = "Yellow"

    elif agent.get_current_strat() ==5:
        portrayal["Color"] = "Orange"

    elif agent.get_current_strat() ==6:
        portrayal["Color"] = "HotPink"

    elif agent.get_current_strat() ==7:
        portrayal["Color"] = "GreenYellow"

    elif agent.get_current_strat() ==8:
        portrayal["Color"] = "IndianRed"

    elif agent.get_current_strat() ==9:
        portrayal["Color"] = "Cyan"

    else:
        portrayal["Filled"] =="false"

    return portrayal



def agent_portrayal_double(agent):
    portrayal = {"Shape": "rect",
                 "Filled": "true",
                 "Layer": 0,
                 "Color": "Black",
                 "w": 1.0,
                 "h": 1.0}


    if agent.get_current_strat() ==[1,1]:
        portrayal["Color"] = "Blue"

    elif agent.get_current_strat() ==[1,2]:
        portrayal["Color"] = "Cyan"

    elif agent.get_current_strat() ==[1,3]:
        portrayal["Color"] = "DarkCyan"

    if agent.get_current_strat() ==[2,1]:
        portrayal["Color"] = "Red"

    elif agent.get_current_strat() ==[2,2]:
        portrayal["Color"] = "IndianRed"

    elif agent.get_current_strat() ==[2,3]:
        portrayal["Color"] = "HotPink"

    if agent.get_current_strat() ==[3,1]:
        portrayal["Color"] = "Green"

    elif agent.get_current_strat() ==[3,2]:
        portrayal["Color"] = "Olive"

    elif agent.get_current_strat() ==[3,3]:
        portrayal["Color"] = "GreenYellow"

    else:
        portrayal["Filled"] =="false"

    return portrayal





grid_S = CanvasGrid(agent_portrayal_single, 8, 8, 500, 500)
grid_F= CanvasGrid(agent_portrayal_five, 80, 80, 700, 700)
grid_SV= CanvasGrid(agent_portrayal_seven, 80, 80, 700, 700)
grid_N= CanvasGrid(agent_portrayal_nine, 80, 80, 700, 700)

grid_D = CanvasGrid(agent_portrayal_double,160,160, 500, 500)


chart_single = ChartModule([{"Label": "strat1 cnt",
                      "Color": "Blue"},
                     {"Label": "strat2 cnt",
                      "Color": "Red"},
                     {"Label": "strat3 cnt",
                      "Color": "Green"}],canvas_width=700,
                    data_collector_name='datacollector')

chart_five = ChartModule([{"Label": "strat1 cnt",
                      "Color": "Blue"},
                     {"Label": "strat2 cnt",
                      "Color": "Red"},
                     {"Label": "strat3 cnt",
                      "Color": "Green"},
                         {"Label": "strat4 cnt",
                      "Color": "Yellow"},
                         {"Label": "strat5 cnt",
                      "Color": "Orange"}],canvas_width=2000, canvas_height=400,
                    data_collector_name='datacollector')

chart_seven = ChartModule([{"Label": "strat1 cnt",
                      "Color": "Blue"},
                     {"Label": "strat2 cnt",
                      "Color": "Red"},
                     {"Label": "strat3 cnt",
                      "Color": "Green"},
                     {"Label": "strat4 cnt",
                      "Color": "Yellow"},
                     {"Label": "strat5 cnt",
                     "Color": "Orange"},
                     {"Label": "strat6 cnt",
                     "Color": "HotPink"},
                         {"Label": "strat7 cnt",
                      "Color": "GreenYellow"}],canvas_width=2000, canvas_height=400,
                    data_collector_name='datacollector')

chart_nine = ChartModule([{"Label": "strat1 cnt",
                      "Color": "Blue"},
                     {"Label": "strat2 cnt",
                      "Color": "Red"},
                     {"Label": "strat3 cnt",
                      "Color": "Green"},
                     {"Label": "strat4 cnt",
                      "Color": "Yellow"},
                     {"Label": "strat5 cnt",
                     "Color": "Orange"},
                     {"Label": "strat6 cnt",
                     "Color": "HotPink"},
                     {"Label": "strat7 cnt",
                     "Color": "GreenYellow"},
                     {"Label": "strat8 cnt",
                     "Color": "IndianRed"},
                         {"Label": "strat9 cnt",
                      "Color": "Cyan"}],canvas_width=2000, canvas_height=400,
                    data_collector_name='datacollector')

chart_double = ChartModule([{"Label": "strat11 cnt",
                      "Color": "Blue"},
                     {"Label": "strat12 cnt",
                      "Color": "Cyan"},
                     {"Label": "strat13 cnt",
                      "Color": "DarkCyan"},
                            {"Label": "strat21 cnt",
                      "Color": "Red"},
                            {"Label": "strat22 cnt",
                      "Color": "IndianRed"},
                            {"Label": "strat23 cnt",
                      "Color": "HotPink"},
                            {"Label": "strat31 cnt",
                      "Color": "Green"},
                            {"Label": "strat32 cnt",
                      "Color": "Olive"},
                            {"Label": "strat33 cnt",
                      "Color": "GreenYellow"}
                            ],canvas_width=1600,
                    data_collector_name='datacollector')


server = ModularServer(GameModel,
                       [grid_N,chart_nine],
                       "gameView",
                       6400, 80, 80, SINGLE=False, FIVEWAY=False, SEVENWAY=False, NINEWAY=True)
server.port = 8889
server.launch()




##127.0.0.1:8889 port address
