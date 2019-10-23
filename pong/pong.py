import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector
from kivy.clock import Clock


class Players(Widget):
    pass

class PongBall(Widget):
    x_velocity = NumericProperty(0)
    y_velocity = NumericProperty(0)
    velocity = ReferenceListProperty(x_velocity, y_velocity)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

class MainWidget(Widget):
    player1_score = 0
    player2_score = 0

    def on_touch_down(self, touch):
        if touch.x < self.width / 2:
            self.player1.center_y = touch.y
        elif touch.x > self.width / 2:
            self.player2.center_y = touch.y


    def kickoff(self):
        self.ball.x_velocity = 5
        self.ball.y_velocity = 5
        self.set_score

    def update(self, delta_time):
        self.ball.move()

        hit_player1 = self.ball.collide_widget(self.player1)
        hit_player2 = self.ball.collide_widget(self.player2)

        if hit_player1 or hit_player2:
            self.ball.x_velocity *= -1
            self.ball.y_velocity *= -1

        if (self.ball.top > self.height) or (self.ball.y < 0):
            self.ball.y_velocity *= -1

        ball_hit_right_wall = self.ball.right > self.width
        ball_hit_left_wall = self.ball.x < 0
        if ball_hit_right_wall or ball_hit_left_wall:
            self.ball.x_velocity *= -1

        if ball_hit_left_wall:
            self.player2_score += 1
        elif ball_hit_right_wall:
            self.player1_score += 1

        self.set_score()

    def set_score(self):
        self.player1_board.text = str(self.player1_score)
        self.player2_board.text = str(self.player2_score)


class Pong(App):

    def build(self):
        game = MainWidget()
        game.kickoff()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game


if __name__ == '__main__':
    app = Pong()
    app.run()
