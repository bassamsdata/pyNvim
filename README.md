# pyNvim - Minimal Python Neovim Configuration

A minimal Neovim configuration primarily focused on Python development.

## Installation

1.  **Create the configuration directory:**
    Open your terminal and create the specific directory for this configuration:
    ```bash
    mkdir -p ~/.config/pyNvim
    ```

2.  **Clone the repository:**
    Clone this repository into the newly created directory:
    ```bash
    git clone https://github.com/bassamsdata/pyNvim.git ~/.config/pyNvim
    ```

## Usage

To use this configuration without affecting your default Neovim setup, always start Neovim with the following command:

```bash
NVIM_APPNAME=pyNvim nvim
```

This command tells Neovim to load its configuration from the `~/.config/pyNvim` directory instead of the default `~/.config/nvim`.

## First Run

The first time you launch Neovim using the `NVIM_APPNAME=pyNvim nvim` command, plugin manager (like `lazy.nvim`) might need to install the configured plugins.

After cloning and launching Neovim for the first time with the command above, close Neovim (`:q`) and open it again using the same command (`NVIM_APPNAME=pyNvim nvim`). Everything should now be set up and working.

## Test with Python file

the repo has one python simple file named `main.py`, so you run after the frist run:

```bash
NVIM_APPNAME=pyNvim nvim main.py
```
