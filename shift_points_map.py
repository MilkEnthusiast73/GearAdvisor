from communicate_with_database import*
def find_shift_points(dict):
    lowestFCR = 100000000
    lowestFCRSpeed = 0
    shift_points = []
    for gear in dict:
        for speed in dict[gear]:
            if dict[gear][speed] < lowestFCR:
                lowestFCR = dict[gear][str(speed)]
                lowestFCRSpeed = speed
        shift_points.append(int(speed))

    return shift_points

def fetchAdvice(speed, gear):
    dict = json_to_dict("FCRModel.json")
    shift_points = find_shift_points(dict)
    idealGear = 1
    direction = ""
    for speedPoint in shift_points:
        if speed <= speedPoint:
            break
        idealGear += 1
        
    if gear == idealGear:
        direction = "maintain"
    elif gear < idealGear:
        direction = "up"
    elif gear > idealGear:
        direction = "down"

    return direction, idealGear