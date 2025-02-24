import alvikController as ac 

controller = ac.DeviceController('http://172.20.10.5:80')

controller.up(10, 'cm')