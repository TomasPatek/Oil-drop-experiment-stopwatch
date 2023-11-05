import keyboard # for keylogs

class ODEStopwatch:               
    def keyUp(self, event):        
        if self.down_start != 0:
            print("Chyba měření")   # measuring error
            self.up_start = 0
            self.down_start = 0
        elif self.up_start == 0:
            self.up_start = event.time
            print("Start nahoru")   # movement up start
        else:
            print("Čas nahoru:")    # movement up time
            print(str(round(event.time - self.up_start, 2)) + " s\n") 
            self.records[self.measurement_idx].append(['UP', event.time - self.up_start])
            self.up_start = 0
        
        
    def keyDown(self, event):
        if self.up_start != 0:
            print("Chyba měření")   # measuring error
            self.up_start = 0
            self.down_start = 0
        elif self.down_start == 0:
            print("Start dolů")     # movement down start
            self.down_start = event.time
        else:
            print("Čas dolu:")      # movement down time
            print(str(round(event.time - self.down_start, 2)) + " s\n") 
            self.records[self.measurement_idx].append(['DOWN', event.time - self.down_start])
            self.down_start = 0
    

    
    def newMeasurement(self, event):
        if self.up_start != 0:
            self.keyUp(event)
        if self.down_start != 0:
            self.keyDown(event)
         
            
        print("\n\nNové měření")        # new measurements
        self.records.append([])
        self.measurement_idx = self.measurement_idx + 1
        
        
    def printOutput(self, event):
        if self.up_start != 0:
            self.keyUp(event)
        if self.down_start != 0:
            self.keyDown(event)        
        
        print("\n\n------------\n")
        for index, measurement in enumerate(self.records):
            print(str(index + 1) + ". měření:")   #idex th measurement:
            time_up_sum = 0
            move_up_count = 0
            time_down_sum = 0
            move_down_count = 0
            for record in measurement:
                if record[0] == "UP":
                    time_up_sum = time_up_sum + record[1]

                    move_up_count = move_up_count + 1
                if record[0] == "DOWN":
                    time_down_sum = time_down_sum + record[1]
                    move_down_count = move_down_count + 1
            print(str(move_up_count) + " měření nahoru, čas: " + str(round(time_up_sum, 2)) + " s")    # measurements up, summary time
            print(str(move_down_count) + " měření dolů, čas: " + str(round(time_down_sum, 2)) + " s")  # measurements down, summary time
            print('\n')     
               
        
    def start(self):
        self.up_start = 0
        self.down_start = 0
        self.measurement_idx = 0
        self.records = [[]]
        
        keyboard.on_press_key(key="up", callback=self.keyUp)
        keyboard.on_press_key(key="down", callback=self.keyDown)
 
        keyboard.on_press_key(key="right", callback=self.newMeasurement)
        keyboard.on_press_key(key="enter", callback=self.printOutput)
        
        print("Program ukončíte stiskem tlačítka Esc")  # Escape program by pressing Esc
        keyboard.wait("esc")       

    
if __name__ == "__main__":
    stopwatch = ODEStopwatch()
    stopwatch.start()