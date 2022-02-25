def on_button_pressed_a():
    global preveiw_int
    if IsReady == "False":
        preveiw_int += -1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global IsReady
    if IsReady == "False":
        IsReady = "True"
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global preveiw_int
    if IsReady == "False":
        preveiw_int += 1
input.on_button_pressed(Button.B, on_button_pressed_b)

bit_5 = 0
carry_4 = 0
bit_4 = 0
carry_3 = 0
bit_3 = 0
carry_2 = 0
bit_2 = 0
carry_1 = 0
bit_1 = 0
dec = 0
preveiw_int = 0
IsReady = ""
IsReady = "False"

def on_forever():
    global dec, bit_1, carry_1, bit_2, carry_2, bit_3, carry_3, bit_4, carry_4, bit_5
    if IsReady == "True":
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
        basic.show_string("" + str(bit_5) + str(bit_4) + str(bit_3) + str(bit_2) + str(bit_1))
        basic.show_string("press reset")
        while True:
            basic.show_leds("""
                . . # . .
                                # # # # .
                                # . # . #
                                # . . . #
                                # # # # #
            """)
basic.forever(on_forever)

def on_forever2():
    while IsReady == "False":
        basic.show_string("" + str((preveiw_int)))
basic.forever(on_forever2)
