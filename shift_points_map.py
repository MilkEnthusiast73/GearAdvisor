from communicate_with_database import*
def find_shift_points(dict):
    lowestFCR = 100000000
    shift_point = 0
    shift_points = []
    for gear in dict:
        lowestFCR = 100000000
        for speed in dict[gear]:   
            if dict[gear][speed] < lowestFCR:
                lowestFCR = dict[gear][speed]
                shift_point = speed
        shift_points.append(int(shift_point))
    return shift_points

def fetchAdvice(speed, gear):
    dict = json_to_dict("FCRModel.json")
    shift_points = find_shift_points(dict)
    if gear < len(shift_points):
        if speed >= shift_points[gear]:
            return "up"
        else:
            return "maintain"
    else:
        return "maintain"