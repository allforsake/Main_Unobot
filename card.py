#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Colors
RED = 'r'
BLUE = 'b'
GREEN = 'g'
YELLOW = 'y'
BLACK = 'x'

COLORS = (RED, BLUE, GREEN, YELLOW)

COLOR_ICONS = {
    RED: '❤️',
    BLUE: '💙',
    GREEN: '💚',
    YELLOW: '💛',
    BLACK: '⬛️'
}

# Values
ZERO = '0'
ONE = '1'
TWO = '2'
THREE = '3'
FOUR = '4'
FIVE = '5'
SIX = '6'
SEVEN = '7'
EIGHT = '8'
NINE = '9'
DRAW_TWO = 'draw_two'
DRAW_FOUR = 'draw_four'
REVERSE = 'reverse'
SKIP = 'skip'
DISCARD_ALL = 'discard_all'
SKIP_EVERYONE = 'skip_everyone'

VALUES = (ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, DRAW_TWO,
          REVERSE, SKIP, DRAW_FOUR, DISCARD_ALL, SKIP_EVERYONE)

# Special cards
DRAW_TEN = 'draw_ten'
REVERSE_DRAW_FOUR = 'reverse_draw_four'
DRAW_SIX = 'draw_six'

SPECIALS = (DRAW_TEN, REVERSE_DRAW_FOUR, DRAW_SIX)

CARDS_CLASSIC = {
    "normal": {
        "b_0": "CAACAgIAAxkBAAFA0uVn5CqdJK2uBVB--spJwIXpBLIJpQAC320AAnSoGEum_5ZWd8-gsDYE",
        "b_1": "CAACAgIAAxkBAAFA0vFn5CqhdLqM2-bjb91aLnArSjrUDgAC8noAAtq2GUtcJY1qj6kHuzYE",
        "b_2": "CAACAgIAAxkBAAFA0vdn5CqlRFIqRDcmr32Gfnn7RZ9ZVQACd2kAAlRVGUvuaSAJdNJLtzYE",
        "b_3": "CAACAgIAAxkBAAFA0v1n5Cqo8eqWZ_P26pZwnk1Dyc6XnQACknsAAuizGUvv2Chb-Wgl7DYE",
        "b_4": "CAACAgIAAxkBAAFA0wdn5Cqr9D-yk-fcqQFeopQ2DmwUqwACRHIAAlgSGEs_GfdctJ_5wjYE",
        "b_5": "CAACAgIAAxkBAAFA0w1n5CquF1nx_MHjNCmsUs3I1ORhXwACFW4AAnn0GUvT52h1lgzvvTYE",
        "b_6": "CAACAgIAAxkBAAFA0w9n5Cqx7tcIKPxd0x5tTiSQZGBVMgACzHsAAhZ6GUuZevqaKLZFsDYE",
        "b_7": "CAACAgIAAxkBAAFA0xNn5Cq0Y3FFrKFu8n8m8TJ-cyL2tAACrnAAAioBGEu7Jl4F922h2DYE",
        "b_8": "CAACAgIAAxkBAAFA0yFn5Cq339DGGaulJAhGy2YRES_GuAACRHIAAklbGUuklN_F09npbDYE",
        "b_9": "CAACAgIAAxkBAAFA0ydn5Cq5OthPaJpkgteRZx_iRKQvtQACAnwAAra1GEud22PaqcxUmTYE",
        "b_draw_two": "CAACAgIAAxkBAAFA0zFn5Cq9lsnPwPz8gRcSfu9wQCNgWQAC23YAAnzLGEvePnUvtDdOGDYE",
        "b_draw_four": "CAACAgIAAxkBAAFA0zln5Cq__pyUvD1mCdYHofqQiLXzbAAC1nYAAvSIGEsSSnbRhNFKNDYE",
        "b_skip": "CAACAgIAAxkBAAFA0z9n5CrEap9I7VbLcPNlvFYJ3d39mgACWnUAAoIJGUswx3bFVH6rAzYE",
        "b_skip_everyone": "CAACAgIAAxkBAAFA01tn5CrKVZeQ9N5pfRYmmfKoJ5zY7gACbHEAAolnGEuTAAG9JNWLhx42BA",
        "b_discard_all": "CAACAgIAAxkBAAFA029n5CrOqUlUYitaikA5ubJMctiWAgACbH0AAh35GUsmlCSzVFftwTYE",
        "b_reverse": "CAACAgIAAxkBAAFA001n5CrH2omCLpfBIGK8WaoxMNgonwACj3MAAkHxGEuMoBlQjoixRTYE",
        "g_0": "CAACAgIAAxkBAAFA059n5CrZAmP8mDYKRFThi23sDP_wOAACN3wAAswHGUtNKXKosc6b-TYE",
        "g_1": "CAACAgIAAxkBAAFA069n5CrgI6XFK8CNLZDPxcKbHVxBCwACsG8AAl7GGUtduxGAes5tFDYE",
        "g_2": "CAACAgIAAxkBAAFA071n5CrkqMPcaje9Zb3g07SvwVQukQACe2gAAkkuGEuhW9mNwAzajTYE",
        "g_3": "CAACAgIAAxkBAAFA08tn5CrndI8-KjQO30sCK11GDJXRiwACyGgAAmK6GUsfNiPfHHi7QTYE",
        "g_4": "CAACAgIAAxkBAAFA09Nn5CrrHHMIB1mCRdInjlS5ct7dYQACgmgAAsFQGEvokZwFGHSgIzYE",
        "g_5": "CAACAgIAAxkBAAFA09ln5Cruj-_LR8YoBrZiBBP3orVFUAAC8Y8AAmgsGUurytL0kknrSDYE",
        "g_6": "CAACAgIAAxkBAAFA099n5CrylXhPxqSrX_zEC2_eupOLBAAC4HoAAqGxGEtIZKZSAxwndTYE",
        "g_7": "CAACAgIAAxkBAAFA0-ln5Cr1bn8Sf5XMRj7sKD--Q93INgACGncAAt65GUuqoZWFA7nzHzYE",
        "g_8": "CAACAgIAAxkBAAFA0-9n5Cr64U2ReQzbm7fRAAEmLk7T6agAAgx3AAIN2xhLYk8SeDUzXuw2BA",
        "g_9": "CAACAgIAAxkBAAFA0_Zn5Cr9ccowNmEWW6xyvOEgHt1sugACgmUAAminGUvNSdKbwNB8BTYE",
        "g_draw_two": "CAACAgIAAxkBAAFA0_pn5CsBi5iAA_uxWRLufSU6p0oiIQAC2W4AAvyIGUtlRr3MDFJrkjYE",
        "g_draw_four": "CAACAgIAAxkBAAFA1AABZ-QrBOeZbb-xql50M2QEHK69rcAAArdxAAIdXBhLhdYpfopPV1Q2BA",
        "g_skip_everyone": "CAACAgIAAxkBAAFA1Bpn5CsPuq9tyGKCS5bLd_NqFqe39QACUHcAAlYGGUtz8ybM0g6jcjYE",
        "g_discard_all": "CAACAgIAAxkBAAFA1Cdn5CsTmV2uk0NYmHt57kUxMECs4gACvnIAAq8MGEtlBDhY-3nRdzYE",
        "g_skip": "CAACAgIAAxkBAAFA1AVn5CsIcOjlCA1EnD4F9Z6GrbRMAwACZWcAAt2JGEt2AAEkkUJ_Wdo2BA",
        "g_reverse": "CAACAgIAAxkBAAFA1BRn5CsLD0P1OvKBr29jgGmxSF3OuwACInsAAtFZGUsd9kL6IcaA9jYE",
        "r_0": "CAACAgIAAxkBAAFA1DNn5CsY3Y3bvRpYwfySirNKTG_09AACOXQAAnnqGUviFyCbwbJNyDYE",
        "r_1": "CAACAgIAAxkBAAFA1Dxn5Cscp7KeRmVbgHdIaj9UauM9gQACKm8AAnnSGEuDLwvo3qhfbjYE",
        "r_2": "CAACAgIAAxkBAAFA1Ehn5CskMf9Bg5VKooc1QpIIr4Hh2QAChHQAAl_0GEv_j78-jhRHCjYE",
        "r_3": "CAACAgIAAxkBAAFA1Exn5Csn3lkvhPfBBCC5BzqJEpKKqwAC3XYAAjLvGEtUsntPSnysNTYE",
        "r_4": "CAACAgIAAxkBAAFA1FBn5Csqx4MpBdu_Dx6zKKw3wsAHuQACE3MAAjm_GEuY_VwfBJL6GTYE",
        "r_5": "CAACAgIAAxkBAAFA1FRn5Csv3NJAieVv_S3c5f3fXizXNQAC72QAAmyIGUuX2AtxmAv4vDYE",
        "r_6": "CAACAgIAAxkBAAFA1Fhn5CszwrYVIxECwwABmTplcV-ZgToAArhiAAIYsxlLwOTkEl3ifwI2BA",
        "r_7": "CAACAgIAAxkBAAFA1GRn5Cs3mb2ktjpcT9wVYLeLsJj3AgACgm0AAmd7GEuFRErLrJKS4DYE",
        "r_8": "CAACAgIAAxkBAAFA1HBn5Cs7UAm-gTso9KUGrS127yrWaAACV3UAAhgAARhLwvRW_JXpsSs2BA",
        "r_9": "CAACAgIAAxkBAAFA1IRn5CtCtFIGwUes1w5gkIoNjiUlyQACXnMAAg3xGEuFBO3ToZ0c1TYE",
        "r_draw_two": "CAACAgIAAxkBAAFA1Ixn5CtG1wXotS2XYfg5BOGqSgpQEgACaXQAAqN4GEsOmbA03hdGszYE",
        "r_draw_four": "CAACAgIAAxkBAAFA1JZn5CtLZApFLXueDMwSk9_RW1KmegACxmUAAnisGEu4jPF4PuO7bzYE",
        "r_skip_everyone": "CAACAgIAAxkBAAFA1MJn5CtdLynOoT8-t0hJn67tThjEkgAC1GYAAh_6GUszOA5Sjx5RRzYE",
        "r_discard_all": "CAACAgIAAxkBAAFA1M5n5Ctha3ukyuoZgySeKadGqSj-xAACjW0AAldzGUtnNqYrki9m3zYE",
        "r_skip": "CAACAgIAAxkBAAFA1KJn5CtQEuB1YxjxvD1Q0QYcCCXkqgACDGwAAlhZGEvxXqvZhRCm4TYE",
        "r_reverse": "CAACAgIAAxkBAAFA1LRn5CtZyrsBN_vuHmS3RH1j2hSeigACTW4AAuQeGUtcAAEtEdZlTf82BA",
        "y_0": "CAACAgIAAxkBAAFA1OBn5CtnDZ0k0OKnWSZuXKTStA0tBAACjWoAAlB-GEt2k7rUq8AnujYE",
        "y_1": "CAACAgIAAxkBAAFA1PJn5CtrVXO7SwLsm2g6kAABzv2eoIUAAh1rAAJsyxhL3lWr8-f8T4A2BA",
        "y_2": "CAACAgIAAxkBAAFA1Qhn5Ctv1YkzEj1bIb4eiL7iqR4CAwACS20AAoTwGEu4v5DbEnwnRjYE",
        "y_3": "CAACAgIAAxkBAAFA1Q5n5Ctz-5FQ9w9nAoD6UzcwA6nKnAAC0HAAAqJUGUtRUXTlxnireTYE",
        "y_4": "CAACAgIAAxkBAAFA1R9n5Ct44EEvLJ5JNiHzr-xdlrkt0gACymwAAh4SGEud7QF_07Z9ITYE",
        "y_5": "CAACAgIAAxkBAAFA1S9n5Ct8hEEV9yx3FL9db8SBDIhCNwACvmQAApfcGUvVTep1cELNpjYE",
        "y_6": "CAACAgIAAxkBAAFA1Ttn5CuAalxL5UATwlLpPH_ol410HwACvnMAApDYGEtgiLUG0nJ0IjYE",
        "y_7": "CAACAgIAAxkBAAFA1UNn5CuE7kkYuUudBr8493Z-yWZmLwACzXcAAqsCGEvoGyxIOoRGBTYE",
        "y_8": "CAACAgIAAxkBAAFA1VFn5CuIOJ4FTE6Ip1NpK67xvYYWvAACOoAAAiQnGUvTAAGREM09u0g2BA",
        "y_9": "CAACAgIAAxkBAAFA1Vtn5CuMTa6NITk3xScYglHfiifzdgACw20AAkaZGUvZlqwPqQYYSjYE",
        "y_draw_two": "CAACAgIAAxkBAAFA1Wln5CuQdGXJ3BYOgBxnbFkP4LH68QACo3YAAhUXGEuWDFVvE_527zYE",
        "y_draw_four": "CAACAgIAAxkBAAFA1XNn5CuUOq2wMM-ilPn2jdMQ3MC7EgAC42kAAlrYGEsFMkwYGlJP9DYE",
        "y_skip_everyone": "CAACAgIAAxkBAAFA1aFn5CumUKz-lkSjMl-kmbpidX5cSgAC5XIAAgnKGEu2OjK7wB0MOTYE",
        "y_discard_all": "CAACAgIAAxkBAAFA1a1n5CuqyEazmFFXUt5Rp6ARLIvEpgAC0moAAlEZGEu5uaZk_7M3LjYE",
        "y_skip": "CAACAgIAAxkBAAFA1Xdn5CuZA3KZstZVqhU7355fMsh34gACV3IAAurBIUuYLUwfuVn9rTYE",
        "y_reverse": "CAACAgIAAxkBAAFA1Zln5CuiKsPVDX6GBkFHp4fxurn7MQACkGEAAjHSGUv4ZoaOPRBwNjYE",
        "reverse_draw_four": "CAACAgIAAxkBAAFA0sVn5CqAmTXi0agfDzkdDCU4xKP7XAACiXYAAgrMGUusZtA4sBwQFzYE",
        "draw_six": "CAACAgIAAxkBAAFAmppn46oqWrO35hUvv02Ja4ZIC4jixAACJ3YAAr1BGEvo7rFzRxAxqjYE",
        "draw_ten": "CAACAgIAAxkBAAFAmlpn46jO8Jv5Z5Nqlt-YaClEPMpJIwACsnYAAus0GUvesMCWW01hLzYE",
    },
    "not_playable": {
        "b_0": "CAACAgIAAxkBAAFA0uVn5CqdJK2uBVB--spJwIXpBLIJpQAC320AAnSoGEum_5ZWd8-gsDYE",
        "b_1": "CAACAgIAAxkBAAFA0vFn5CqhdLqM2-bjb91aLnArSjrUDgAC8noAAtq2GUtcJY1qj6kHuzYE",
        "b_2": "CAACAgIAAxkBAAFA0vdn5CqlRFIqRDcmr32Gfnn7RZ9ZVQACd2kAAlRVGUvuaSAJdNJLtzYE",
        "b_3": "CAACAgIAAxkBAAFA0v1n5Cqo8eqWZ_P26pZwnk1Dyc6XnQACknsAAuizGUvv2Chb-Wgl7DYE",
        "b_4": "CAACAgIAAxkBAAFA0wdn5Cqr9D-yk-fcqQFeopQ2DmwUqwACRHIAAlgSGEs_GfdctJ_5wjYE",
        "b_5": "CAACAgIAAxkBAAFA0w1n5CquF1nx_MHjNCmsUs3I1ORhXwACFW4AAnn0GUvT52h1lgzvvTYE",
        "b_6": "CAACAgIAAxkBAAFA0w9n5Cqx7tcIKPxd0x5tTiSQZGBVMgACzHsAAhZ6GUuZevqaKLZFsDYE",
        "b_7": "CAACAgIAAxkBAAFA0xNn5Cq0Y3FFrKFu8n8m8TJ-cyL2tAACrnAAAioBGEu7Jl4F922h2DYE",
        "b_8": "CAACAgIAAxkBAAFA0yFn5Cq339DGGaulJAhGy2YRES_GuAACRHIAAklbGUuklN_F09npbDYE",
        "b_9": "CAACAgIAAxkBAAFA0ydn5Cq5OthPaJpkgteRZx_iRKQvtQACAnwAAra1GEud22PaqcxUmTYE",
        "b_draw_two": "CAACAgIAAxkBAAFA0zFn5Cq9lsnPwPz8gRcSfu9wQCNgWQAC23YAAnzLGEvePnUvtDdOGDYE",
        "b_draw_four": "CAACAgIAAxkBAAFA0zln5Cq__pyUvD1mCdYHofqQiLXzbAAC1nYAAvSIGEsSSnbRhNFKNDYE",
        "b_skip": "CAACAgIAAxkBAAFA0z9n5CrEap9I7VbLcPNlvFYJ3d39mgACWnUAAoIJGUswx3bFVH6rAzYE",
        "b_skip_everyone": "CAACAgIAAxkBAAFA01tn5CrKVZeQ9N5pfRYmmfKoJ5zY7gACbHEAAolnGEuTAAG9JNWLhx42BA",
        "b_discard_all": "CAACAgIAAxkBAAFA029n5CrOqUlUYitaikA5ubJMctiWAgACbH0AAh35GUsmlCSzVFftwTYE",
        "b_reverse": "CAACAgIAAxkBAAFA001n5CrH2omCLpfBIGK8WaoxMNgonwACj3MAAkHxGEuMoBlQjoixRTYE",
        "g_0": "CAACAgIAAxkBAAFA059n5CrZAmP8mDYKRFThi23sDP_wOAACN3wAAswHGUtNKXKosc6b-TYE",
        "g_1": "CAACAgIAAxkBAAFA069n5CrgI6XFK8CNLZDPxcKbHVxBCwACsG8AAl7GGUtduxGAes5tFDYE",
        "g_2": "CAACAgIAAxkBAAFA071n5CrkqMPcaje9Zb3g07SvwVQukQACe2gAAkkuGEuhW9mNwAzajTYE",
        "g_3": "CAACAgIAAxkBAAFA08tn5CrndI8-KjQO30sCK11GDJXRiwACyGgAAmK6GUsfNiPfHHi7QTYE",
        "g_4": "CAACAgIAAxkBAAFA09Nn5CrrHHMIB1mCRdInjlS5ct7dYQACgmgAAsFQGEvokZwFGHSgIzYE",
        "g_5": "CAACAgIAAxkBAAFA09ln5Cruj-_LR8YoBrZiBBP3orVFUAAC8Y8AAmgsGUurytL0kknrSDYE",
        "g_6": "CAACAgIAAxkBAAFA099n5CrylXhPxqSrX_zEC2_eupOLBAAC4HoAAqGxGEtIZKZSAxwndTYE",
        "g_7": "CAACAgIAAxkBAAFA0-ln5Cr1bn8Sf5XMRj7sKD--Q93INgACGncAAt65GUuqoZWFA7nzHzYE",
        "g_8": "CAACAgIAAxkBAAFA0-9n5Cr64U2ReQzbm7fRAAEmLk7T6agAAgx3AAIN2xhLYk8SeDUzXuw2BA",
        "g_9": "CAACAgIAAxkBAAFA0_Zn5Cr9ccowNmEWW6xyvOEgHt1sugACgmUAAminGUvNSdKbwNB8BTYE",
        "g_draw_two": "CAACAgIAAxkBAAFA0_pn5CsBi5iAA_uxWRLufSU6p0oiIQAC2W4AAvyIGUtlRr3MDFJrkjYE",
        "g_draw_four": "CAACAgIAAxkBAAFA1AABZ-QrBOeZbb-xql50M2QEHK69rcAAArdxAAIdXBhLhdYpfopPV1Q2BA",
        "g_skip_everyone": "CAACAgIAAxkBAAFA1Bpn5CsPuq9tyGKCS5bLd_NqFqe39QACUHcAAlYGGUtz8ybM0g6jcjYE",
        "g_discard_all": "CAACAgIAAxkBAAFA1Cdn5CsTmV2uk0NYmHt57kUxMECs4gACvnIAAq8MGEtlBDhY-3nRdzYE",
        "g_skip": "CAACAgIAAxkBAAFA1AVn5CsIcOjlCA1EnD4F9Z6GrbRMAwACZWcAAt2JGEt2AAEkkUJ_Wdo2BA",
        "g_reverse": "CAACAgIAAxkBAAFA1BRn5CsLD0P1OvKBr29jgGmxSF3OuwACInsAAtFZGUsd9kL6IcaA9jYE",
        "r_0": "CAACAgIAAxkBAAFA1DNn5CsY3Y3bvRpYwfySirNKTG_09AACOXQAAnnqGUviFyCbwbJNyDYE",
        "r_1": "CAACAgIAAxkBAAFA1Dxn5Cscp7KeRmVbgHdIaj9UauM9gQACKm8AAnnSGEuDLwvo3qhfbjYE",
        "r_2": "CAACAgIAAxkBAAFA1Ehn5CskMf9Bg5VKooc1QpIIr4Hh2QAChHQAAl_0GEv_j78-jhRHCjYE",
        "r_3": "CAACAgIAAxkBAAFA1Exn5Csn3lkvhPfBBCC5BzqJEpKKqwAC3XYAAjLvGEtUsntPSnysNTYE",
        "r_4": "CAACAgIAAxkBAAFA1FBn5Csqx4MpBdu_Dx6zKKw3wsAHuQACE3MAAjm_GEuY_VwfBJL6GTYE",
        "r_5": "CAACAgIAAxkBAAFA1FRn5Csv3NJAieVv_S3c5f3fXizXNQAC72QAAmyIGUuX2AtxmAv4vDYE",
        "r_6": "CAACAgIAAxkBAAFA1Fhn5CszwrYVIxECwwABmTplcV-ZgToAArhiAAIYsxlLwOTkEl3ifwI2BA",
        "r_7": "CAACAgIAAxkBAAFA1GRn5Cs3mb2ktjpcT9wVYLeLsJj3AgACgm0AAmd7GEuFRErLrJKS4DYE",
        "r_8": "CAACAgIAAxkBAAFA1HBn5Cs7UAm-gTso9KUGrS127yrWaAACV3UAAhgAARhLwvRW_JXpsSs2BA",
        "r_9": "CAACAgIAAxkBAAFA1IRn5CtCtFIGwUes1w5gkIoNjiUlyQACXnMAAg3xGEuFBO3ToZ0c1TYE",
        "r_draw_two": "CAACAgIAAxkBAAFA1Ixn5CtG1wXotS2XYfg5BOGqSgpQEgACaXQAAqN4GEsOmbA03hdGszYE",
        "r_draw_four": "CAACAgIAAxkBAAFA1JZn5CtLZApFLXueDMwSk9_RW1KmegACxmUAAnisGEu4jPF4PuO7bzYE",
        "r_skip_everyone": "CAACAgIAAxkBAAFA1MJn5CtdLynOoT8-t0hJn67tThjEkgAC1GYAAh_6GUszOA5Sjx5RRzYE",
        "r_discard_all": "CAACAgIAAxkBAAFA1M5n5Ctha3ukyuoZgySeKadGqSj-xAACjW0AAldzGUtnNqYrki9m3zYE",
        "r_skip": "CAACAgIAAxkBAAFA1KJn5CtQEuB1YxjxvD1Q0QYcCCXkqgACDGwAAlhZGEvxXqvZhRCm4TYE",
        "r_reverse": "CAACAgIAAxkBAAFA1LRn5CtZyrsBN_vuHmS3RH1j2hSeigACTW4AAuQeGUtcAAEtEdZlTf82BA",
        "y_0": "CAACAgIAAxkBAAFA1OBn5CtnDZ0k0OKnWSZuXKTStA0tBAACjWoAAlB-GEt2k7rUq8AnujYE",
        "y_1": "CAACAgIAAxkBAAFA1PJn5CtrVXO7SwLsm2g6kAABzv2eoIUAAh1rAAJsyxhL3lWr8-f8T4A2BA",
        "y_2": "CAACAgIAAxkBAAFA1Qhn5Ctv1YkzEj1bIb4eiL7iqR4CAwACS20AAoTwGEu4v5DbEnwnRjYE",
        "y_3": "CAACAgIAAxkBAAFA1Q5n5Ctz-5FQ9w9nAoD6UzcwA6nKnAAC0HAAAqJUGUtRUXTlxnireTYE",
        "y_4": "CAACAgIAAxkBAAFA1R9n5Ct44EEvLJ5JNiHzr-xdlrkt0gACymwAAh4SGEud7QF_07Z9ITYE",
        "y_5": "CAACAgIAAxkBAAFA1S9n5Ct8hEEV9yx3FL9db8SBDIhCNwACvmQAApfcGUvVTep1cELNpjYE",
        "y_6": "CAACAgIAAxkBAAFA1Ttn5CuAalxL5UATwlLpPH_ol410HwACvnMAApDYGEtgiLUG0nJ0IjYE",
        "y_7": "CAACAgIAAxkBAAFA1UNn5CuE7kkYuUudBr8493Z-yWZmLwACzXcAAqsCGEvoGyxIOoRGBTYE",
        "y_8": "CAACAgIAAxkBAAFA1VFn5CuIOJ4FTE6Ip1NpK67xvYYWvAACOoAAAiQnGUvTAAGREM09u0g2BA",
        "y_9": "CAACAgIAAxkBAAFA1Vtn5CuMTa6NITk3xScYglHfiifzdgACw20AAkaZGUvZlqwPqQYYSjYE",
        "y_draw_two": "CAACAgIAAxkBAAFA1Wln5CuQdGXJ3BYOgBxnbFkP4LH68QACo3YAAhUXGEuWDFVvE_527zYE",
        "y_draw_four": "CAACAgIAAxkBAAFA1XNn5CuUOq2wMM-ilPn2jdMQ3MC7EgAC42kAAlrYGEsFMkwYGlJP9DYE",
        "y_skip_everyone": "CAACAgIAAxkBAAFA1aFn5CumUKz-lkSjMl-kmbpidX5cSgAC5XIAAgnKGEu2OjK7wB0MOTYE",
        "y_discard_all": "CAACAgIAAxkBAAFA1a1n5CuqyEazmFFXUt5Rp6ARLIvEpgAC0moAAlEZGEu5uaZk_7M3LjYE",
        "y_skip": "CAACAgIAAxkBAAFA1Xdn5CuZA3KZstZVqhU7355fMsh34gACV3IAAurBIUuYLUwfuVn9rTYE",
        "y_reverse": "CAACAgIAAxkBAAFA1Zln5CuiKsPVDX6GBkFHp4fxurn7MQACkGEAAjHSGUv4ZoaOPRBwNjYE",
        "reverse_draw_four": "CAACAgIAAxkBAAFA0sVn5CqAmTXi0agfDzkdDCU4xKP7XAACiXYAAgrMGUusZtA4sBwQFzYE",
        "draw_six": "CAACAgIAAxkBAAFAmppn46oqWrO35hUvv02Ja4ZIC4jixAACJ3YAAr1BGEvo7rFzRxAxqjYE",
        "draw_ten": "CAACAgIAAxkBAAFAmlpn46jO8Jv5Z5Nqlt-YaClEPMpJIwACsnYAAus0GUvesMCWW01hLzYE",
    },
}

STICKERS_OPTIONS = {
    "option_draw": "BQADBAAD-AIAAl9XmQABxEjEcFM-VHIC",
    "option_pass": "BQADBAAD-gIAAl9XmQABcEkAAbaZ4SicAg",
    "option_bluff": "BQADBAADygIAAl9XmQABJoLfB9ntI2UC",
    "option_info": "BQADBAADxAIAAl9XmQABC5v3Z77VLfEC",
}

# TODO: Support multiple card packs
# For now, just use classic colorblind
STICKERS = {
    **CARDS_CLASSIC["normal"],
    **STICKERS_OPTIONS,
}

STICKERS_GREY = {
    **CARDS_CLASSIC["not_playable"],
}


class Card(object):
    """This class represents an UNO card"""

    def __init__(self, color, value, special=None):
        self.color = color
        self.value = value
        self.special = special

    def __str__(self):
        if self.special:
            return self.special
        else:
            return '%s_%s' % (self.color, self.value)

    def __repr__(self):
        if self.special:
            return '%s%s%s' % (COLOR_ICONS.get(self.color, ''),
                               COLOR_ICONS[BLACK],
                               ' '.join([s.capitalize()
                                         for s in self.special.split('_')]))
        else:
            return '%s%s' % (COLOR_ICONS[self.color], self.value.capitalize())

    def __eq__(self, other):
        """Needed for sorting the cards"""
        return str(self) == str(other)

    def __lt__(self, other):
        """Needed for sorting the cards"""
        return str(self) < str(other)


def from_str(string):
    """Decodes a Card object from a string"""
    if string not in SPECIALS:
        color, value = string.split('_')
        return Card(color, value)
    else:
        return Card(None, None, string)
