#![no_main]
#![no_std]

use cortex_m::asm;
use cortex_m_rt::entry;
use defmt_rtt as _;
use panic_probe as _;

use embedded_graphics::{
    mono_font::{ascii::FONT_9X18_BOLD, MonoTextStyle},
    pixelcolor::BinaryColor,
    prelude::*,
    text::{Alignment, Text},
};
use sharp_memory_display::*;
use stm32h7xx_hal::{pac, prelude::*, spi::NoMiso};

#[entry]
fn main() -> ! {
    defmt::info!("Starting up, initializing resources");

    let board = daisy::Board::take().unwrap();
    let dp = pac::Peripherals::take().unwrap();

    let ccdr = daisy::board_freeze_clocks!(board, dp);
    let pins = daisy::board_split_gpios!(board, ccdr, dp);
    let mut led = daisy::board_split_leds!(pins).USER;

    let sck = pins.GPIO.PIN_8.into_alternate();
    let mosi = pins.GPIO.PIN_10.into_alternate();
    let cs = pins.GPIO.PIN_7.into_push_pull_output();
    let disp = pins.GPIO.PIN_11.into_push_pull_output();
    let miso = NoMiso;

    let spi = dp.SPI1.spi(
        (sck, miso, mosi),
        sharp_memory_display::MODE,
        2.MHz(),
        ccdr.peripheral.SPI1,
        &ccdr.clocks,
    );

    defmt::info!("Instantiating embedded graphics display");

    let mut display = MemoryDisplay::new(spi, cs, disp);
    display.enable();
    display.set_clear_state(BinaryColor::On);
    display.clear_buffer();

    defmt::info!("Printing on the screen");

    Text::with_alignment(
        "hello world",
        display.bounding_box().center(),
        MonoTextStyle::new(&FONT_9X18_BOLD, BinaryColor::Off),
        Alignment::Center,
    )
    .draw(&mut display)
    .unwrap();

    defmt::info!("Entering idle loop, refreshing the display");

    loop {
        display.display_mode();

        led.toggle();
        asm::delay(240_000_000);
    }
}
