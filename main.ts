input.onButtonPressed(Button.A, function () {
    cookies += click_power
    basic.showIcon(IconNames.Happy)
    basic.pause(150)
    basic.showNumber(cookies)
})
input.onButtonPressed(Button.B, function () {
    cost = 10 * (auto_clickers + 1)
    if (cookies >= cost) {
        cookies += 0 - cost
        auto_clickers += 1
        basic.showIcon(IconNames.Yes)
        basic.pause(300)
        basic.showString("Lvl " + ("" + auto_clickers))
    } else {
        basic.showIcon(IconNames.No)
        basic.pause(300)
        basic.showString("Need " + ("" + cost))
    }
})
input.onGesture(Gesture.Shake, function () {
    cookies = 0
    auto_clickers = 0
    basic.showIcon(IconNames.Sad)
    basic.pause(500)
    basic.showString("Reset")
})
let auto_clickers = 0
let cost = 0
let cookies = 0
let click_power = 0
click_power = 1
basic.forever(function () {
    if (auto_clickers > 0) {
        cookies += auto_clickers
        basic.pause(800)
    }
})
