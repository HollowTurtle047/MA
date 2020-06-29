
import pygame, sys, os, zmq

CARDS = ['1','2','3','4','5','6','7','8','9','B']

def main():
    selectSC()
    
def selectSC():
    strIn = valid_input(['0','1','Q','q'], '0-Server 1-Client Q-Quit:')
    if strIn == '0':
        # server
        print('server')
        server()
    elif strIn == '1':
        # client
        print('client')
        client()
    elif strIn == 'Q' or 'q':
        print('Quit')

def server():
    context = zmq.Context(1)
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")
    cards = CARDS
    score = 0
    
    while True:
        if not cards:
            break
        
        message = socket.recv()
        print("Received: %s" % message)
        socket.send_string("I am OK!")
        
def client():
    context = zmq.Context(2)
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")
    cards = CARDS
    score = 0
    
    while True:
        if not cards:
            break
        
        strIn = valid_input(cards, cards)
        socket.send_string(strIn)
        
    
    response = socket.recv()
    print("response: %s" % response)
    
def valid_input(valid_list, mesg):
    while True:
        inputStr = input(mesg + '\r\n')
        if inputStr in valid_list:
            return inputStr

if __name__ == '__main__':
    main()


