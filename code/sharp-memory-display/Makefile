CARGO = cargo

.PHONY: all
all: format clippy

.PHONY: check-format
check-format:
	$(CARGO) fmt --all -- --check

.PHONY: format
format:
	$(CARGO) fmt --all

.PHONY: clippy
clippy:
	$(CARGO) clippy --all

.PHONY: update
update:
	$(CARGO) update

.PHONY: clean
clean:
	$(CARGO) clean

.PHONY: flash
flash:
	$(CARGO) run --release

.PHONY: flash-dfu
flash-dfu:
	$(CARGO) objcopy --release -- -O binary target/arplus.bin
	dfu-util -a 0 -s 0x08000000:leave -D target/arplus.bin -d ,0483:df11
