if __name__ == '__main__':  # if we're running file directly and not importing it
    from threading import Thread
    import time
    flag = 1
    def work():
        time.sleep(2)
        print('hahah')
    thread = Thread(target=work)
    thread.start()
    print(12454)