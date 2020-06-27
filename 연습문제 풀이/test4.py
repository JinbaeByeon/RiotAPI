from tkinter import *

class Ball:
    def __init__(self):
        self.x = 10
        self.y = 10
        self.dx = 2
        self.dy = 2
        self.radius = 3
        self.color = "#FF0000"

width = 500
height = 300

class BallAnimate:
    def __init__(self):
        window = Tk()
        window.title("Bouncing Balls")

        self.ballList = []
        self.sleepTime = 100
        self.isStopped = False

        self.canvas = Canvas(window, bg="white", width=width, height=height)
        self.canvas.pack()

        frame = Frame(window)
        frame.pack()
        btStop = Button(frame, text="정지", command=self.stop)
        btStop.pack(side=LEFT)
        btResume = Button(frame, text="재시작", command=self.resume)
        btResume.pack(side=LEFT)
        btAdd = Button(frame, text="+(공 추가)", command=self.add)
        btAdd.pack(side=LEFT)
        btRemove = Button(frame, text="-(공 제거)", command=self.remove)
        btRemove.pack(side=LEFT)
        btFaster = Button(frame, text="빠르게", command=self.faster)
        btFaster.pack(side=LEFT)
        btSlower = Button(frame, text="느리게", command=self.slower)
        btSlower.pack(side=LEFT)

        self.animate()
        window.mainloop()  # Create an event loop

    def stop(self):  # Stop animation
        self.isStopped = True

    def resume(self):  # Resume animation
        self.isStopped = False
        self.animate()

    def add(self):  # Add a new ball
        self.ballList.append(Ball())

    def remove(self):  # Remove the last ball
        self.ballList.pop()

    def faster(self):  # Speed up the animation
        if self.sleepTime > 15:
            self.sleepTime -= 20

    def slower(self):  # Slow down the animation
        self.sleepTime += 20

    def animate(self):  # Move the message
        while not self.isStopped:
            self.canvas.after(self.sleepTime)  # Sleep for 100 milliseconds
            self.canvas.update()  # Update canvas
            self.canvas.delete("ball")

            for ball in self.ballList:
                self.redisplayBall(ball)

    def redisplayBall(self, ball):
        if ball.x >= width:
            ball.dx = -2
        elif ball.x <= 0:
            ball.dx = 2

        if ball.y >= height:
            ball.dy = -2
        elif ball.y <= 0:
            ball.dy = 2

        ball.x += ball.dx
        ball.y += ball.dy
        self.canvas.create_oval(ball.x - ball.radius, ball.y - ball.radius, ball.x + ball.radius, ball.y + ball.radius,
                                fill=ball.color, tags="ball")

BallAnimate()