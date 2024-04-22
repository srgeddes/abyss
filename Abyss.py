import uvage

camera = uvage.Camera(1920, 1080, True)


# -------------------------------------------STATUS--------------------------------------------------------------------#
home_screen_status = True




# -------------------------------------------HOME SCREEN ASSETS--------------------------------------------------------#
home_screen_count = 0
home_screen_background = uvage.from_image(5400, 360, 'assets/home_screen/big_stars.png')
home_screen_title = uvage.from_image(0, 0, 'assets/home_screen/title.png')
home_screen_start = uvage.from_image(0, 0, 'assets/home_screen/start.png')
home_screen_menu_star = uvage.from_image(0, 0, 'assets/home_screen/menu_star.png')

home_screen_assets = [home_screen_background, home_screen_title, home_screen_start, home_screen_menu_star]
home_screen_start.scale_by(.4)
home_screen_menu_star.scale_by(.4)


# -------------------------------------------HOME SCREEN FUNCTIONS-----------------------------------------------------#
def home_screen():
    global home_screen_status, home_screen_count, home_screen_menu_star
    home_screen_count += .4
    if home_screen_status:
        # Home Screen Assets adjustment
        home_screen_title.center = [960 + home_screen_count, 400]
        home_screen_start.center = [960 + home_screen_count, 700]
        home_screen_menu_star.center = [1150 + home_screen_count, 700]

        # Draw
        for i in home_screen_assets:
            camera.draw(i)



        # Movement (Scrolling)
        camera.move(.4, 0)
        home_screen_title.xspeed = .4
        home_screen_title.move_speed()
        if home_screen_background.right_touches(home_screen_title):
            home_screen_background.move(5000, 0)
        camera.display()








def tick():
    home_screen()


uvage.timer_loop(60, tick)



