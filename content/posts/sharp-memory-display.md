+++
title = "Using Sharp Memory Display with Rust"
description = "Using Rust on STM32H7 to print on this odd display"
date = 2024-05-25
+++

Looking for an interesting mid-sized display with a good resolution, 
I stumbled accross this – Sharp's Memory Display. It looks like a display
you would find on an old digital clock or a calculator. It has 2.7",
resolution 400x240, no backlight, and is controlled using SPI.

![Breadboard picture](/pictures/sharp-memory-display-breadboard.jpg)

In this project, I'm using [Adafruit's breakout](https://www.adafruit.com/product/4694),
and I'm controlling it using [Daisy Seed](https://electro-smith.com/products/daisy-seed) platform.
The program is written in Rust.

# Wiring it up

This is how I wired the display up with my Daisy Seed. The CS and DISP pins
could be connected elsewhere, but there is no other SPI exposed on the board.

| Daisy Seed           | Display Breakout |
| -------------------- | ---------------- |
| 8 (D7 / SPI1 CS)     | CS               |
| 9 (D8 / SPI1 SCK)    | CLK              |
| 11 (D10 / SPI1 MOSI) | DI               |
| 12 (D11)             | DISP             |
| 38 (3V3 Digital)     | VIN              |
| 40 (DGND)            | GND              |

# Controlling the display

I recommend reading the [Programming Sharp’s Memory LCDs application note](datasheetdatasheethttps://www.sharpsde.com/fileadmin/products/Displays/2016_SDE_App_Note_for_Memory_LCD_programming_V1.3.pdf),
it is a fairly simple read. Pay attention to the explanation of VCOM.

If you want to understand more, compare the datasheet with the sources of the
[display driver](https://git.sr.ht/~doesnotcompete/sharp-memory-display/tree/main/item/src/lib.rs).

# The program

For this demo I used these crates:

* [`daisy = "0.8"`](https://crates.io/crates/daisy)
* [`embedded-graphics = "0.7"`](https://crates.io/crates/embedded-graphics)
* [`sharp-memory-display = "0.3"`](https://crates.io/crates/sharp-memory-display)


The full program can be found on [GitHub](https://github.com/phoracek/phoracek.github.io/tree/main/code/sharp-memory-display).
Commented code of the key parts follows.

Initializing resources using the `daisy` crate:

```rust
let board = daisy::Board::take().unwrap();
let dp = pac::Peripherals::take().unwrap();

let ccdr = daisy::board_freeze_clocks!(board, dp);
let pins = daisy::board_split_gpios!(board, ccdr, dp);
let mut led = daisy::board_split_leds!(pins).USER;
```

Take pins based on the mapping mentioned above:

```rust
let sck = pins.GPIO.PIN_8.into_alternate();
let mosi = pins.GPIO.PIN_10.into_alternate();
let cs = pins.GPIO.PIN_7.into_push_pull_output();
let disp = pins.GPIO.PIN_11.into_push_pull_output();
let miso = NoMiso;
```

The display is controlled using SPI. Note that the speed of 2 MHz is the maximum
recommended by Sharp. Setting it faster may work, but you would risk damaging the
display (it gets hot):

```rust
let spi = dp.SPI1.spi(
    (sck, miso, mosi),
    sharp_memory_display::MODE,
    2.MHz(),
    ccdr.peripheral.SPI1,
    &ccdr.clocks,
);
```

Instantiate display's driver. `enable()` will power on the display.
`set_clear_state` configures the color to which `clear_buffer` zeroes
all pixels. Note that `On` here means "not lit up", since drawing a pixel
makes it dark (`Off`):

```rust
let mut display = MemoryDisplay::new(spi, cs, disp);
display.enable();
display.set_clear_state(BinaryColor::On);
display.clear_buffer();
```

This is standard `embedded-graphics` code, printing text to the middle of the
screen:

```rust
Text::with_alignment(
    "hello world",
    display.bounding_box().center(),
    MonoTextStyle::new(&FONT_9X18_BOLD, BinaryColor::Off),
    Alignment::Center,
)
.draw(&mut display)
.unwrap();
```

Finally, since the display is running in the software clock VCOM mode, an update
(even with no actual changes) must be sent at least once a second. In this
example, it is set every half a second. On board LED is toggled to signalize that the
program is still running:

```rust
loop {
    display.display_mode();
    led.toggle();
    asm::delay(480_000_000 / 2);
}
```

This is not perfect, since stopping the program without disabling the display
may result in display burn-in. It would be probably better to use the display
in external clock mode and supply the tick using a 555 chip. Or implementing
a panic handler that would call `disable()` on the display to shut it down
nicely.

If you use this code, make sure the program always runs when the display is
powered.

# Other resources

* [Display Datasheet](https://cdn-learn.adafruit.com/assets/assets/000/094/215/original/LS027B7DH01_Rev_Jun_2010.pdf)
