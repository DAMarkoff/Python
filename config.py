WIN_SCORE = 10
BALL_DISTANCE_TO_MOVE = 10
BALL_SPEED_RATE = 0.9
BALL_SPEED_DEFAULT = 0.04
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_X_POSITION_FROM_WALL = 40
PADDLE_Y_POSITION_STOP = 80
BALL_BOUNCE_FROM_WALL_Y_DELTA = 20

LEFT_PLAYER_KEY_UP = 'q'
LEFT_PLAYER_KEY_DOWN = 'a'
RIGHT_PLAYER_KEY_UP = 'Up'
RIGHT_PLAYER_KEY_DOWN = 'Down'

BALL_DEVIATION_ON_BOUNCE_FROM_PADDLE = 12
ANGLE_MIN = 35
ANGLE_MAX = 45

PADDLE_X_DELTA_BOUNCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
PADDLE_SPEED = 30

WALL_BOUNCE_Y_COR = SCREEN_HEIGHT / 2 - BALL_BOUNCE_FROM_WALL_Y_DELTA
LEFT_PADDLE_X_POSITION = -SCREEN_WIDTH / 2 + PADDLE_X_POSITION_FROM_WALL
RIGHT_PADDLE_X_POSITION = SCREEN_WIDTH / 2 - PADDLE_X_POSITION_FROM_WALL
PADDLE_STARTING_POSITIONS = [(0, 0), (LEFT_PADDLE_X_POSITION, 0), (RIGHT_PADDLE_X_POSITION, 0)]

# BALL_BOUNCE_FROM_PADDLE_X_DELTA_FROM_WALL = 50
# PADDLE_BOUNCE_Y_DELTA = 50
# PADDLE_BOUNCE_X_COR = SCREEN_WIDTH / 2 - BALL_BOUNCE_FROM_PADDLE_X_DELTA_FROM_WALL
# PADDLE_STOP_Y_COR = SCREEN_HEIGHT / 2 - PADDLE_Y_POSITION_STOP
