def find_shift_points(dict):
    lowestFCR = 100000000
    lowestFCRSpeed = 0
    shift_points = []
    for gear in dict:
        for speed in gear:
            if dict[gear][speed] < lowestFCR:
                lowestFCR = dict[gear][speed]
                lowestFCRSpeed = speed
        shift_points.append(speed)

    return shift_points

def fetchAdvice(speed, gear):
    dict = json_to_dict()
    shift_points = find_shift_points(dict)
    idealGear = 1
    direction = ""
    for speedPoint in shift_points:
        if speed <= speedPoint:
            idealGear = 1
            break
    if gear == idealGear:
        direction = "maintain"
    elif gear < idealGear:
        direction = "shift up"
    elif gear > idealGear:
        direction = "shift down"

    return direction, idealGear