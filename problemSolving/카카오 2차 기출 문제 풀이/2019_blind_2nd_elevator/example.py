import requests


url = 'http://localhost:8000'


def start(user, problem, count):
    uri = url + '/start' + '/' + user + '/' + str(problem) + '/' + str(count)
    return requests.post(uri).json()


def oncalls(token):
    uri = url + '/oncalls'
    return requests.get(uri, headers={'X-Auth-Token': token}).json()


def action(token, cmds):
    uri = url + '/action'
    return requests.post(uri, headers={'X-Auth-Token': token}, json={'commands': cmds}).json()


def p0_simulator():
    user = 'tester'
    problem = 0
    count = 2

    ret = start(user, problem, count)
    token = ret['token']
    print('Token for %s is %s' % (user, token))

    f = open("./p0.in", 'r')
    d = f.read().split('\n')
    data = []
    calls = []
    for i in range(len(d)):
        data.append(list(map(lambda x: int(x), d[i].split(','))))
    for i in range(len(data)):
        calls.append({'id': data[i][0], 'timestamp': data[i][1], 'start': data[i][2], 'end': data[i][3]})
    
    print(ret)
    while not ret['is_end']:
        ret = oncalls(token)
        call = None
        if calls:
            call = calls.pop(0)
        if call:
            # find minimal move
            min_value = 26
            move_idx = 0
            if call['start'] < call['end']:
                for i in range(2):
                    if ret['elevators'][i]['status'] == 'STOPPED':
                        if abs(ret['elevators'][i]['floor'] - call['start']) < min_value:
                            min_value = abs(ret['elevators'][i]['floor'] - call['start'])
                            move_idx = i
                    elif ret['elevators'][i]['status'] == 'UPWARD':
                        if 0 <= call['start'] - ret['elevators'][i]['floor'] < min_value:
                            min_value = ret['elevators'][i]['floor'] - call['start']
                            move_idx = i
            else:
                for i in range(2):
                    if ret['elevators'][i]['status'] == 'STOPPED':
                        if abs(ret['elevators'][i]['floor'] - call['start']) < min_value:
                            min_value = abs(ret['elevators'][i]['floor'] - call['start'])
                            move_idx = i
                    elif ret['elevators'][i]['status'] == 'DOWNWARD':
                        if 0 <= ret['elevators'][i]['floor'] - call['start'] < min_value:
                            min_value = ret['elevators'][i]['floor'] - call['start']
                            move_idx = i
        print(ret['elevators'][i])
        break
        

    action(token, [{'elevator_id': 0, 'command': 'UP'}, {'elevator_id': 1, 'command': 'STOP'}])

    action(token, [{'elevator_id': 0, 'command': 'UP'}, {'elevator_id': 1, 'command': 'OPEN'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'UP'}, {'elevator_id': 1, 'command': 'ENTER', 'call_ids': [2, 3]}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'STOP'}, {'elevator_id': 1, 'command': 'CLOSE'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'OPEN'}, {'elevator_id': 1, 'command': 'UP'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'ENTER', 'call_ids': [0, 1]}, {'elevator_id': 1, 'command': 'STOP'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'CLOSE'}, {'elevator_id': 1, 'command': 'OPEN'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'DOWN'}, {'elevator_id': 1, 'command': 'EXIT', 'call_ids': [2]}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'STOP'}, {'elevator_id': 1, 'command': 'CLOSE'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'OPEN'}, {'elevator_id': 1, 'command': 'UP'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'EXIT', 'call_ids': [1]}, {'elevator_id': 1, 'command': 'UP'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'CLOSE'}, {'elevator_id': 1, 'command': 'STOP'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'DOWN'}, {'elevator_id': 1, 'command': 'OPEN'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'STOP'}, {'elevator_id': 1, 'command': 'EXIT', 'call_ids': [3]}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'OPEN'}, {'elevator_id': 1, 'command': 'CLOSE'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'ENTER', 'call_ids': [4]}, {'elevator_id': 1, 'command': 'STOP'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'CLOSE'}, {'elevator_id': 1, 'command': 'STOP'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'DOWN'}, {'elevator_id': 1, 'command': 'STOP'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'STOP'}, {'elevator_id': 1, 'command': 'STOP'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'OPEN'}, {'elevator_id': 1, 'command': 'STOP'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'EXIT', 'call_ids': [0, 4]}, {'elevator_id': 1, 'command': 'STOP'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'ENTER', 'call_ids': [5]}, {'elevator_id': 1, 'command': 'STOP'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'CLOSE'}, {'elevator_id': 1, 'command': 'STOP'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'UP'}, {'elevator_id': 1, 'command': 'STOP'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'STOP'}, {'elevator_id': 1, 'command': 'STOP'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'OPEN'}, {'elevator_id': 1, 'command': 'STOP'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'EXIT', 'call_ids': [5]}, {'elevator_id': 1, 'command': 'STOP'}])
    ret = oncalls(token)
    print(ret['is_end'])

if __name__ == '__main__':
    p0_simulator()
