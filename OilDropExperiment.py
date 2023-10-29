import keyboard # for keylogs

class ODEStopwatch:               
    def keyUp(self, event):        
        if self.down_start != 0:
            print("Chyba měření")
            self.up_start = 0
            self.down_start = 0
        elif self.up_start == 0:
            self.up_start = event.time
            print("Start nahoru")
        else:
            print("Čas nahoru:")
            print(event.time - self.up_start)
            self.up_start = 0
        
    def keyDown(self, event):
        if self.up_start != 0:
            print("Chyba měření")
            self.up_start = 0
            self.down_start = 0
        elif self.down_start == 0:
            print("Start dolů")
            self.down_start = event.time
        else:
            print("Čas dolu:")
            print(event.time - self.down_start)
            self.down_start = 0
            
    def start(self):
        self.up_start = 0
        self.down_start = 0
        
        keyboard.on_press_key(key="up", callback=self.keyUp)
        keyboard.on_press_key(key="down", callback=self.keyDown)
        
        print("Program ukončíte stiskem tlačítka Esc")
        keyboard.wait("esc")       


    
if __name__ == "__main__":
    stopwatch = ODEStopwatch()
    stopwatch.start()