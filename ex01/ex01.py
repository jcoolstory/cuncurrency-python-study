import rx
from rx import Observable, Observer

class temperatureObserver(Observer):

    def on_next(self,x):

        if x>6 :
            print("warning")
        if x == 0:
            print("datacneter")

    def on_error(self,e):
        print("error : %s" % e)

    def on_complated(self):
        print("all temps")

xs = Observable.from_interable(range(10))

d = xs.subscribe(temperatureObserver())


