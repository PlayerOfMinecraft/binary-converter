input.onButtonPressed(Button.A, function () {
    if (IsReady == "False") {
        preveiw_int += -1
    }
})
input.onButtonPressed(Button.AB, function () {
    if (IsReady == "False") {
        IsReady = "True"
    }
})
input.onButtonPressed(Button.B, function () {
    if (IsReady == "False") {
        preveiw_int += 1
    }
})
let bit_6 = 0
let carry_5 = 0
let bit_5 = 0
let carry_4 = 0
let bit_4 = 0
let carry_3 = 0
let bit_3 = 0
let carry_2 = 0
let bit_2 = 0
let carry_1 = 0
let bit_1 = 0
let dec = 0
let preveiw_int = 0
let IsReady = ""
IsReady = "False"
basic.forever(function () {
    while (IsReady == "False") {
        basic.showString("" + preveiw_int)
    }
})
basic.forever(function () {
    if (IsReady == "True") {
        dec = preveiw_int
        bit_1 = dec % 2
        carry_1 = Math.floor(dec / 2)
        bit_2 = carry_1 % 2
        carry_2 = Math.floor(carry_1 / 2)
        bit_3 = carry_2 % 2
        carry_3 = Math.floor(carry_2 / 2)
        bit_4 = carry_3 % 2
        carry_4 = Math.floor(carry_3 / 2)
        bit_5 = carry_4 % 2
        carry_5 = Math.floor(carry_4 / 2)
        bit_6 = carry_5 % 2
        basic.showString("" + bit_6 + ("" + bit_5) + ("" + bit_4) + ("" + bit_3) + ("" + bit_2) + ("" + bit_1))
        basic.showString("press reset")
        while (true) {
            basic.showLeds(`
                . . # . .
                # # # # .
                # . # . #
                # . . . #
                # # # # #
                `)
        }
    }
})
