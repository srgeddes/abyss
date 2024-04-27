import uvage
import random

camera = uvage.Camera(1280, 720, True)

# -------------------------------------------STATUS--------------------------------------------------------------------#
home_screen_status = True
level_1_status = False
question_status = False
game_over_status = False
last_chance_status = False

# -------------------------------------------HOME SCREEN ASSETS--------------------------------------------------------#
home_screen_count = 0
black_hole_count = 0
home_screen_background = uvage.from_image(5400, 360, 'assets/home_screen/big_stars.png')
home_screen_title = uvage.from_image(0, 0, 'assets/home_screen/title.png')
home_screen_start = uvage.from_image(0, 0, 'assets/home_screen/start.png')
home_screen_menu_star = uvage.from_image(0, 0, 'assets/home_screen/menu_star.png')

home_screen_assets = [home_screen_background, home_screen_title, home_screen_start, home_screen_menu_star]
home_screen_title.scale_by(.8)
home_screen_start.scale_by(.3)
home_screen_menu_star.scale_by(.3)

random_x = random.randint(100, 1000)
random_y = random.randint(100, 600)


# -------------------------------------------HOME SCREEN FUNCTIONS-----------------------------------------------------#


def home_screen():
    global home_screen_status, home_screen_count, home_screen_menu_star, black_hole_count
    home_screen_count += .4

    if home_screen_status:
        # Home Screen Assets adjustment
        home_screen_title.center = [640 + home_screen_count, 400]
        home_screen_start.center = [640 + home_screen_count, 650]
        home_screen_menu_star.center = [770 + home_screen_count, 650]

        # Draw
        for i in home_screen_assets:
            camera.draw(i)


        black_hole.rotate(5)
        if black_hole.y <= 100 or black_hole.y >= camera.height:
            black_hole.yspeed *= -1
        if black_hole.x <= 100 + home_screen_count or black_hole.x >= camera.width + home_screen_count - 100:
            black_hole.xspeed *= -1

        black_hole.move_speed()
        camera.draw(black_hole)
        # black_hole.center = [640 + home_screen_count, 200]

        # Movement (Scrolling)
        camera.move(.4, 0)
        home_screen_title.xspeed = .4
        home_screen_title.move_speed()
        if home_screen_background.right_touches(home_screen_title):
            home_screen_background.move(5000, 0)

        home_screen_controller()

        camera.display()


def home_screen_controller():
    global home_screen_status, level_1_status

    if uvage.is_pressing("return"):
        home_screen_status = False
        camera.center = [640, 360]
        black_hole.center = [640, 1300]
        generate_questions()
        level_1_status = True


# -------------------------------------------LEVEL ASSETS-----------------------------------------------------#

# Background
background = []

level_1_background = uvage.from_image(640, 450, 'assets/level1/spacebackground.jpg')
level_1_background.size = [1280, 900]
background.append(level_1_background)
level_1_background1 = uvage.from_image(640, -450, 'assets/level1/spacebackground.jpg')
level_1_background1.size = [1280, 900]
background.append(level_1_background1)
level_1_background2 = uvage.from_image(640, -900, 'assets/level1/spacebackground.jpg')
level_1_background2.size = [1280, 900]
background.append(level_1_background2)
level_1_background3 = uvage.from_image(640, -1800, 'assets/level1/spacebackground.jpg')
level_1_background3.size = [1280, 900]
background.append(level_1_background3)
level_1_background4 = uvage.from_image(640, -2700, 'assets/level1/spacebackground.jpg')
level_1_background4.size = [1280, 900]
background.append(level_1_background4)
level_1_background5 = uvage.from_image(640, -3600, 'assets/level1/spacebackground.jpg')
level_1_background5.size = [1280, 900]
background.append(level_1_background5)
level_1_background6 = uvage.from_image(640, -4500, 'assets/level1/spacebackground.jpg')
level_1_background6.size = [1280, 900]
background.append(level_1_background6)
level_1_background7 = uvage.from_image(640, -5400, 'assets/level1/spacebackground.jpg')
level_1_background7.size = [1280, 900]
background.append(level_1_background7)
level_1_background8 = uvage.from_image(640, -6300, 'assets/level1/spacebackground.jpg')
level_1_background8.size = [1280, 900]
background.append(level_1_background8)
level_1_background9 = uvage.from_image(640, -7200, 'assets/level1/spacebackground.jpg')
level_1_background9.size = [1280, 900]
background.append(level_1_background9)

player_images = uvage.load_sprite_sheet('assets/level1/spr_trooper_run_strip12_resized.png', rows=1, columns=12)

# Rocket
rocket = uvage.from_image(600, -6350, "assets/level1/rocketship.png")
rocket.size = [75, 100]

# Player
player = uvage.from_image(600, 500, player_images[-1])

# Black Hole

black_hole = uvage.from_image(random_x, random_y, 'assets/level1/black_hole.png')
black_hole.scale_by(.15)
black_hole.yspeed = 3
black_hole.xspeed = 3

# Score
score_number = 0
final_score = 0

floor = uvage.from_image(700, 600, "assets/level1/platforms.png")
floor.size = [1400, 20]
end = uvage.from_image(700, -6300, "assets/level1/platforms.png")
end.size = [1400, 20]

level_1_frame = 0
facing_right = True
facing_left = False
goingright = True
goingright1 = False
goingright2 = True
goingright3 = False
canjump = False
gameover = False
jumping = False
win = False

size = [200, 20]
smallish = [150, 20]
small = [100, 20]
big = [400, 20]
tiny = [50, 15]

right_wall = uvage.from_color(1280, 500, "black", .1, 100000)
left_wall = uvage.from_color(0, 500, "black", .1, 100000)

yspeed = 1.8

platforms = []
moving_platforms = []
moving_platforms1 = []
moving_platforms2 = []
moving_platforms3 = []

level_1_ending_barrier = uvage.from_color(635, -8200, 'red', 5, 5)

last_chance_text = uvage.from_text(0, 0, "LAST CHANCE", 40, 'red', True)

one = uvage.from_image(400, 500, "assets/level1/platforms.png")
platforms.append(one)
one.size = size
two = uvage.from_image(700, 350, "assets/level1/platforms.png")
platforms.append(two)
two.size = size
three = uvage.from_image(1000, 200, "assets/level1/platforms.png")
platforms.append(three)
three.size = size
four = uvage.from_image(800, 50, "assets/level1/platforms.png")
platforms.append(four)
four.size = size
five = uvage.from_image(500, -100, "assets/level1/platforms.png")
platforms.append(five)
five.size = size
six = uvage.from_image(200, -250, "assets/level1/platforms.png")
platforms.append(six)
six.size = size
seven = uvage.from_image(400, -440, "assets/level1/platforms.png")
platforms.append(seven)
seven.size = size
eight = uvage.from_image(700, -590, "assets/level1/platforms.png")
platforms.append(eight)
eight.size = size
nine = uvage.from_image(400, -740, "assets/level1/platforms.png")
moving_platforms.append(nine)
nine.size = size
ten = uvage.from_image(100, -1040, "assets/level1/platforms.png")
moving_platforms1.append(ten)
ten.size = size
eleven = uvage.from_image(700, -890, "assets/level1/platforms.png")
platforms.append(eleven)
eleven.size = size
twelve = uvage.from_image(500, -1200, "assets/level1/platforms.png")
platforms.append(twelve)
twelve.size = small
thirteen = uvage.from_image(700, -890, "assets/level1/platforms.png")
platforms.append(thirteen)
thirteen.size = small
fourteen = uvage.from_image(200, -1350, "assets/level1/platforms.png")
moving_platforms2.append(fourteen)
fourteen.size = big
fifteen = uvage.from_image(100, -1500, "assets/level1/platforms.png")
platforms.append(fifteen)
fifteen.size = size
sixteen = uvage.from_image(1100, -1650, "assets/level1/platforms.png")
platforms.append(sixteen)
sixteen.size = size
seventeen = uvage.from_image(800, -1810, "assets/level1/platforms.png")
platforms.append(seventeen)
seventeen.size = small
eighteen = uvage.from_image(200, -1960, "assets/level1/platforms.png")
moving_platforms1.append(eighteen)
eighteen.size = big
nineteen = uvage.from_image(400, -2120, "assets/level1/platforms.png")
platforms.append(nineteen)
nineteen.size = small
twenty = uvage.from_image(200, -2270, "assets/level1/platforms.png")
moving_platforms2.append(twenty)
twenty.size = size
twentyone = uvage.from_image(400, -2420, "assets/level1/platforms.png")
platforms.append(twentyone)
twentyone.size = smallish
twentytwo = uvage.from_image(700, -2600, "assets/level1/platforms.png")
moving_platforms2.append(twentytwo)
twentytwo.size = smallish
twentythree = uvage.from_image(1000, -2800, "assets/level1/platforms.png")
platforms.append(twentythree)
three.size = smallish
twentyfour = uvage.from_image(800, -3000, "assets/level1/platforms.png")
moving_platforms1.append(twentyfour)
twentyfour.size = size
twentyfive = uvage.from_image(500, -3200, "assets/level1/platforms.png")
platforms.append(twentyfive)
twentyfive.size = small
twentysix = uvage.from_image(200, -3350, "assets/level1/platforms.png")
moving_platforms2.append(twentysix)
twentysix.size = small
twentyseven = uvage.from_image(400, -3550, "assets/level1/platforms.png")
platforms.append(twentyseven)
twentyseven.size = smallish
twentyeight = uvage.from_image(700, -3750, "assets/level1/platforms.png")
platforms.append(twentyeight)
twentyeight.size = big
twentynine = uvage.from_image(400, -3950, "assets/level1/platforms.png")
moving_platforms.append(twentynine)
twentynine.size = smallish
thirty = uvage.from_image(100, -4150, "assets/level1/platforms.png")
moving_platforms1.append(thirty)
thirty.size = size
thirtyone = uvage.from_image(700, -4350, "assets/level1/platforms.png")
platforms.append(thirtyone)
thirtyone.size = small
thirtytwo = uvage.from_image(910, -4550, "assets/level1/platforms.png")
platforms.append(thirtytwo)
thirtytwo.size = small
thirtythree = uvage.from_image(1130, -4750, "assets/level1/platforms.png")
platforms.append(thirtythree)
thirtythree.size = small
thirtyfour = uvage.from_image(50, -4950, "assets/level1/platforms.png")
platforms.append(thirtyfour)
thirtyfour.size = small
thirtyfive = uvage.from_image(600, -5150, "assets/level1/platforms.png")
moving_platforms3.append(thirtyfive)
thirtyfive.size = smallish
thirtysix = uvage.from_image(600, -5350, "assets/level1/platforms.png")
platforms.append(thirtysix)
thirtysix.size = smallish
thirtyseven = uvage.from_image(700, -5550, "assets/level1/platforms.png")
platforms.append(thirtyseven)
thirtyseven.size = small
thirtyeight = uvage.from_image(850, -5750, "assets/level1/platforms.png")
platforms.append(thirtyeight)
thirtyeight.size = tiny
thirtynine = uvage.from_image(650, -5950, "assets/level1/platforms.png")
platforms.append(thirtynine)
thirtynine.size = tiny
fourty = uvage.from_image(600, -6150, "assets/level1/platforms.png")
moving_platforms3.append(fourty)
fourty.size = tiny

# Questions
questions_dict = {}

# index of answer in answer_list
question_answers_dict = {
    "1": "B",
    "2": "B",
    "3": "A",
    "4": "D",
    "5": "B",
    "6": "B",
    "7": "D",
    "8": "C",
    "9": "A",
    "10": "C",
    "11": "C",
    "12": "C",
    "13": "C",
    "14": "C",
    "15": "B",
    "16": "A",
    "17": "D",
    "18": "A"
}

thing = ["B", "B", "A", "D", "B", "B", "D", "C", "A", "C", "C", "C", "C", "C", "B", "A", "D", "A"]
list_of_possible_answers = ["A", "B", "C", "D"]

questions_dict["1"] = uvage.from_image(0, 0, 'assets/level1/questions/questions_1.jpeg')
questions_dict["2"] = uvage.from_image(0, 0, 'assets/level1/questions/question_2.png')
questions_dict["3"] = uvage.from_image(0, 0, 'assets/level1/questions/question_3.png')
questions_dict["4"] = uvage.from_image(0, 0, 'assets/level1/questions/question_4.png')
questions_dict["5"] = uvage.from_image(0, 0, 'assets/level1/questions/question_5.png')
questions_dict["6"] = uvage.from_image(0, 0, 'assets/level1/questions/question_6.png')
questions_dict["7"] = uvage.from_image(0, 0, 'assets/level1/questions/question_7.png')
questions_dict["8"] = uvage.from_image(0, 0, 'assets/level1/questions/question_8.png')
questions_dict["9"] = uvage.from_image(0, 0, 'assets/level1/questions/question_9.png')
questions_dict["10"] = uvage.from_image(0, 0, 'assets/level1/questions/question_10.png')
questions_dict["11"] = uvage.from_image(0, 0, 'assets/level1/questions/question_11.png')
questions_dict["12"] = uvage.from_image(0, 0, 'assets/level1/questions/question_12.png')
questions_dict["13"] = uvage.from_image(0, 0, 'assets/level1/questions/question_13.png')
questions_dict["14"] = uvage.from_image(0, 0, 'assets/level1/questions/question_14.png')
questions_dict["15"] = uvage.from_image(0, 0, 'assets/level1/questions/question_15.png')
questions_dict["16"] = uvage.from_image(0, 0, 'assets/level1/questions/question_16.png')
questions_dict["17"] = uvage.from_image(0, 0, 'assets/level1/questions/question_17.png')
questions_dict["18"] = uvage.from_image(0, 0, 'assets/level1/questions/question_18.png')

def generate_questions():
    global questions_dict
    # get 10 random
    # questions_dict = dict(random.sample(list(questions_dict.items()), 13))

for question in questions_dict.values():
    question.scale_by(.6)

star_collectable_1 = uvage.from_image(500, -150, 'assets/level1/star_collectable.png')
star_collectable_2 = uvage.from_image(400, -800, 'assets/level1/star_collectable.png')
star_collectable_3 = uvage.from_image(1100, -1700, 'assets/level1/star_collectable.png')
star_collectable_4 = uvage.from_image(700, -3800, 'assets/level1/star_collectable.png')
star_collectable_5 = uvage.from_image(600, -6200, 'assets/level1/star_collectable.png')

star_collectable_list = [star_collectable_1, star_collectable_2, star_collectable_3, star_collectable_4,
                         star_collectable_5]
for star_collectable in star_collectable_list:
    star_collectable.scale_by(.2)
    star_collectable.speedy = 1.8
star_count = 0

# TODO : Make the star bounce


# -------------------------------------------QUESTION SCREEN----------------------------------------------------------#
question_screen_count = 0


def question_handler():
    global question_status, game_over_status, last_chance_status, level_1_status, question_screen_count, score_number

    if question_status:
        question_screen_count += .4
        home_screen_background.center = [camera.x - home_screen_count, camera.y - question_screen_count]
        camera.draw(home_screen_background)

        question_key = list(questions_dict)[0]
        question_value = questions_dict[question_key]
        question_value.center = [camera.x, camera.y]
        camera.draw(question_value)

        answer = question_answers_dict[question_key]
        possible_answer_list = ["a", "b", "c", "d"]
        possible_answer_list.pop(possible_answer_list.index(answer.lower()))
        if uvage.is_pressing(answer.lower()):
            del questions_dict[question_key]
            black_hole.move(0, 500)
            question_status = False
            score_number += 1
            # black_hole.center = [camera.x, camera.y + 500]
            question_screen_count = 0
            level_1_status = True
        elif (uvage.is_pressing(possible_answer_list[0]) or uvage.is_pressing(
                possible_answer_list[1]) or uvage.is_pressing(possible_answer_list[2])) and last_chance_status:
            question_status = False
            level_1_status = False
            black_hole.center = [640, 100]
            black_hole.yspeed = 3
            black_hole.xspeed = 3
            question_screen_count = 0
            game_over_status = True
        elif (uvage.is_pressing(possible_answer_list[0]) or uvage.is_pressing(
                possible_answer_list[1]) or uvage.is_pressing(possible_answer_list[2])) and (not last_chance_status):
            question_status = False
            black_hole.move(0, 500)
            # black_hole.center = [camera.x, camera.y + 500]
            last_chance_status = True
            question_screen_count = 0
            level_1_status = True


# -------------------------------------------LEVEL 1 FUNCTIONS---------------------------------------------------------#
def star_handler():
    global question_status, star_count
    for star_collectable in star_collectable_list:
        camera.draw(star_collectable)
        star_collectable.move_speed()
        if player.touches(star_collectable):
            star_count += 1
            star_collectable.move(0, 100000)
            question_status = True


def black_hole_handler():
    global level_1_status, last_chance_status, question_status
    camera.draw(black_hole)
    black_hole.rotate(5)
    black_hole.yspeed = .15
    black_hole.xspeed = 0
    black_hole.move_speed()
    if player.y + 100 >= black_hole.y >= player.y:
        level_1_status = False
        last_chance_status = True
        question_status = True


def level_1():
    global level_1_frame, facing_left, facing_right, canjump, xspeed, yspeed, gameover, goingright1, goingright, goingright2, \
        jumping, goingright3, win, score_number, level_1_status, game_over_status, final_score, question_status

    camera.y = player.y

    if level_1_status and not question_status:

        camera.clear('black')
        camera.draw(level_1_ending_barrier)
        # Background
        for each in background:
            camera.draw(each)
            each.speedy = yspeed
            each.move_speed()

        # platform movement
        camera.draw(rocket)
        camera.draw(floor)
        camera.draw(end)
        floor.speedy = yspeed
        end.speedy = yspeed
        rocket.speedy = yspeed
        floor.move_speed()
        end.move_speed()
        rocket.move_speed()

        for each in platforms:
            camera.draw(each)
            each.speedy = yspeed
            each.move_speed()
            if player.bottom_touches(each):
                player.move_to_stop_overlapping(each)
                player.speedx = 0
                canjump = True
        for each in moving_platforms:
            camera.draw(each)
            if each.right_touches(right_wall):
                goingright = False
            if each.left_touches(left_wall):
                goingright = True
            each.speedy = yspeed
            if player.bottom_touches(each):
                player.move_to_stop_overlapping(each)
                player.speedx = each.speedx
                canjump = True
            if goingright:
                speed = 3
                each.speedx = speed
            if not goingright:
                speed = -3
                each.speedx = speed
            each.move_speed()
        for each in moving_platforms1:
            camera.draw(each)
            if each.right_touches(right_wall):
                goingright1 = False
            if each.left_touches(left_wall):
                goingright1 = True
            each.speedy = yspeed
            if player.bottom_touches(each):
                player.move_to_stop_overlapping(each)
                player.speedx = each.speedx
                canjump = True
            if goingright1:
                speed = 3
                each.speedx = speed
            if not goingright1:
                speed = -3
                each.speedx = speed
            each.move_speed()
        for each in moving_platforms2:
            camera.draw(each)
            if each.right_touches(right_wall):
                goingright2 = False
            if each.left_touches(left_wall):
                goingright2 = True
            each.speedy = yspeed
            if player.bottom_touches(each):
                player.move_to_stop_overlapping(each)
                player.speedx = each.speedx
                canjump = True
            if goingright2:
                speed = 4
                each.speedx = speed
            if not goingright2:
                speed = -4
                each.speedx = speed
            each.move_speed()
        for each in moving_platforms3:
            camera.draw(each)
            if each.right_touches(right_wall):
                goingright3 = False
            if each.left_touches(left_wall):
                goingright3 = True
            each.speedy = yspeed
            if player.bottom_touches(each):
                player.move_to_stop_overlapping(each)
                player.speedx = each.speedx
                canjump = True
            if goingright3:
                speed = 4
                each.speedx = speed
            if not goingright3:
                speed = -4
                each.speedx = speed
            each.move_speed()
        # Animation and Player Collision
        if player.x > 1270:
            player.x = 0
        if player.x < 0:
            player.x = 1270
        is_moving = False
        if uvage.is_pressing("right arrow"):
            if not facing_right:
                facing_right = True
                player.flip()
            is_moving = True
            player.x += 5
        if uvage.is_pressing("left arrow"):
            if facing_right:
                facing_right = False
                player.flip()
            is_moving = True
            player.x -= 5
        if not is_moving:
            camera.draw(player)
        else:
            level_1_frame += .3
            if level_1_frame >= 12:
                level_1_frame = 0
            player.image = player_images[int(level_1_frame)]
            camera.draw(player)
        # Player Falling
        player.yspeed += .9
        if player.bottom_touches(floor):
            player.yspeed = 0
            if uvage.is_pressing("space"):
                player.yspeed = -20
        if player.bottom_touches(end):
            player.yspeed = 0
            if uvage.is_pressing("space"):
                player.yspeed = -20
        player.move_speed()

        for each in platforms:
            if uvage.is_pressing("space") and player.bottom_touches(each):
                player.yspeed = -20
                jumping = True
        for each in moving_platforms:
            if uvage.is_pressing("space") and player.bottom_touches(each):
                player.yspeed = -20
                jumping = True
        for each in moving_platforms1:
            if uvage.is_pressing("space") and player.bottom_touches(each):
                player.yspeed = -20
                jumping = True
        for each in moving_platforms2:
            if uvage.is_pressing("space") and player.bottom_touches(each):
                player.yspeed = -20
                jumping = True
        for each in moving_platforms3:
            if uvage.is_pressing("space") and player.bottom_touches(each):
                player.yspeed = -20
                jumping = True

        if jumping:
            player.speedx = 0

        # winning
        if player.touches(rocket) and star_count == 5:
            win = True
        elif player.touches(rocket) and star_count < 5:
            black_hole.center = [640, 100]
            game_over_status = True
        if win:
            player.x = rocket.x
            player.y = rocket.y
            rocket.speedy = -4
            rocket.move_speed()

        # black hole
        black_hole_handler()

        # Star
        star_handler()

        # Question

        # Win
        if level_1_background9.top_touches(rocket):
            final_score = score_number
            level_1_status = False
            camera.clear('black')
            black_hole.center = [640, 100]
            game_over_status = True

        # Score
        # score_number += .016
        score = uvage.from_text(1230, 50, str(int(score_number)), 40, 'red')
        score.move(0, player.y - 350)
        camera.draw(score)

        if last_chance_status and not question_status:
            last_chance_text.center = [1100, camera.y - 350]
            camera.draw(last_chance_text)

        camera.display()

    # Question s
    if question_status:
        question_handler()
        camera.display()


# -------------------------------------------GAME OVER ASSETS AND FUNCTION----------------------------------------------#

score_number_2 = 0
game_over_background = uvage.from_image(620, 200, 'assets/home_screen/big_stars.png')
game_over_title = uvage.from_image(640, 360, 'assets/home_screen/title.png')
game_over_title.scale_by(.8)
game_over_barrier = uvage.from_color(640, 100, 'black', .01, .01)
win_text = uvage.from_text(640, 600, 'YOU TRAVELED FASTER THAN THE SPEED OF LIGHT AND ESCAPED', 50, 'red', True)
lose_text = uvage.from_text(640, 600, 'YOU WERE CAUGHT BY THE BLACK HOLE', 50, 'red', True)
restart_text = uvage.from_text(640, 600, 'PRESS R TO RESTART', 50, 'red', True)


def game_over():
    global win
    if game_over_status:
        camera.center = [640, 360]
        # Movement
        if not game_over_title.top_touches(game_over_barrier):
            game_over_title.yspeed = -.25
            game_over_title.move_speed()

        camera.draw(game_over_background)
        camera.draw(game_over_barrier)
        camera.draw(game_over_title)
        if win:
            camera.draw(win_text)
        elif not win:
            camera.draw(lose_text)

        # camera.draw(restart_text)


        #black_hole
        black_hole.rotate(5)
        if black_hole.y <= 0 or black_hole.y >= camera.height - 125:
            black_hole.yspeed *= -1
        if black_hole.x <= 125 or black_hole.x >= camera.width - 125:
            black_hole.xspeed *= -1

        black_hole.move_speed()
        camera.draw(black_hole)


        # if uvage.is_pressing('r'):
        #     reset_level1()
        camera.display()



def reset_level1():
    global game_over_status, question_status, level_1_status, last_chance_status, star_collectable_1, star_collectable_2, star_collectable_3, \
        star_collectable_4, star_collectable_5

    player.center = [640, 360]
    camera.center = [640, 1000]
    black_hole.center = [640, 1100]
    game_over_status = False
    # last_chance_status = False

    # reset stars
    # star_collectable_1.center = [500, -150]
    # star_collectable_2.center = [400, -800]
    # star_collectable_3.center = [1100, -1700]
    # star_collectable_4.center = [700, -3750]
    # star_collectable_5.center = [600, -6150]
    level_1_status = True


def score_counting():
    global score_number_2
    if level_1_status:
        score_number_2 += .016


#
def tick():
    home_screen()
    level_1()
    game_over()
    score_counting()


uvage.timer_loop(60, tick)
