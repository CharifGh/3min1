from operator import attrgetter


def make_groups(district):
    """Finds the five houses closest to the five starting points"""
    start_coords = [
        {'x': 0, 'y': 0},
        {'x': 0, 'y': 50},
        {'x': 50, 'y': 0},
        {'x': 50, 'y': 50},
        {'x': 25, 'y': 25}
    ]

    all_first_houses = []
    for start_point in start_coords: 
        nearest = None
        smallest_distance = 200
        all_houses = []
        for house in district.unconnected_houses():
            distance = (abs(start_point['x'] - house.x_grid) + abs(start_point['y'] - house.y_grid))
            all_houses.append({'house': house, 'distance': distance})
            if distance < smallest_distance:
                smallest_distance = distance
                nearest = house
        nearest.connected = True
        if start_point['x'] > nearest.x_grid:
            xl = start_point['x']
            xs = nearest.x_grid
        else: 
            xl = nearest.x_grid
            xs = start_point['x']
        if start_point['y'] > nearest.y_grid:
            yl = start_point['y']
            ys = nearest.y_grid
        else:
            yl = nearest.y_grid
            ys = start_point['y']

        square = abs(xl-xs) * abs(yl-ys)
        point_data = {
            'start': start_point, 
            'all_houses': all_houses, 
            'xl': xl, 
            'xs': xs, 
            'yl': yl, 
            'ys': ys, 
            'square': square, 
            'houses': [nearest], 
            'output': nearest.output
            }
        all_first_houses.append(point_data)
        
    next_step(district, all_first_houses)


def next_step(district, all_first_houses):
    """Divides the other 145 houses between the first five points"""
    s=0
    for s in range(30):
        i = 0
        for i in range(5):
            point = all_first_houses[i]
            houses = point['all_houses']
            houses.sort(key=lambda d: d['distance'])
            free_houses = [h['house'] for h in houses if not h['house'].get_status()]
            if len(free_houses) > 5:
                free_houses = free_houses[0:5]

            squares = []   
            for house in free_houses:
                test_xl = max([point['xl'], house.x_grid])
                test_xs = min([point['xs'], house.x_grid])
                test_yl = max([point['yl'], house.y_grid])
                test_ys = min([point['ys'], house.y_grid])
                new_square = abs(test_xl-test_xs) * abs(test_yl-test_ys)
                squares.append({'house': house, 'square': new_square})
            
            if squares:
                squares.sort(key=lambda n: n['square'])
                new_house = squares[0]
                the_house = new_house['house']
                the_house.connected = True
                point['houses'].append(the_house)
            i += 1    
        s += 1
    third_step(district, all_first_houses)


def third_step(district, all_first_houses):
    """Finds the closest battery for each starting point and connects all the houses in that group to that battery"""
    batteries = district.batteries
    k = 0
    for k in range(5):
        battery = batteries[k]
        nearest = 0
        smallest = 1000
        for group in all_first_houses:
            start_point = group['start']
            distance =  (abs(start_point['x'] - battery.x_grid) + abs(start_point['y'] - battery.y_grid))
            if distance < smallest:
                smallest = distance
                nearest = all_first_houses.index(group)

        get_houses = all_first_houses[nearest]
        true_houses = get_houses['houses']
        for each_house in true_houses:
            connection = district.find_specific_connection(each_house, battery)
            district.make_connection(connection)
        all_first_houses.remove(get_houses)    
        k += 1
            

def share_cables(district):
    """Finds the closest house for each battery and constructs cables between them"""
    for battery in district.batteries:        
        connections = [c for c in district.get_true_connections() if c.battery == battery]
        close_x = 200
        con_x = None
        for connection in connections:
            if abs(connection.house.x_grid / battery.x_grid) < close_x:
                close_x = abs(connection.house.x_grid / battery.x_grid)
                con_x = connection
            elif abs(connection.house.x_grid / battery.x_grid) == close_x:
                if connection.distance > con_x.distance:
                    close_x = abs(connection.house.x_grid / battery.x_grid)
                    con_x = connection

        con_x.house.construct_cable(battery.x_grid, battery.y_grid, con_x.distance)
        connections.remove(con_x)

        close_y = 200
        con_y = None
        for connection in connections:
            if abs(connection.house.y_grid / battery.y_grid) < close_y:
                close_y = abs(connection.house.y_grid / battery.y_grid)
                con_y = connection
            elif abs(connection.house.y_grid / battery.y_grid) == close_y:
                if connection.distance > con_y.distance:
                    close_y = abs(connection.house.y_grid / battery.y_grid)
                    con_y = connection
    
        con_y.house.construct_cable(battery.x_grid, battery.y_grid, con_y.distance)
        connections.remove(con_y)

        cables = []
        for cp in con_x.house.cable_points:
            cables.append(cp)
        for points in con_y.house.cable_points:
            cables.append(points)
        connect_points(connections, cables)


def connect_points(connections, cables):
    """Connects all the other houses to the nearest cable that is connected to its battery"""
    connections.sort(key=attrgetter('distance'))
    cable_points = cables    
    for connection in connections:
        closest_point = 1000
        go_x = 0
        go_y = 0
        for p in cable_points:
            pxy = p.split(",")
            px = int(pxy[0])
            py = int(pxy[1])
            dist = abs(px - connection.house.x_grid) + abs(py - connection.house.y_grid)
            if dist < closest_point:
                closest_point = dist
                go_x = px
                go_y = py    
        connection.house.construct_cable(go_x, go_y, closest_point)   
        for more_p in connection.house.cable_points:
            cable_points.append(more_p)     
