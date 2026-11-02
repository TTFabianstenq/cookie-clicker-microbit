cookies = 0
auto_clickers = 0
click_power = 1

def on_button_pressed_a():
    global cookies
    cookies += click_power
    basic.show_icon(IconNames.HAPPY)
    basic.pause(150)
    basic.show_number(cookies)

input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global cookies, auto_clickers
    cost = 10 * (auto_clickers + 1)
    if cookies >= cost:
        cookies -= cost
        auto_clickers += 1
        basic.show_icon(IconNames.YES)
        basic.pause(300)
        basic.show_string("Lvl " + str(auto_clickers))
    else:
        basic.show_icon(IconNames.NO)
        basic.pause(300)
        basic.show_string("Need " + str(cost))

input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global cookies, auto_clickers
    cookies = 0
    auto_clickers = 0
    basic.show_icon(IconNames.SAD)
    basic.pause(500)
    basic.show_string("Reset")

input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    global cookies
    if auto_clickers > 0:
        cookies += auto_clickers
        basic.pause(800)

basic.forever(on_forever)