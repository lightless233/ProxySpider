import time, threading


def target():
    print 'current threading: %s is running' % threading.current_thread().name
    time.sleep(1)
    print 'current threading: %s is ended' % threading.current_thread().name

print 'current threading: %s is running' % threading.current_thread().name
t = threading.Thread(target=target)
#t.setDaemon(True)
t.start()
t.join()
print 'current threading: %s is ended' % threading.current_thread().name