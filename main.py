import model,view,controller,time,controller2,view2

while True:
    time.sleep(1/60)
    # model.model()
    if model.display=='first':
        controller.event()
        view.view()
    else:
        controller2.event()
        view2.view()